"""Restore the hash-pinned runtime data archive inside the app directory."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent


def prepare(root=ROOT):
    manifest = json.loads((root / 'data/assets_manifest.json').read_text(encoding='utf-8'))
    archive = root / 'data/runtime.zip'
    with archive.open('rb') as stream:
        actual = hashlib.file_digest(stream, 'sha256').hexdigest()
    if actual != manifest['runtime_zip_sha256']:
        raise ValueError('Runtime data archive hash mismatch')
    with zipfile.ZipFile(archive) as source:
        for name in source.namelist():
            if not name.startswith('data/') or not (root / name).resolve().is_relative_to((root / 'data').resolve()):
                raise ValueError('Unsafe data archive path')
        source.extractall(root)
    print('Runtime data restored; no model fitting or API call performed.')


if __name__ == '__main__': prepare()
