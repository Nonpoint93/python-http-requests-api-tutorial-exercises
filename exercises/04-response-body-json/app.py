import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")

body = response.json()

print(f"Current time: {body['hours']} hrs {body['minutes']} min and {body['seconds']} sec")