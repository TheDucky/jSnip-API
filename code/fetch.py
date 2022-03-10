import requests

raw = requests.get("https://theducky.github.io/jSnip-API/API/jSnip.json")
req = raw.json()

print("Status code:", raw.status_code)
print(req)