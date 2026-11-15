"""Check selected, versioned documentary limits; never infer complete approval."""
import math


def evaluate_operation(result, profiles):
    reference = result.get("reference") or {}
    profile = profiles.get(reference.get("dataset")) if isinstance(profiles,dict) else None
    if not isinstance(profile, dict) or result.get("scenario") == "unignited_baseline":
        return {"status":"unknown", "title":"SAFETY CHECKS: UNKNOWN",
                "message":"No applicable versioned operating profile is selected for this scenario.",
                "checks":[], "pending":["Select the applicable equipment and operating protocol."],
                "scope":"Documentary checks, not complete equipment approval."}
    checks = []
    for rule in profile.get("rules", []):
        if not isinstance(rule, dict):
            continue
        value = result.get("input", {}).get(rule.get("field"))
        valid = isinstance(value, (int,float)) and not isinstance(value,bool) and math.isfinite(value)
        bounds = [rule.get("min"),rule.get("max")]
        if any(v is not None and (isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v)) for v in bounds):
            continue
        passed = valid and (bounds[0] is None or value >= bounds[0]-1e-9) and (bounds[1] is None or value <= bounds[1]+1e-9)
        checks.append({"label":rule.get("label",rule.get("field")), "status":"pass" if passed else "fail" if valid else "pending",
                       "input":value if valid else None, "unit":rule.get("unit"), "min":bounds[0],"max":bounds[1],
                       "source_title":profile.get("source_title"),"source_url":profile.get("source_url"),
                       "pdf_page":rule.get("pdf_page",profile.get("pdf_page")), "source_id":profile.get("source_id"),
                       "source_sha256":profile.get("source_sha256"),"qualifier":rule.get("qualifier")})
    failed = sum(c["status"]=="fail" for c in checks)
    passed = sum(c["status"]=="pass" for c in checks)
    status = "fail" if failed else "conditional_pass" if checks and passed==len(checks) else "unknown"
    message = ("Outside the selected archived protocol's checked limits; do not treat this as an approved operating point." if failed else
               f"{passed}/{len(checks)} numeric protocol checks passed. Required procedures and remaining hardware conditions are pending.")
    return {"status":status,"title":"SAFETY CHECKS: "+{"fail":"FAIL","conditional_pass":"CONDITIONAL PASS","unknown":"UNKNOWN"}[status],
            "message":message,"checks":checks,"pending":profile.get("pending",[]),"profile":profile.get("profile"),
            "scope":"Selected archived protocol numeric checks only; conditional pass is not complete operating approval or predicted freedom from fire."}
