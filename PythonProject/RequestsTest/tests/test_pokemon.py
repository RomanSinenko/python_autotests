import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9b20d17c1a0c700ebbf7ed3474f85777'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '5978'

# Информация о тренере

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Roman'


