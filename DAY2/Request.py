import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

print(response.json())
