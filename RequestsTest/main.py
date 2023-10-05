import requests

token = "a80078a1f6b9c3b59b36670af403dd7c"
host = 'https://api.pokemonbattle.me:9104'

response = requests.post(f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"}, 
headers = {"Content-Type" : "application/json",
           "trainer_token" : token})
print(response.text)

response = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "4659",
    "name": "Good Name",
    "photo": "https://dolnikov.ru/pokemons/albums/042.png"
},
headers = {"Content-Type" : "application/json",
           "trainer_token" : token})
print(response.text)

response = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "4660"
},
headers = {"Content-Type" : "application/json",
           "trainer_token" : token})
print(response.text)