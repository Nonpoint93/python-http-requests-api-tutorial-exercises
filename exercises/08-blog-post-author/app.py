import requests

# Your code here
response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

body = response.json()

print(body['posts'][0]['author']['name'])