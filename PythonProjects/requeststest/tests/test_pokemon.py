import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token':'c44ddc730b9ab1b792de192ac9316e48'}

def test_get_trainers():
    """
    KTI-1. Get trainers
    """
    response=requests.get(url=f'{URL}/trainers',timeout=5)
    assert response.status_code ==200 ,'unexpected status code' 
    
def test_get_trainers_by_id():
    """
    KTI-1. Get trainers by id
    """
    response=requests.get(url=f'{URL}/trainers',params={'trainer_id':4655},timeout=5)
    assert response.json()['trainer_name'] == 'Pupsen', ' '