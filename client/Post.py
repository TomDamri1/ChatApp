import requests


print("started2");
URL = "http://localhost:5000/api/chat"

PARAMS = {'ID':"99","otherID":"87",'chat':[{"senderName":"tom","text":"helloworld"}]}

r =requests.post(url = URL, json = PARAMS)#sending data to the server
pastebin_url = r.text
print("now get");


URL = "http://localhost:5000/api/chat/99/87"


ans = requests.get(url = URL) 
data = r.json() 
print("and the answer is :\n");
print(data);


