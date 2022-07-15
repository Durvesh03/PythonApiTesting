import requests
import json
import jsonpath


def test_add_multiple_student_data():
    api_url = 'https://reqres.in/api/users'

    file_path = "C:\\Users\\Durvesh\\PycharmProjects\\pythonProject\\tests\\request_json.json"

    with open(file_path, 'r') as j:
        contents = json.loads(j.read())

    response = requests.post(api_url, contents)
    print(response.status_code)
    assert response.status_code == 201