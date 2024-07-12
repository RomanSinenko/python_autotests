import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9b20d17c1a0c700ebbf7ed3474f85777'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

# Создание покемона

body_create = {
    "name": "generate",
    "photo_id": -1
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
message = response_create.json()['message']
pokemon_id = response_create.json()['id'] # Сохраняем id покемона в переменную
print(message)

# Смена имени покемона

body_rename = {
    "pokemon_id": pokemon_id,
    "name": "Name",
    "photo_id": 1
}
response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)
message = response_rename.json()['message']
print(message)

# Покемона в покебола

body_pokeball = {
    "pokemon_id": pokemon_id
}
response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)
message = response_pokeball.json()['message']
print(message)

# Список покемонов

response_pokemons = requests.get(url = f'{URL}/pokemons?status=1&trainer_id=5978', headers = HEADER)
print(response_pokemons.text)
message = response_pokemons.json()
print(message)