import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import make_body


def test_root_body_contains_expected_fields():
    os.environ['PORT'] = '8000'
    body = make_body('/')
    assert body['ok'] is True
    assert body['message'] == 'hello from docker-learning'
    assert body['port'] == 8000
    assert body['path'] == '/'


def test_healthz_body_reports_healthy():
    os.environ['PORT'] = '8000'
    body = make_body('/healthz')
    assert body['ok'] is True
    assert body['status'] == 'healthy'
    assert body['port'] == 8000
    assert body['path'] == '/healthz'
