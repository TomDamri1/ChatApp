import requests
import sys


print("started")
URL = "http://localhost:5000/api/users/removefriend/user"
try:
    msg = sys.argv[1]
except:
    msg = 'defaultMSG fourth time'

PARAMS = {'friend':'chuck norris'}

r = requests.delete(url=URL, json=PARAMS)#sending data to the server
print(r.json())


