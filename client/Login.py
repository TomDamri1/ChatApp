import requests
import sys


print("started")
URL = "http://localhost:5000/api/users/login"

PARAMS = {'id': 'user','password':'223'}

r = requests.post(url=URL, json=PARAMS)#sending data to the server
print(r.json())
pastebin_url = r.text

