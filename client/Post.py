import requests
import sys


print("started2")
URL = "http://localhost:5000/api/chat"
try:
    msg = sys.argv[1]
except:
    msg = 'test msg3'
id1 = 'testUser'
id2 = 'testUser2'
PARAMS = {'ID': id1, "otherID": id2, 'chat': {"senderName": "testUser", "text": msg}}

r = requests.post(url=URL, json=PARAMS)#sending data to the server
pastebin_url = r.text
print("now get")

URL = "http://localhost:5000/api/chat/{}/{}".format(id1 , id2)


ans = requests.get(url=URL)
data = r.json() 
print("and the answer is :\n")
print(data)


