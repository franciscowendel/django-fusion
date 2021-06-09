import requests


def test_status_code_home():

    url = 'http://127.0.0.1:8000/'

    resposta = requests.get(url=url)

    assert resposta.status_code == 200
