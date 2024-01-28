# tests/test_routes.py
import pytest
from flask import Flask
from simwire_plugin import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check_route(client):
    response = client.get('/health_check')
    assert response.status_code == 200

def test_example_route(client):
    response = client.get('/')  # Update with your actual route
    assert response.status_code == 200


