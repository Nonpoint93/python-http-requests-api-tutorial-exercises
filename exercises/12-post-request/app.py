import requests

# Your code here

headers = {'Content-Type': 'application/json'}
body_json = {}

response = requests.post("https://assets.breatheco.de/apis/fake/sample/post.php", data=body_json, headers=headers, verify=False)
print(response.text)