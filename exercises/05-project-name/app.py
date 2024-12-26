import requests

# Your code here

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")

body = response.json()

print(body['name'])