import requests
from requests.auth import HTTPBasicAuth


def test_basic_auth():
    response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('Durvesh03', 'duru09130063D'))
    r = requests.get('https://api.github.com/user', auth=('Durvesh03', 'duru09130063D'))
    print(r.text)
