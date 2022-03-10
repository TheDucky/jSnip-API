# i use this python file to get json data to check if i have done things right

import requests

req = requests.get("https://theducky.github.io/jSnip-API/API/jSnip.json")

data = req.json()

print(data["while_loop"][0]["snip"])

print("----------------------------")

print(data["while_loop"][0]["example"])