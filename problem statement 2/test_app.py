import pytest
from flask import Flask

from server import app


# Test that the index route returns a message
def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.get_json() == {'message': 'app has been setup'}

# Test that the getip route returns an IP address
def test_getip():
    client = app.test_client()
    response = client.get('/getip')
    assert response.status_code == 200
    assert len(response.get_data(as_text=True)) > 0

# Test that the classifier/metrics route returns a dictionary with model and metrics keys
def test_classifier_metrics():
    client = app.test_client()
    response = client.get('/classifier/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert 'model' in data
    assert 'metrics' in data

# Test that the cnn/metrics route returns a dictionary with model and metrics keys
def test_cnn_metrics():
    client = app.test_client()
    response = client.get('/cnn/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert 'model' in data
    assert 'metrics' in data
