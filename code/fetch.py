import requests

raw = requests.get("http://127.0.0.1:5500/API/jSnip.json")
req = raw.json()

print("Status code:", raw.status_code)
print(req)