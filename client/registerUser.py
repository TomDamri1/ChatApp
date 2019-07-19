import requests
import sys


print("started2")
URL = "http://localhost:5000/api/users/register"
try:
    msg = sys.argv[1]
except:
    msg = 'defaultMSG fourth time'

PARAMS = {'name': 'testUser4','lastname':'testUser4', 'id':'testUser4','motherboard':'???','cpu':'???','password':'12345'}
for i in PARAMS.keys():
    PARAMS[i] = input(str(i)+ ":")

r = requests.post(url=URL, json=PARAMS)#sending data to the server
print(r.json())
pastebin_url = r.text

