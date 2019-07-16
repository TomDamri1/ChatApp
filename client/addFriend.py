import requests
import sys


print("started2")
URL = "http://localhost:5000/api/users/addfriend/1"
try:
    msg = sys.argv[1]
except:
    msg = 'defaultMSG fourth time'

PARAMS = {'friend':'ghost'}

r = requests.post(url=URL, json=PARAMS)#sending data to the server
pastebin_url = r.text



