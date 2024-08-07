import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

data = response.json()

latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']
timestamp = data['timestamp']

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
print(f"Timestamp: {timestamp}")
