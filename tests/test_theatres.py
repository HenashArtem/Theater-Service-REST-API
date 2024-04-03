import json
import pytest
import shutil
import os
from app import app


@pytest.fixture(scope='function', autouse=True)
def setup_function():
    shutil.copyfile('data/theatres.json', 'data/theatres_copy.json')
    yield
    shutil.copyfile('data/theatres_copy.json', 'data/theatres.json')
    os.remove('data/theatres_copy.json')


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_theatres(client):
    response = client.get('/theatres')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'theatres' in data
    assert len(data['theatres']) == 3


def test_get_theatre(client):
    response = client.get('/theatres/1')
    assert response.status_code == 200
    theatre = json.loads(response.data)
    assert theatre['id'] == 1


def test_get_nonexistent_theatre(client):
    response = client.get('/theatres/100')
    assert response.status_code == 404


def test_update_theatre(client):
    updated_theatre = {
        "name": "Updated Theatre",
        "location": "Updated Location",
        "capacity": 2000,
        "rating": 4.9
    }
    response = client.put('/theatres/1', json=updated_theatre)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == "Theatre updated successfully"


def test_delete_theatre(client):
    response = client.delete('/theatres/1')
    assert response.status_code == 200


def test_add_theatre(client):
    new_theatre = {
        "name": "New Theatre",
        "location": "New Location",
        "capacity": 3000,
        "rating": 4.7
    }
    response = client.post('/theatres', json=new_theatre)
    assert response.status_code == 201
    response = client.get('/theatres')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['theatres']) == 4


def test_delete_nonexistent_theatre(client):
    response = client.delete('/theatres/100')
    assert response.status_code == 404
