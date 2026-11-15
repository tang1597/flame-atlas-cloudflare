"""Read-only comparison of uploaded liquid records and their stored predictions.

No fitting or coefficient reconstruction occurs here. Original model outputs can
be replayed at source records or, when explicitly requested, geometrically
interpolated as a labeled research display; the original models are not executed.
"""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import math
import numbers
from pathlib import Path

try:
    from scipy.spatial import Delaunay as _Delaunay
    from scipy.spatial import QhullError as _QhullError
except ImportError:  # replay and one-dimensional interpolation remain usable
    _Delaunay = None
    _QhullError = RuntimeError


AXES = ("diameter_mm", "pressure_kpa", "oxygen_percent")
_TARGETS = {
    "PSI-69": (
        ("visible_extinction_time_s", "Visible extinction time", "s",
         "std_duration_s", "pred_visible_extinction_time_s",
         "Conditional on source-reported visible extinction; not extinction probability."),
        ("burning_rate_constant_m2_s", "Average burning-rate constant", "m2/s",
         "std_burning_rate_constant_m2_s", "pred_burning_rate_constant_m2_s",
         "Source average droplet D-squared slope; not flame size or a full trajectory."),
    ),
    "PSI-39": (
        ("hot_flame_duration_s", "Hot-flame duration", "s",
         "std_hot_flame_duration_s", "pred_hot_flame_duration_s",
         "Hot-flame stage only; not total hot-plus-cool lifetime."),
        ("hot_burning_rate_constant_m2_s", "Hot-stage burning-rate constant", "m2/s",
         "std_hot_burning_rate_constant_m2_s", "pred_hot_burning_rate_constant_m2_s",
         "Hot-stage droplet D-squared slope; not a full trajectory."),
        ("cool_burning_rate_constant_m2_s", "Cool-stage burning-rate constant", "m2/s",
         "std_cool_burning_rate_constant_m2_s", "pred_cool_burning_rate_constant_m2_s",
         "Conditional cool-stage value; does not predict whether a cool flame occurs."),
    ),
}
_SCHEMA_CATALOG = "liquid-catalog-v1"
_SCHEMA_COMPARE = "liquid-compare-v1"
_STUDIES = {
    "PSI-39": [{
        "id": "PSI-39",
        "title": "Cool Flames Investigation (CFI)",
        "source_url": "https://psi.nasa.gov/physci/repo/data/investigations/PSI-39",
        "data_url": "https://psi.nasa.gov/physci/repo/data/investigations/PSI-39",
        "summary": "Reported liquid-droplet conditions and hot/cool-stage measurements.",
    }],
    "PSI-69": [{
        "id": "PSI-69",
        "title": "Flame Extinguishment Experiment (FLEX)",
        "source_url": "https://psi.nasa.gov/physci/repo/data/investigations/PSI-69",
        "data_url": "https://psi.nasa.gov/physci/repo/data/investigations/PSI-69",
        "summary": "Reported liquid-droplet conditions, burning rates and conditional visible-extinction measurements.",
    }, {
        "id": "NTRS-20150023456",
        "title": "Detailed Results From the Flame Extinguishment Experiment (FLEX) March 2009 to December 2011",
        "source_url": "https://ntrs.nasa.gov/citations/20150023456",
        "data_url": "https://psi.nasa.gov/physci/repo/data/investigations/PSI-69",
        "summary": "NASA report on droplet histories and visible-extinction measurements from FLEX.",
    }],
}


def _number(value):
    """Preserve unknowns and reject non-finite source values; never zero-fill."""
    if value is None or isinstance(value, bool):
        return None
    try:
        result = float(value)
    except (ValueError, TypeError, OverflowError):
        return None
    return result if math.isfinite(result) else None


def _object(value):
    try:
        result = json.loads(value or "{}")
    except (TypeError, ValueError):
        return {}
    return result if isinstance(result, dict) else {}


def _near(left, right):
    return math.isclose(left, right, rel_tol=1e-10, abs_tol=1e-10)


def _same_optional(left, right):
    return left is None and right is None or (
        left is not None and right is not None and _near(left, right)
    )


def _percent(row, normalized, original):
    value = _number(row.get(normalized))
    return value * 100.0 if value is not None else _number(row.get(original))


def _conditions(row):
    diameter = _number(row.get("std_initial_droplet_diameter_m"))
    pressure = _number(row.get("std_pressure_Pa"))
    oxygen = _number(row.get("std_oxygen_fraction"))
    return {
        "diameter_mm": diameter * 1000 if diameter is not None else None,
        "pressure_kpa": pressure / 1000 if pressure is not None else None,
        "oxygen_percent": oxygen * 100 if oxygen is not None else None,
        "nitrogen_percent": _percent(row, "std_ambient_nitrogen_fraction", "nitrogen (mol %)"),
        "helium_percent": _percent(row, "std_ambient_helium_fraction", "helium (mol %)"),
        "carbon_dioxide_percent": _percent(row, "std_ambient_carbon_dioxide_fraction", "carbon_dioxide (mol %)"),
    }


def _ranges(records):
    return {axis: {"min": min(r["conditions"][axis] for r in records),
                   "max": max(r["conditions"][axis] for r in records)}
            for axis in AXES}


def _controls(records):
    ranges = _ranges(records)
    return {axis: {**bounds, "step": step} for axis, bounds, step in (
        ("diameter_mm", ranges["diameter_mm"], 0.001),
        ("pressure_kpa", ranges["pressure_kpa"], 0.001),
        ("oxygen_percent", ranges["oxygen_percent"], 0.01),
    )}


def _mixture_context(conditions):
    parts = []
    for label, key in (("He", "helium_percent"), ("CO2", "carbon_dioxide_percent"), ("N2", "nitrogen_percent")):
        value = conditions[key]
        parts.append(label + " " + ("unknown" if value is None else f"{value:g}%"))
    return "Source mixture: " + "; ".join(parts) + ". These are the fixed reference values."


def _search_terms(fuel):
    """Discovery aliases only; they do not establish purity or molecular isomer."""
    terms = [fuel]
    name = fuel.casefold()
    if "methanol" in name or "ch3oh" in name:
        terms.extend(("methanol", "CH3OH", "甲醇"))
    if "heptane" in name or "c7h16" in name:
        terms.extend(("heptane", "C7H16", "庚烷"))
    if "dodecane" in name or "c12h26" in name:
        terms.extend(("dodecane", "C12H26", "十二烷"))
        if any(marker in name for marker in ("iso", "[.", "/", "mixture", "blend")):
            terms.extend(("dodecane mixture", "dodecane blend", "十二烷混合物", "isomer composition as reported"))
    return list(dict.fromkeys(terms))


def _fuel_presentation(fuel):
    # CFI Final Science Report, physical PDF p.6, identifies the mixtures by mass.
    names = {
        "Methanol": ("Methanol", "Methanol (CH3OH)", "pure", 0),
        "Heptane": ("n-Heptane", "n-Heptane (C7H16)", "pure", 1),
        "C12H26": ("n-Dodecane", "n-Dodecane (C12H26)", "pure", 2),
        "[.60]/[.40] C12H26/iso-dodecane": ("Dodecane blend · 60/40 wt%", "60 wt% n-dodecane + 40 wt% isododecane; CFI Final Science Report p.6.", "binary_blend", 3),
        "[.75]/[.25] C12H26/iso-dodecane": ("Dodecane blend · 75/25 wt%", "75 wt% n-dodecane + 25 wt% isododecane; CFI Final Science Report p.6.", "binary_blend", 4),
    }
    label, description, kind, order = names.get(fuel, (fuel, fuel, "as_reported", 10))
    return {"label": label, "description": description, "formulation_kind": kind, "display_order": order}


def _baseline(reference):
    return {
        "diameter_mm": reference["conditions"]["diameter_mm"],
        "pressure_kpa": 101.325, "oxygen_percent": 21,
        "temperature_K": None, "ignition_source": "not_present_assumption",
        "state": "unignited_assumption",
        "assurance": "scenario_preset_not_measured_or_validated_safe",
    }


def _surface_coordinates(conditions):
    return (math.log(conditions["diameter_mm"]),
            math.log(conditions["pressure_kpa"]), conditions["oxygen_percent"] / 100)


def _eligible_surface_anchor(record, metric):
    value, metadata = metric["predicted"], metric["metadata"]
    return (value is not None and value > 0 and metric["status"] != "unavailable"
            and metadata.get("domain") == "within_marginal_training_envelope_not_joint_domain_guarantee"
            and metadata.get("validation_kind") in ("group_held_out", "full_fit_unlabelled_row")
            and metadata.get("result_class") == "data_fitted_prediction"
            and metadata.get("model_id") == record["dataset"] + "_" + metric["observed_field"])


def _build_stored_surface(records, metric_id):
    """Construct only geometry of stored outputs: no fit, optimizer or calibration."""
    grouped = {}
    for record in records:
        metric = next(m for m in record["metrics"] if m["id"] == metric_id)
        if _eligible_surface_anchor(record, metric):
            grouped.setdefault(_surface_coordinates(record["conditions"]), []).append((record, metric))
    points = sorted(grouped)
    if not points:
        return {"error": "no_eligible_positive_stored_outputs"}
    minimum = [min(point[axis] for point in points) for axis in range(3)]
    maximum = [max(point[axis] for point in points) for axis in range(3)]
    active = [axis for axis in range(3) if not _near(minimum[axis], maximum[axis])]
    normalized = [[(point[axis] - minimum[axis]) / (maximum[axis] - minimum[axis])
                   for axis in active] for point in points]
    surface = {"points": points, "groups": grouped, "minimum": minimum,
               "maximum": maximum, "active": active, "normalized": normalized,
               "triangulation": None, "error": None,
               "helium_percent": records[0]["conditions"]["helium_percent"],
               "carbon_dioxide_percent": records[0]["conditions"]["carbon_dioxide_percent"]}
    if len(active) >= 2:
        if _Delaunay is None:
            surface["error"] = "scipy_unavailable_for_multidimensional_surface"
        elif len(points) < len(active) + 1:
            surface["error"] = "insufficient_points_for_surface_dimension"
        else:
            try:
                # Qhull receives only fixed normalized coordinates, never target values.
                surface["triangulation"] = _Delaunay(normalized)
            except (_QhullError, ValueError):
                surface["error"] = "degenerate_stored_surface_geometry"
    return surface


def _interpolate_surface(surface, requested, preferred_id):
    """Return convex log-output interpolation and its exact source weights."""
    if "points" not in surface:
        return None, surface["error"]
    query = _surface_coordinates(requested)
    points, groups = surface["points"], surface["groups"]
    active, minimum, maximum = surface["active"], surface["minimum"], surface["maximum"]
    for axis in range(3):
        if axis not in active and not _near(query[axis], minimum[axis]):
            return None, "query_differs_from_constant_source_axis"
        if query[axis] < minimum[axis] and not _near(query[axis], minimum[axis]) or query[axis] > maximum[axis] and not _near(query[axis], maximum[axis]):
            return None, "outside_target_source_marginal_range"
    # Exact source nodes use a stored value, preferring held-out provenance; no
    # artificial averaging of a known record or claim of a newly validated OOF.
    exact_point = next((point for point in points if all(_near(a, b) for a, b in zip(point, query))), None)
    exact_entry = None
    if exact_point is not None:
        exact_entry = min(groups[exact_point], key=lambda entry: (
            entry[0]["id"] != preferred_id,
            entry[1]["metadata"].get("validation_kind") != "group_held_out", entry[0]["id"]))
        vertices = [(points.index(exact_point), 1.0)]
    elif not active:
        return None, "zero_dimensional_surface_requires_exact_source_point"
    elif len(active) == 1:
        axis = active[0]
        ordered = sorted(range(len(points)), key=lambda index: points[index][axis])
        position = next((position for position, index in enumerate(ordered) if points[index][axis] > query[axis]), None)
        if position is None or position == 0:
            return None, "outside_stored_output_convex_hull"
        left, right = ordered[position - 1], ordered[position]
        weight = (query[axis] - points[left][axis]) / (points[right][axis] - points[left][axis])
        vertices = [(left, 1 - weight), (right, weight)]
    else:
        if surface["error"]:
            return None, surface["error"]
        triangulation = surface["triangulation"]
        normalized_query = [(query[axis] - minimum[axis]) / (maximum[axis] - minimum[axis]) for axis in active]
        simplex = int(triangulation.find_simplex([normalized_query], tol=1e-10)[0])
        if simplex < 0:
            return None, "outside_stored_output_convex_hull"
        transform = triangulation.transform[simplex]
        dimension = len(active)
        barycentric = [sum(float(transform[i][j]) * (normalized_query[j] - float(transform[dimension][j]))
                           for j in range(dimension)) for i in range(dimension)]
        barycentric.append(1 - sum(barycentric))
        if any(not math.isfinite(value) or value < -1e-8 for value in barycentric):
            return None, "invalid_surface_barycentric_weights"
        # Clamp numerical roundoff only; no extrapolation and no optimized weights.
        barycentric = [max(0.0, min(1.0, value)) for value in barycentric]
        weight_sum = sum(barycentric)
        if weight_sum <= 0:
            return None, "invalid_surface_barycentric_weights"
        vertices = [(int(index), float(weight / weight_sum)) for index, weight in
                    zip(triangulation.simplices[simplex], barycentric) if weight > 0]
    contributors = []
    logarithm = 0.0
    for index, vertex_weight in vertices:
        entries = [exact_entry] if exact_entry is not None else groups[points[index]]
        for record, metric in entries:
            weight = vertex_weight / len(entries)
            logarithm += weight * math.log(metric["predicted"])
            contributors.append({
                "source_id": record["id"], "weight": float(weight),
                "test_id": record["test_id"], "source_row": record["source_row"],
                "std_input_record_number": record["std_input_record_number"],
                "stored_prediction": metric["predicted"],
                "validation_kind": metric["metadata"].get("validation_kind", "unknown"),
                "fold": metric["metadata"].get("fold"),
                "domain": metric["metadata"].get("domain", "unknown"),
            })
    try:
        value = math.exp(logarithm)
    except OverflowError:
        return None, "nonfinite_surface_result"
    if not math.isfinite(value) or value <= 0:
        return None, "nonfinite_surface_result"
    return {
        "value": value,
        "provenance": {
            "method": "log_output_barycentric", "result_class": "stored_output_interpolation",
            "transforms": {"diameter_mm": "natural_log", "pressure_kpa": "natural_log", "oxygen_percent": "divide_by_100"},
            "geometry_normalization": "per_target_source_min_max_on_active_transformed_axes",
            "active_axes": [AXES[axis] for axis in active], "contributors": contributors,
            "source_point_count": len(points), "uncertainty": None,
            "independently_validated": False, "original_model_executed": False,
            "fixed_reference_helium_percent": surface["helium_percent"],
            "fixed_reference_carbon_dioxide_percent": surface["carbon_dioxide_percent"],
            "composition_equivalence_established": False,
            "composition_note": "Matching stored model features does not establish identical physical composition; unreported CO2 remains unknown.",
            "uses_full_fit_unlabelled_outputs": any(c["validation_kind"] == "full_fit_unlabelled_row" for c in contributors),
            "full_fit_note": "Full-fit outputs at unlabelled rows, when used, are not held-out measurements or independent validation.",
            "coincident_points": "Equal log-output weights for coincident vertices; an exact source node prefers one existing held-out value.",
        },
    }, None


def _public_metadata(metadata, field_status):
    """Return scalar provenance only, without original machine-specific paths."""
    keys = {
        "resultClass": "result_class", "modelId": "model_id",
        "validationKind": "validation_kind", "fold": "fold", "scope": "scope",
        "inputSHA256": "input_sha256", "unit": "unit", "assurance": "assurance",
    }
    result = {out: metadata[key] for key, out in keys.items()
              if key in metadata and isinstance(metadata[key], (str, int, float, type(None)))
              and not isinstance(metadata[key], bool)}
    if "validation_kind" not in result and isinstance(field_status.get("validationKind"), str):
        result["validation_kind"] = field_status["validationKind"]
    if "scope" not in result and isinstance(field_status.get("scope"), str):
        result["scope"] = field_status["scope"]
    # These flags belong to each target, not to an entire source row.
    result["domain"] = field_status.get("domain") if isinstance(field_status.get("domain"), str) else "unknown"
    result["uncertainty"] = None  # no calibrated per-record interval supplied
    return result


def _stored_metrics(row):
    dataset = row["dataset"]
    result_metadata = _object(row.get("pred_result_metadata"))
    field_statuses = _object(row.get("pred_field_status"))
    result = []
    for metric_id, label, unit, observed_field, predicted_field, scope in _TARGETS[dataset]:
        observed = _number(row.get(observed_field))
        predicted = _number(row.get(predicted_field))
        metadata = result_metadata.get(predicted_field, {})
        field_status = field_statuses.get(predicted_field, {})
        metadata = metadata if isinstance(metadata, dict) else {}
        field_status = field_status if isinstance(field_status, dict) else {}
        if dataset == "PSI-69" and metric_id == "visible_extinction_time_s":
            # The legacy alias has the same conditional meaning, never generic burn time.
            if predicted is None:
                predicted = _number(row.get("pred_flex_duration_s"))
                metadata = result_metadata.get("pred_flex_duration_s", metadata)
                field_status = field_statuses.get("pred_flex_duration_s", field_status)
                metadata = metadata if isinstance(metadata, dict) else {}
                field_status = field_status if isinstance(field_status, dict) else {}
        reason = None
        if dataset == "PSI-39" and str(row.get("std_source_analysis_complete", "")).lower() != "true":
            reason = "source_analysis_incomplete"
        elif dataset == "PSI-69" and metric_id == "visible_extinction_time_s" and row.get("outcome", "").strip().lower() != "extinction":
            reason = "requires_source_reported_visible_extinction"
        elif metric_id == "cool_burning_rate_constant_m2_s" and not (
            observed is not None and observed > 0
            or str(row.get("std_cool_flame_reported", "")).lower() in ("true", "yes")
        ):
            # A full-fit value is a conditional value, not evidence of a cool-stage event.
            reason = "source_cool_stage_not_established"
        if reason:
            observed = predicted = None
        status = "unavailable" if reason or observed is None and predicted is None else "stored_source_values"
        metric = {
            "id": metric_id, "label": label, "unit": unit,
            "observed": observed, "predicted": predicted,
            "observed_field": observed_field, "prediction_field": predicted_field,
            "scope": scope, "status": status,
            "reason": reason or ("target_and_prediction_missing" if status == "unavailable" else None),
            "metadata": _public_metadata(metadata, field_status),
        }
        if observed is not None and predicted is not None:
            metric["absolute_error"] = abs(predicted - observed)
            metric["relative_error_percent"] = abs(predicted - observed) / abs(observed) * 100 if observed != 0 else None
        else:
            metric["absolute_error"] = None
            metric["relative_error_percent"] = None
        result.append(metric)
    return result


class LiquidRepository:
    """Cached scalar replay and labeled stored-output interpolation for PSI-39/69."""

    def __init__(self, path):
        self._path = Path(path)
        digest = hashlib.sha256()
        with self._path.open("rb") as source:
            for block in iter(lambda: source.read(1024 * 1024), b""):
                digest.update(block)
        self.source_sha256 = digest.hexdigest()
        self._records = []
        self._by_id = {}
        self._fuels = {}
        self._surface_cache = {}
        with self._path.open("r", encoding="utf-8-sig", newline="") as source:
            reader = csv.DictReader(source)
            for record_index, row in enumerate(reader, 1):
                dataset = row.get("dataset")
                expected_experiment = {"PSI-39": "CFI", "PSI-69": "FLEX"}.get(dataset)
                if not expected_experiment or row.get("experiment", "").upper() != expected_experiment or row.get("record_type") != "Test":
                    continue
                conditions = _conditions(row)
                if any(conditions[axis] is None for axis in AXES):
                    continue
                if not 0 < conditions["diameter_mm"] <= 1000 or not 0 < conditions["pressure_kpa"] <= 100000 or not 0 <= conditions["oxygen_percent"] <= 100:
                    continue
                # Catalog eligibility does not promote incomplete targets to measurements.
                targets = _TARGETS[dataset]
                fields = [field for target in targets for field in target[3:5]]
                if not any(_number(row.get(field)) is not None for field in fields):
                    continue
                fuel = row.get("fuel", "").strip()
                if not fuel:
                    continue
                fuel_id = dataset + ":" + hashlib.sha256(fuel.encode("utf-8")).hexdigest()[:16]
                source_hash = row.get("std_source_sha256", "").strip() or self.source_sha256
                # Upload record number, rather than test ID, preserves duplicate source IDs.
                record_number = row.get("std_input_record_number", "").strip() or str(record_index)
                record_id = source_hash + ":" + record_number
                if record_id in self._by_id:
                    record_id += ":csv" + str(record_index)
                record = {
                    "id": record_id, "fuel_id": fuel_id, "fuel": fuel,
                    "label": f"{expected_experiment} {row.get('test_id', '')} · record {record_number}",
                    "dataset": dataset, "experiment": expected_experiment,
                    "test_id": row.get("test_id", ""), "source_row": row.get("source_row") or None,
                    "std_input_record_number": record_number, "source_sha256": source_hash,
                    "source_url": "https://psi.nasa.gov/physci/repo/data/investigations/" + dataset,
                    "source_locator": (row.get("std_source_relative_path") or row.get("source") or "source table").replace("\\", "/").rsplit("/", 1)[-1] + " · row " + (row.get("source_row") or "unknown"),
                    "conditions": conditions, "metrics": _stored_metrics(row),
                    "mixture_context": _mixture_context(conditions),
                }
                self._records.append(record)
                self._by_id[record_id] = record
                self._fuels.setdefault(fuel_id, []).append(record)
        self._default = next((r for r in self._records if r["dataset"] == "PSI-39" and r["test_id"] == "1206" and r["std_input_record_number"] == "1382"), self._records[0] if self._records else None)
        if self._default:
            self._default = self._best_reference(self._fuels[self._default["fuel_id"]], self._default)
        self._catalog = self._make_catalog()

    @staticmethod
    def _best_reference(records, preferred):
        if all(_eligible_surface_anchor(preferred, metric) for metric in preferred["metrics"]):
            return preferred
        complete = next((record for record in records if all(_eligible_surface_anchor(record, metric) for metric in record["metrics"])), None)
        if complete:
            return complete
        return max(records, key=lambda record: (
            sum(_eligible_surface_anchor(record, metric) for metric in record["metrics"]),
            record["id"] == preferred["id"]))

    def _default_for_fuel(self, fuel_id):
        if self._default and self._default["fuel_id"] == fuel_id:
            return self._default
        records = self._fuels[fuel_id]
        return self._best_reference(records, records[0])

    def _demo_preset(self, fuel_id, records):
        reference = self._default_for_fuel(fuel_id)
        recipe_keys = ("helium_percent", "carbon_dioxide_percent")
        compatible = [record for record in records if all(
            _same_optional(record["conditions"][gas], reference["conditions"][gas]) for gas in recipe_keys)]
        common = [record for record in compatible if all(
            _eligible_surface_anchor(record, metric) for metric in record["metrics"])]
        parameters = {"fuel": fuel_id, "reference_id": reference["id"],
                      "scenario": "source_experiment", "prediction_method": "stored_surface",
                      "reference_policy": "nearest_compatible"}
        basis = "common_eligible_source_centroid_in_log_diameter_log_pressure_oxygen_fraction"
        if common:
            parameters.update(
                diameter_mm=math.exp(sum(math.log(record["conditions"]["diameter_mm"]) for record in common) / len(common)),
                pressure_kpa=math.exp(sum(math.log(record["conditions"]["pressure_kpa"]) for record in common) / len(common)),
                oxygen_percent=sum(record["conditions"]["oxygen_percent"] for record in common) / len(common))
            known_cfi = next((record for record in common if record["fuel"] == "C12H26" and record["test_id"] == "1206" and record["std_input_record_number"] == "1382"), None)
            if known_cfi:
                parameters.update(diameter_mm=4.5, pressure_kpa=150.0, oxygen_percent=20.0,
                                  reference_id=known_cfi["id"])
                basis = "checked_cfi_stored_surface_example"
            result = self.compare(parameters)
            if not all(metric["predicted"] is not None and metric["predicted"] > 0 for metric in result["metrics"]):
                # A geometrically degenerate surface or missing SciPy must not
                # produce a preset that claims unsupported slider predictions.
                reference = self._best_reference(common, reference if reference in common else common[0])
                parameters.update(reference_id=reference["id"], **{axis: reference["conditions"][axis] for axis in AXES})
                basis = "exact_eligible_source_fallback_surface_unavailable"
        else:
            # Explicit partial fallback: lookup only, never fill missing targets.
            reference = max(compatible, key=lambda record: sum(
                metric["predicted"] is not None and metric["predicted"] > 0 for metric in record["metrics"]))
            parameters.update(reference_id=reference["id"], **{axis: reference["conditions"][axis] for axis in AXES})
            basis = "partial_exact_source_fallback_no_common_eligible_targets"
        result = self.compare(parameters)
        count = sum(metric["predicted"] is not None and metric["predicted"] > 0 for metric in result["metrics"])
        complete = bool(common) and count == len(result["metrics"])
        return {key: value for key, value in parameters.items() if key != "fuel"} | {
            "metric_count": count, "target_count": len(result["metrics"]),
            "complete": complete, "partial": not complete, "basis": basis,
        }

    def _make_catalog(self):
        fuels = []
        for fuel_id, records in self._fuels.items():
            first = records[0]
            fuels.append({
                "id": fuel_id, "source_fuel": first["fuel"], **_fuel_presentation(first["fuel"]),
                "search_terms": _search_terms(first["fuel"]),
                "baseline": _baseline(self._default_for_fuel(fuel_id)),
                "demo_preset": self._demo_preset(fuel_id, records),
                "dataset": first["dataset"], "experiment": first["experiment"],
                "default_reference_id": self._default_for_fuel(fuel_id)["id"],
                "cases": [{"id": r["id"], "label": r["label"], "mixture_context": r["mixture_context"],
                           **{axis: r["conditions"][axis] for axis in AXES}}
                          for r in records],
                "controls": _controls(records),
            })
        fuels.sort(key=lambda fuel: (fuel["display_order"], fuel["label"]))
        return {
            "schema_version": _SCHEMA_CATALOG, "fuels": fuels,
            "default_fuel": self._default["fuel_id"] if self._default else None,
            "default_reference": self._default["id"] if self._default else None,
            "model_artifacts_available": False, "source_sha256": self.source_sha256,
            "range_note": "Source marginal ranges only; not a validated joint prediction or safety domain.",
            "stored_surface": {"method": "fixed_log_output_barycentric_display_interpolation",
                               "multidimensional_available": _Delaunay is not None,
                               "independently_validated": False},
        }

    def catalog(self):
        return copy.deepcopy(self._catalog)

    def compare(self, payload):
        if not isinstance(payload, dict):
            raise ValueError("Comparison input must be a JSON object.")
        if not self._default:
            raise ValueError("No eligible liquid experiment records are available.")
        scenario = payload.get("scenario", "source_experiment")
        if not isinstance(scenario, str) or scenario not in ("unignited_baseline", "source_experiment"):
            raise ValueError("Unknown scenario. Choose unignited_baseline or source_experiment.")
        reference_policy = payload.get("reference_policy", "fixed")
        if not isinstance(reference_policy, str) or reference_policy not in ("fixed", "nearest_compatible"):
            raise ValueError("Unknown reference policy. Choose fixed or nearest_compatible.")
        prediction_method = payload.get("prediction_method", "stored_replay")
        if not isinstance(prediction_method, str) or prediction_method not in ("stored_replay", "stored_surface"):
            raise ValueError("Unknown prediction method. Choose stored_replay or stored_surface.")
        fuel_id = payload.get("fuel", self._default["fuel_id"])
        if not isinstance(fuel_id, str) or fuel_id not in self._fuels:
            raise ValueError("Unknown liquid fuel selection.")
        selected_id = payload.get("reference_id", self._default_for_fuel(fuel_id)["id"])
        if not isinstance(selected_id, str) or selected_id not in self._by_id:
            raise ValueError("Unknown reference record.")
        selected = self._by_id[selected_id]
        if selected["fuel_id"] != fuel_id:
            raise ValueError("Reference record does not belong to the selected fuel.")
        defaults = _baseline(self._default_for_fuel(fuel_id)) if scenario == "unignited_baseline" else selected["conditions"]
        requested = {}
        for axis in AXES:
            value = payload.get(axis, defaults[axis])
            if isinstance(value, bool) or not isinstance(value, numbers.Real) or not math.isfinite(value):
                raise ValueError(axis + " must be a finite number.")
            value = float(value)
            if axis == "oxygen_percent":
                valid = 0 <= value <= 100
            else:
                valid = 0 < value <= (1000 if axis == "diameter_mm" else 100000)
            if not valid:
                raise ValueError(axis + " is outside the allowed physical input limits.")
            requested[axis] = value
        # Unknown diluent and a measured zero are different recipes.
        recipe_keys = ("helium_percent", "carbon_dioxide_percent")
        candidates = [r for r in self._fuels[fuel_id] if all(
            _same_optional(r["conditions"][gas], selected["conditions"][gas]) for gas in recipe_keys
        )]
        ranges = _ranges(candidates)
        reference = selected
        selection_method = "fixed_source_record"
        if reference_policy == "nearest_compatible":
            # Only an explicitly requested policy may choose another source row.
            # He/CO2 recipe remains bound to the original reference, including unknowns.
            def distance(record):
                total = 0.0
                for axis in AXES:
                    lower, upper = ranges[axis]["min"], ranges[axis]["max"]
                    scale = upper - lower or max(abs(lower), 1.0)
                    total += ((requested[axis] - record["conditions"][axis]) / scale) ** 2
                return total, record["id"] != selected_id, record["id"]
            reference = min(candidates, key=distance)
            selection_method = "nearest_compatible_source_marginal_distance"
        exact = all(_near(requested[axis], reference["conditions"][axis]) for axis in AXES)
        reasons = []
        for axis in AXES:
            if requested[axis] < ranges[axis]["min"] and not _near(requested[axis], ranges[axis]["min"]) or requested[axis] > ranges[axis]["max"] and not _near(requested[axis], ranges[axis]["max"]):
                reasons.append(axis + "_outside_source_marginal_range")
        known_diluent = sum(selected["conditions"][gas] or 0 for gas in recipe_keys)
        if requested["oxygen_percent"] + known_diluent > 100 + 1e-8:
            reasons.append("oxygen_and_fixed_diluents_exceed_100_percent")
        if reasons:
            support_status = "outside_data_range"
            support_message = "Outside source marginal ranges or incompatible with the fixed diluent recipe. No new prediction is available."
        elif exact:
            support_status = "exact_record"
            support_message = "Exact source record. Values below replay its existing stored predictions; no model was run."
        else:
            support_status = "within_marginal_ranges"
            support_message = "Within individual source ranges only; joint support is not established. Frozen model exports are missing, so no prediction is available at this new condition."
        condition_match = "outside_documented_range" if support_status == "outside_data_range" else "exact_documented" if exact else "within_marginal_ranges_only"
        unignited = scenario == "unignited_baseline"
        if unignited:
            reasons.append("unignited_scenario_not_supported_by_post_ignition_targets")
            if support_status != "outside_data_range":
                support_status = "insufficient_evidence"
            support_message = "Unignited is a user scenario assumption. The stored post-ignition targets do not model ignition state or establish storage, leakage, or ignition safety; no current-condition comparison is available."
        replay = exact and not reasons and not unignited
        stored = copy.deepcopy(reference["metrics"])
        metrics = copy.deepcopy(stored)
        if not replay:
            for metric in metrics:
                metric.update(observed=None, predicted=None, absolute_error=None,
                              relative_error_percent=None,
                              status="unavailable", reason="unignited_scenario_not_supported_by_post_ignition_targets" if unignited else "no_experiment_or_frozen_model_at_requested_conditions")
                metric["metadata"] = {"domain": "unknown", "uncertainty": None}
        prediction_mode = "unavailable_unignited_scenario" if unignited else "stored_prediction_replay" if replay else "unavailable_missing_frozen_model"
        target_statuses = {}
        if prediction_method == "stored_surface" and not replay and not unignited:
            interpolated = False
            for metric in metrics:
                key = (tuple(record["id"] for record in candidates), metric["id"])
                if key not in self._surface_cache:
                    self._surface_cache[key] = _build_stored_surface(candidates, metric["id"])
                result, reason = _interpolate_surface(self._surface_cache[key], requested, selected_id)
                if result is not None:
                    interpolated = True
                    metric.update(predicted=result["value"], observed=None, absolute_error=None,
                                  relative_error_percent=None, status="interpolated_stored_outputs", reason=None,
                                  interpolation=result["provenance"],
                                  metadata={"result_class": "stored_output_interpolation",
                                            "validation_kind": "not_independently_validated",
                                            "domain": "within_stored_output_convex_hull_only",
                                            "uncertainty": None})
                    target_statuses[metric["id"]] = "within_stored_output_convex_hull"
                else:
                    metric["reason"] = reason
                    target_statuses[metric["id"]] = reason
            if interpolated:
                prediction_mode = "stored_output_interpolation"
                support_status = "within_surface_support"
                support_message = "Displayed targets use fixed geometric interpolation inside their stored-output convex hulls. This research display does not execute or validate the original models, establish identical composition, or establish equipment safety."
            else:
                prediction_mode = "unavailable_outside_surface_support"
                support_status = "outside_surface_support"
                support_message = "No target has usable stored-output surface support here. Individual ranges do not guarantee convex-hull support; no extrapolated output is shown."
        public_reference = {key: copy.deepcopy(value) for key, value in reference.items()
                            if key not in ("metrics", "fuel_id")}
        public_reference["selected_reference_id"] = selected_id
        echoed_input = {"fuel": fuel_id, "reference_id": selected_id, **requested}
        if "scenario" in payload:
            echoed_input["scenario"] = scenario
        if "reference_policy" in payload:
            echoed_input["reference_policy"] = reference_policy
        if "prediction_method" in payload:
            echoed_input["prediction_method"] = prediction_method
        if unignited:
            assessment = {
                "active_fire": "not_specified", "safety": "not_established",
                "basis": "User scenario assumes no heating or ignition; stored data are post-ignition and do not validate storage/leak/ignition safety.",
            }
        else:
            assessment = {
                "context": "chamber_operation", "active_fire": "source_experiment_burned",
                "safety": "not_established",
                "test_condition_match": condition_match,
                "basis": "Flames are intentional in the chamber. Equipment safety requires pressure/thermal ratings, containment and operating procedures; these are not supplied by this CSV.",
            }
        assessment["selection_method"] = selection_method
        return {
            "schema_version": _SCHEMA_COMPARE,
            "input": echoed_input, "scenario": scenario,
            "prediction_mode": prediction_mode,
            "reference_matches_input": replay, "reference": public_reference,
            "metrics": metrics, "stored_metrics": stored,
            "support": {"status": support_status, "message": support_message, "reasons": reasons,
                        "range_basis": "selected_fuel_and_fixed_reference_helium_carbon_dioxide_recipe",
                        "marginal_ranges": ranges,
                        "target_statuses": target_statuses,
                        "ignition_state_supported": False,
                        "joint_domain_validated": False},
            "assessment": assessment,
            "studies": copy.deepcopy(_STUDIES[reference["dataset"]]),
            "safety": {"status": "not_established", "message": "SAFETY NOT ESTABLISHED. These conditional scalar experiment results do not establish ignition risk, fire occurrence, safe operation, or a suppression threshold."},
            "model_artifacts_available": False, "source_sha256": self.source_sha256,
            "model": {
                "method": "Fixed geometric display interpolation of existing stored model outputs; original models not executed." if prediction_method == "stored_surface" and not replay else "Stored outputs from the document-reported P1-P5 log-Ridge models; no model executed.",
                "limits": [
                    "Frozen v6 coefficients and scalers are missing; arbitrary new conditions cannot be evaluated.",
                    "No calibrated per-record prediction interval is supplied.",
                    "Conditional scalar targets do not establish ignition, fire occurrence, or operational safety.",
                    "Feature marginal ranges do not establish a jointly validated prediction domain.",
                ],
            },
        }
