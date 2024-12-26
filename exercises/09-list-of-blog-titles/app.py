import requests

def get_titles():
    # Your code here
    titles = [] # Empty list
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    body = response.json()
    for post in body['posts']:
        titles.append(post['title'])

    return titles


print(get_titles())