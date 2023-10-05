import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'

def test_ctatus_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 1627})
    assert response.json()["trainer_name"] == 'Arseny'

