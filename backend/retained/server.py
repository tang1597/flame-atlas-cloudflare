"""Loopback English safety dashboard over reviewed offline evidence chains."""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

from evidence_search import FrozenRetriever, read_json, search, validate_chains
from liquid_compare import LiquidRepository
from scenario_search import ScenarioResearch
from operating_limits import evaluate_operation
from gas_case import catalog as gas_case_catalog
from strategy_catalog import CatalogUnavailable, StrategyCatalog
from habitat_atlas import HabitatAtlas
from habitat_evidence_links import attach_evidence_links

BASE = Path(__file__).resolve().parent
WORKSPACE = BASE.parent.parent
DATA = WORKSPACE / "output/earth_space_transfer_20261114/phase8_fire_safety_dashboard_20261114"
STATIC = {".html", ".js", ".css", ".svg", ".png", ".jpg", ".ico", ".ttf", ".otf", ".woff2", ".txt"}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def reply(self, body, status=200, content_type="application/json; charset=utf-8"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def send_json(self, value, status=200):
        self.reply(json.dumps(value, ensure_ascii=False, allow_nan=False).encode("utf-8"), status)

    def valid_request(self):
        hosts = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
        if self.headers.get("Host", "").lower() not in hosts:
            self.send_json({"error": "Loopback host required."}, 403)
            return False
        origin = self.headers.get("Origin")
        if origin and origin not in {"http://" + host for host in hosts}:
            self.send_json({"error": "Cross-origin requests are not enabled."}, 403)
            return False
        return True

    def chains(self):
        value = validate_chains(read_json(self.server.chains_path))
        manifest = self.source_manifest()
        for chain in value["chains"]:
            for source in chain["literature"]:
                identifier = source.get("id")
                entry = manifest.get(identifier)
                if isinstance(entry, dict) and entry.get("sha256") == source.get("sha256") and re.fullmatch(r"[A-Za-z0-9_-]{1,120}", identifier or ""):
                    page = source.get("pdf_page")
                    fragment = f"#page={page}" if isinstance(page, int) and not isinstance(page, bool) and page > 0 else ""
                    source["local_pdf_url"] = f"http://127.0.0.1:{self.server.server_port}/sources/{identifier}.pdf" + fragment
        return value

    def source_manifest(self):
        try:
            data = read_json(self.server.sources_path)
            entries = data.get("sources", {}) if isinstance(data, dict) else {}
            return entries if isinstance(entries, dict) else {}
        except (OSError, ValueError, TypeError):
            return {}

    def serve_source(self, path):
        match = re.fullmatch(r"/sources/([A-Za-z0-9_-]{1,120})\.pdf", path)
        entry = self.source_manifest().get(match[1]) if match else None
        if not isinstance(entry, dict):
            return self.send_json({"error": "Reviewed source not available."}, 404)
        try:
            target = Path(entry["path"])
            if target.suffix.lower() != ".pdf" or target.stat().st_size > 50 * 1024 * 1024:
                raise ValueError("Invalid source file")
            body = target.read_bytes()
            if not body.startswith(b"%PDF-") or hashlib.sha256(body).hexdigest() != entry["sha256"]:
                raise ValueError("Source edition hash mismatch")
        except (OSError, ValueError, TypeError, KeyError):
            return self.send_json({"error": "Exact reviewed source edition is unavailable."}, 503)
        return self.reply(body, content_type="application/pdf")

    def do_GET(self):
        if not self.valid_request():
            return
        try:
            parsed_url = urlsplit(self.path)
            path = unquote(parsed_url.path)
            if "\x00" in path:
                raise ValueError("Invalid URL")
        except ValueError:
            return self.send_json({"error": "Not found."}, 404)
        if path == "/api/status":
            return self.send_json({"version": "0.8.0", "status": "ready", "training_stopped": True,
                                   "semantic_retrieval": "external frozen local BGE; availability is reported per search",
                                   "physics_demo_url": self.server.physics_url,
                                   "evidence_file_present": self.server.chains_path.is_file(),
                                   "standards_file_present": self.server.standards_path.is_file()})
        if path == "/api/case-studies/gas-isolation":
            try:
                return self.send_json(gas_case_catalog(self.source_manifest(), self.server.server_port))
            except (OSError, ValueError, TypeError, KeyError):
                return self.send_json({"error": "The reviewed gas-isolation case is unavailable."}, 503)
        if path == "/api/fire-strategies":
            parameters = parse_qs(parsed_url.query, keep_blank_values=True)
            if set(parameters) - {"q"} or len(parameters.get("q", [])) > 1:
                return self.send_json({"error": "Supply one optional text query."}, 400)
            query = parameters.get("q", [""])[0]
            if len(query) > 2000:
                return self.send_json({"error": "Keep the strategy query within 2000 characters."}, 400)
            try:
                return self.send_json(self.server.strategies.catalog(self.source_manifest(), self.server.server_port, query))
            except (CatalogUnavailable, OSError, ValueError, TypeError, KeyError):
                return self.send_json({"error": "The reviewed strategy catalog is unavailable.", "status": "unavailable"}, 503)
        if path == "/api/habitat-atlas":
            if parsed_url.query:
                return self.send_json({"error": "The atlas exposes the supplied navigation catalog without inferred query parameters."}, 400)
            try:
                atlas = self.server.habitat_atlas.catalog(self.source_manifest(), self.server.server_port)
                try:
                    strategy_views = self.server.strategies.catalog(self.source_manifest(), self.server.server_port)
                except (OSError, ValueError, TypeError, KeyError):
                    strategy_views = None
                return self.send_json(attach_evidence_links(atlas, strategy_views))
            except (OSError, ValueError, TypeError, KeyError):
                return self.send_json({"error": "The reviewed habitat navigation is unavailable.", "status": "unavailable"}, 503)
        if path == "/api/liquid/catalog":
            try:
                return self.send_json(self.server.liquids().catalog())
            except (OSError, ValueError, TypeError, KeyError):
                return self.send_json({"error": "Offline liquid CSV is unavailable or invalid.", "fuels": []}, 503)
        if path == "/api/evidence-chains":
            try:
                return self.send_json(self.chains())
            except (OSError, ValueError, TypeError, KeyError):
                return self.send_json({"error": "Reviewed offline evidence chains are unavailable.", "chains": []}, 503)
        if path == "/api/iss-fire-context":
            try:
                value = read_json(self.server.standards_path)
                if not isinstance(value, dict) or value.get("schema_version") != "iss-fire-context-v1":
                    raise ValueError("Unexpected ISS source context")
                return self.send_json(value)
            except (OSError, ValueError, TypeError):
                return self.send_json({"error": "Reviewed ISS source context is unavailable."}, 503)
        if path.startswith("/api/"):
            return self.send_json({"error": "Unknown endpoint."}, 404)
        if path.startswith("/sources/"):
            return self.serve_source(path)
        try:
            entry = next((name for name in ("atlas.html", "liquid.html", "index.html") if (self.server.web_root / name).is_file()), "index.html")
            target = (self.server.web_root / (entry if path == "/" else path.lstrip("/"))).resolve()
            allowed = target.is_relative_to(self.server.web_root) and target.suffix.lower() in STATIC and target.is_file()
        except (OSError, ValueError):
            allowed = False
        if not allowed:
            return self.send_json({"error": "Asset not found."}, 404)
        try:
            body = target.read_bytes()
        except OSError:
            return self.send_json({"error": "Asset unavailable."}, 404)
        mime = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        if target.suffix.lower() in {".html", ".js", ".css", ".svg"}:
            mime += "; charset=utf-8"
        return self.reply(body, content_type=mime)

    do_HEAD = do_GET

    def do_POST(self):
        if not self.valid_request():
            return
        if self.path not in {"/api/search", "/api/liquid/compare", "/api/scenario/search"}:
            return self.send_json({"error": "Unknown read-only search endpoint."}, 404)
        try:
            if self.headers.get("Transfer-Encoding"):
                raise ValueError("Chunked requests are not supported")
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= 32768:
                raise ValueError("Supply a query body of 1-32768 bytes")
            payload = json.loads(self.rfile.read(size))
        except (ValueError, UnicodeError):
            return self.send_json({"error": "Invalid search request."}, 400)
        if self.path == "/api/scenario/search":
            try:
                return self.send_json(self.server.research.search(payload))
            except (ValueError, TypeError, KeyError):
                return self.send_json({"error": "Supply a natural-language research query of 1-2000 characters."}, 400)
        if self.path == "/api/liquid/compare":
            try:
                repository = self.server.liquids()
            except (OSError, ValueError, TypeError, KeyError):
                return self.send_json({"error": "Offline liquid CSV is unavailable or invalid."}, 503)
            try:
                result = repository.compare(payload)
                result["operating_checks"] = evaluate_operation(result, self.server.operation_profiles)
                for check in result["operating_checks"]["checks"]:
                    entry = self.source_manifest().get(check.get("source_id"))
                    if isinstance(entry, dict) and entry.get("sha256") == check.get("source_sha256"):
                        check["source_url"] = f"http://127.0.0.1:{self.server.server_port}/sources/{check['source_id']}.pdf#page={check['pdf_page']}"
                return self.send_json(result)
            except (ValueError, TypeError, KeyError):
                return self.send_json({"error": "Choose a listed fuel and experiment, with finite positive diameter and pressure and oxygen between 0 and 100%."}, 400)
        try:
            chains = self.chains()["chains"]
        except (OSError, ValueError, TypeError, KeyError):
            return self.send_json({"error": "Reviewed offline evidence chains are unavailable."}, 503)
        try:
            result = search(payload, chains, self.server.retriever)
            result["physics_demo_url"] = self.server.physics_url
            return self.send_json(result)
        except (ValueError, TypeError, KeyError):
            return self.send_json({"error": "Use a valid research query and documented filters."}, 400)


def make_server(port, web_root, chains_path, standards_path, retriever=None, physics_url="http://127.0.0.1:8793/physics.html", sources_path=None, liquid_csv=None, liquid_repository=None, research_corpus=None, operating_limits=None, strategy_catalog=None, strategy_preview=False, atlas_mapping=None, atlas_insights=None, atlas_qa=None):
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.web_root = Path(web_root).resolve()
    server.chains_path, server.standards_path = Path(chains_path), Path(standards_path)
    server.retriever = retriever if retriever is not None else FrozenRetriever()
    server.physics_url = physics_url
    server.sources_path = Path(sources_path) if sources_path else Path(chains_path).parent / "local_source_manifest.json"
    server.strategies = StrategyCatalog(strategy_catalog, review_mode=strategy_preview)
    server.habitat_atlas = HabitatAtlas(atlas_mapping, atlas_insights, atlas_qa)
    # One immutable offline snapshot per service lifetime; never execute model producers.
    # CSV and original model exports remain outside the public web root.
    if liquid_repository is None and liquid_csv is not None:
        try:
            liquid_repository = LiquidRepository(liquid_csv)
        except (OSError, ValueError, TypeError, KeyError):
            liquid_repository = None
    def liquids():
        if liquid_repository is None:
            raise ValueError("No valid offline liquid snapshot configured")
        return liquid_repository
    server.liquids = liquids
    server.research = ScenarioResearch(liquid_csv, research_corpus, server.retriever)
    try:
        server.operation_profiles = read_json(operating_limits).get("profiles", {}) if operating_limits else {}
    except (OSError, ValueError, TypeError, AttributeError):
        server.operation_profiles = {}
    return server


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8794)
    parser.add_argument("--web-root", type=Path, default=BASE / "web")
    parser.add_argument("--chains", type=Path, default=DATA / "reviewed_chains.json")
    parser.add_argument("--standards", type=Path, default=DATA / "iss_fire_context.json")
    parser.add_argument("--semantic-url", default="http://127.0.0.1:8784/api/search")
    parser.add_argument("--physics-url", default="http://127.0.0.1:8793/physics.html")
    parser.add_argument("--sources", type=Path, default=DATA / "local_source_manifest.json")
    parser.add_argument("--liquid-csv", type=Path, help="Read-only standardized CSV from the offline data package")
    parser.add_argument("--research-corpus", type=Path, default=WORKSPACE / "output/demo_20261113_1800/data/literature-data.json")
    parser.add_argument("--operating-limits", type=Path, default=DATA / "hardware_limits.json")
    parser.add_argument("--strategy-catalog", type=Path, default=WORKSPACE / "output/fire_strategy_priorities_20261115/strategy_catalog.json")
    parser.add_argument("--strategy-preview", action="store_true", help="Explicitly allow a pending-main-review catalog for local review only")
    parser.add_argument("--atlas-mapping", type=Path, default=WORKSPACE / "output/habitat_fire_atlas_20261115/habitat_fire_mapping.json")
    parser.add_argument("--atlas-insights", type=Path, default=WORKSPACE / "output/cross_dataset_insights_20261115/insight_map.json")
    parser.add_argument("--atlas-qa", type=Path, default=WORKSPACE / "output/habitat_fire_atlas_20261115/qa_contract.json")
    args = parser.parse_args()
    retriever = FrozenRetriever(args.semantic_url)
    with make_server(args.port, args.web_root, args.chains, args.standards, retriever, args.physics_url, args.sources, args.liquid_csv, research_corpus=args.research_corpus, operating_limits=args.operating_limits, strategy_catalog=args.strategy_catalog, strategy_preview=args.strategy_preview, atlas_mapping=args.atlas_mapping, atlas_insights=args.atlas_insights, atlas_qa=args.atlas_qa) as server:
        print(f"Flame Atlas v0.8.0: http://127.0.0.1:{server.server_port}/", flush=True)
        server.serve_forever()


if __name__ == "__main__":
    main()
