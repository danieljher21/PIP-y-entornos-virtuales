import requests

def get_categories():
    url = 'https://api.escuelajs.co/api/v1/categories'
    r = requests.get(url)
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    print(type(categories))
    for category in categories:
        print(category['name'])