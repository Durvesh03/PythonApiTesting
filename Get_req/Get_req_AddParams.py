import requests
params = {'name':'durvesh','mob_num':'654654613'}
response = requests.get('https://httpbin.org/get', params=params)
print(response.text)
