import requests
import sys


print("started2")
URL = "http://localhost:5000/api/users/register"
try:
    msg = sys.argv[1]
except:
    msg = 'defaultMSG fourth time'

PARAMS = {'name': 'tomer','lastname':'leon', 'id':'1','motherboard':'intel','cpu':'i5','password':'22'}

r = requests.post(url=URL, json=PARAMS)#sending data to the server
pastebin_url = r.text
print("now get")

URL = "http://localhost:5000/api/chat/99/87"


ans = requests.get(url=URL)
data = r.json()
print("and the answer is :\n")
print(data)


