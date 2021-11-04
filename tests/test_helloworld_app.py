from app import app, index
from chalice.test import Client
import json


def test_api_root():
    with Client(app) as client:
        result = client.http.get('/')
        assert result.status_code == 200
        assert result.json_body == {'hello': 'world'}

def test_health_route():
    with Client(app) as client:
        result = client.http.get('/health')
        assert result.status_code == 200
        assert result.json_body == {'Status': 'OK'}

def test_user_route():
    with Client(app) as client:
        payload = {"Name": "sharabh", "Age": 39.0,"Sex": "Male"}
        headers = {'Content-Type': 'application/json'}
        result = client.http.post('/user', body = json.dumps(payload, sort_keys=True), headers=headers)
        assert result.status_code == 200
        assert result.json_body == payload



