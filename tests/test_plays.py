import json
import pytest
import shutil
import os
from app import app


@pytest.fixture(scope='function', autouse=True)
def setup_function():
    shutil.copyfile('data/plays.json', 'data/plays_copy.json')
    yield
    shutil.copyfile('data/plays_copy.json', 'data/plays.json')
    os.remove('data/plays_copy.json')


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_plays(client):
    response = client.get('/plays')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'plays' in data
    assert len(data['plays']) == 3


def test_get_play(client):
    response = client.get('/plays/1')
    assert response.status_code == 200
    play = json.loads(response.data)
    assert play['title'] == 'Romeo and Juliet'


def test_get_nonexistent_play(client):
    response = client.get('/plays/100')
    assert response.status_code == 404


def test_update_play(client):
    updated_play = {
        "title": "Macbeth",
        "author": "William Shakespeare",
        "genre": "Tragedy",
        "duration": "3 hours"
    }
    response = client.put('/plays/1', json=updated_play)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == "Play updated successfully"


def test_delete_play(client):
    response = client.delete('/plays/1')
    assert response.status_code == 200


def test_add_play(client):
    new_play = {
        "title": "A Midsummer Night's Dream",
        "author": "William Shakespeare",
        "genre": "Comedy",
        "duration": "2.5 hours"
    }
    response = client.post('/plays', json=new_play)
    assert response.status_code == 201
    response = client.get('/plays')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['plays']) == 4


def test_delete_nonexistent_play(client):
    response = client.delete('/plays/100')
    assert response.status_code == 404
