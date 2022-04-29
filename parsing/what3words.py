import requests

# api_url = "http://api.openweathermap.org/data/2.5/weather"
api_url = "http://api.what3words.com/w3w"

params = {
    'key': 'H6W389MA',
    'string': 'prom.cape.pump',
    'corners': 'false'
}

res = requests.get(api_url, timeout=0.1, params=params)
print(res.status_code)
print(res.url)
print(res.encoding)
print(res.headers["Content-Type"])
print(res.json())  # returns json.loads(res.text) :)
print(res.text)
print(res.content)
print(res.cookies)
print(res.history)
