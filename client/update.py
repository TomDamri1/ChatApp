import requests
import sys


print("started2")
URL = "http://localhost:5000/api/users/update/user"


PARAMS = {'externalIP':'1234','internalIP':'45678','CPU':'intel','motherboard':'ASUS'}

r = requests.post(url=URL, json=PARAMS)#sending data to the server
print(r.json())
pastebin_url = r.text
