import requests
import json
import jsonpath
base_url = 'https://reqres.in/'
rel_url = 'api/users?page=2'
response = requests.get(base_url + rel_url)
json_response = json.loads(response.text)

pages = jsonpath.jsonpath(json_response,'per_page')
print(pages[0])

name_user2 = jsonpath.jsonpath(json_response,'data[1].first_name')
print(name_user2[0])