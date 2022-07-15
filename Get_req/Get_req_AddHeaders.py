import requests
headerdata = {'t1':'first header', 't2':'second_header'}
response = requests.get('https://httpbin.org/get', headers=headerdata)
print(response.text)
