import json
import pytest
import shutil
import os
from app import app


@pytest.fixture(scope='function', autouse=True)
def setup_function():
    shutil.copyfile('data/performances.json', 'data/performances_copy.json')
    yield
    shutil.copyfile('data/performances_copy.json', 'data/performances.json')
    os.remove('data/performances_copy.json')


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_performances(client):
    response = client.get('/performances')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'performances' in data
    assert len(data['performances']) == 3


def test_get_performance(client):
    response = client.get('/performances/1')
    assert response.status_code == 200
    performance = json.loads(response.data)
    assert performance['id'] == 1


def test_get_nonexistent_performance(client):
    response = client.get('/performances/100')
    assert response.status_code == 404


def test_update_performance(client):
    updated_performance = {
        "theatre_id": 1,
        "play_id": 1,
        "date": "2024-03-25",
        "time": "19:00",
        "tickets_sold": 850,
        "ticket_price": 30.0
    }
    response = client.put('/performances/1', json=updated_performance)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == "Performance updated successfully"


def test_delete_performance(client):
    response = client.delete('/performances/1')
    assert response.status_code == 200


def test_add_performance(client):
    new_performance = {
        "theatre_id": 2,
        "play_id": 2,
        "date": "2024-04-20",
        "time": "20:00",
        "tickets_sold": 1000,
        "ticket_price": 35.0
    }
    response = client.post('/performances', json=new_performance)
    assert response.status_code == 201
    response = client.get('/performances')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['performances']) == 4


def test_delete_nonexistent_performance(client):
    response = client.delete('/performances/100')
    assert response.status_code == 404
