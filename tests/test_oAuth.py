import requests
import json
import jsonpath


def test_oauth():
    # First mention url which will generate token
    token_url = "http://thetestingworldapi.com/Token"
    # we need to pass 3 values username, password, grant type as a dictionary
    # Grant type  - how my server is going to give access in this case grant_type is password
    data = {'grant_type': 'password', 'username': 'duru', 'password': '123@abcde'}

    # now create a POST request on token url with data
    response = requests.post(token_url, data)
    print(response.text)

    # Now fetch token value from response (in response.text, token value is in 'access_token' field)
    token_val = jsonpath.jsonpath(response.json(), 'access_token')

    # now use this token value to create one more dictionary
    # mention 'Bearer ' before token value
    auth = {'Authorization': 'Bearer ' + token_val[0]}

    api_url = 'http://thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(api_url, headers=auth)
    print(response.text)
