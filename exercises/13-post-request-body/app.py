import requests

headers = {'Content-Type': 'application/json'}
body_json = {
    "id": 2323,
    "title": "Very big project"
}

response = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php", json=body_json, headers=headers)
print(response.text)