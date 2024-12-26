import requests

# Your code here

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
body = response.json()

print(body[1]["name"])