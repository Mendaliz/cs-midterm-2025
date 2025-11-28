import requests

response = requests.get("https://swapi.dev/api/people/")
data = response.json()
print(data)