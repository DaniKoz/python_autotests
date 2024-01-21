"""
Daniel test api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token':'c44ddc730b9ab1b792de192ac9316e48'}

body =  {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url=f'{URL}/pokemons',json=body,headers=HEADER,timeout=5)
print (f'status code:{response.status_code} . message:{response.json()["message"]}')

BODY={
    "pokemon_id": "27949",
    "name": "zubizub",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
}
response=requests.put(url=f'{URL}/pokemons',json=BODY,headers=HEADER,timeout=5)
print (f'status code:{response.status_code} . message:{response.json()["message"]}')
BODY2={
    "pokemon_id": "27949"
}
response=requests.post(url=f'{URL}/trainers/add_pokeball',json=BODY2,headers=HEADER,timeout=5)
print (f'status code:{response.status_code} . message:{response.json()["message"]}')