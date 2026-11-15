"""Relocatable, loopback launcher copied to the root of the offline delivery."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True


def contained(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('Package path escapes its root')
    return path


def verify_files(root):
    manifest = json.loads((root / 'MANIFEST.json').read_text(encoding='utf-8'))
    for entry in manifest['files']:
        path = contained(root, entry['path'])
        with path.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        if path.stat().st_size != entry['bytes'] or digest != entry['sha256']:
            raise ValueError('Package integrity mismatch: ' + entry['path'])
    return len(manifest['files'])


def resolved_config(root, semantic_url=None):
    config = json.loads((root / 'backend/config.relative.json').read_text(encoding='utf-8'))
    for key in ['baseline_server', 'web_root', 'bridge_catalog', 'atlas_snapshot', 'chart_presentation', 'narratives']:
        config[key] = str(contained(root, config[key]))
    if config.get('dataset_markdown_index'):
        config['dataset_markdown_index'] = str(contained(root, config['dataset_markdown_index']))
    for key, value in config['baseline_arguments'].items():
        if key not in {'physics_url', 'strategy_preview'} and isinstance(value, str):
            config['baseline_arguments'][key] = str(contained(root, value))
    if semantic_url:
        config['semantic_url'] = semantic_url
    return config


def configure_ai(mode):
    if mode == 'openai':
        os.environ['NASA_AI_PROVIDER'] = 'openai'
        os.environ.setdefault('NASA_AI_MODEL', 'gpt-6.1-sol')
        os.environ.setdefault('NASA_OPENAI_REASONING_EFFORT', 'max')
        os.environ.setdefault('NASA_OPENAI_SERVICE_TIER', 'fast')
        # A missing key must not silently run Qwen or pretend an offline
        # synthesis is a ChatGPT response.
        if not (os.environ.get('OPENAI_API_KEY') or os.environ.get('NASA_AI_API_KEY')):
            raise ValueError('Set OPENAI_API_KEY in this server environment. Never paste it into a URL or commit it. For package verification only, use --ai-mode off.')
    else:
        for key in ['NASA_AI_PROVIDER', 'NASA_AI_BASE_URL', 'OPENAI_BASE_URL', 'NASA_AI_MODEL',
                    'OPENAI_MODEL', 'NASA_AI_API_KEY', 'OPENAI_API_KEY']:
            os.environ.pop(key, None)
        os.environ['NASA_AI_PROVIDER'] = 'local'


def load_workspace(root):
    workspace = root / 'backend/workspace'
    sys.path.insert(0, str(workspace))
    spec = importlib.util.spec_from_file_location('_flame_delivery_workspace', workspace / 'server.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(argv=None):
    parser = argparse.ArgumentParser(description='Run the packaged Flame Atlas. Local verification is not public hosting.')
    parser.add_argument('--port', type=int, default=8794)
    parser.add_argument('--ai-mode', choices=['openai', 'local', 'off'], default='openai')
    parser.add_argument('--semantic-url', help='Optional existing frozen local search endpoint; no service is started')
    parser.add_argument('--check', action='store_true', help='Verify files and load data on an ephemeral port, then exit')
    args = parser.parse_args(argv)
    count = verify_files(ROOT)
    configure_ai(args.ai_mode)
    config = resolved_config(ROOT, args.semantic_url)
    workspace = load_workspace(ROOT)
    # The absolute launch configuration exists only during this process and
    # contains no key. The archived configuration contains package-relative paths.
    with tempfile.TemporaryDirectory(prefix='flame-atlas-runtime-') as temp:
        config_path = Path(temp) / 'launch_config.json'
        config_path.write_text(json.dumps(config), encoding='utf-8')
        with workspace.make_integrated_server(config_path, 0 if args.check else args.port) as server:
            if args.ai_mode == 'off':
                server.workspace_ai = None
            if args.check:
                print(json.dumps({'status': 'PASS', 'files_verified': count,
                    'documents': len(server.workspace_bridge.documents),
                    'charts': len(server.workspace_bridge.charts),
                    'ai_mode': args.ai_mode, 'paid_api_called': False}))
                return
            print('Flame Atlas: http://127.0.0.1:' + str(server.server_port) + '/', flush=True)
            print('AI mode: ' + args.ai_mode + '. No fitting or training is started.', flush=True)
            server.serve_forever()


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, ImportError) as error:
        print('Cannot start Flame Atlas: ' + str(error), file=sys.stderr)
        raise SystemExit(2)
