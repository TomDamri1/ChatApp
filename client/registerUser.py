import requests
import sys
sys.path.append("../..")
import URL

print("*******************************REGISTER*******************************")
#print("started2")
my_url = URL.registerURL
try:
    msg = sys.argv[1]
except:
    msg = 'defaultMSG fourth time'

PARAMS = {'name': 'testUser4','lastname':'testUser4', 'id':'testUser4','password':'12345'}
for i in PARAMS.keys():
    PARAMS[i] = input(str(i)+ ":")

PARAMS['motherboard'] = 'unknown'
PARAMS['cpu'] = 'unknown'

try:
    r = requests.post(url=my_url, json=PARAMS)#sending data to the server
    print(r.json())
    pastebin_url = r.text
except:
    print("Error - check your internet connection.\nif the server is local, check configuration and that the server is running.\nif all above are ok, check the server at: "+URL.URL)

if __name__ == '__main__':
    pass