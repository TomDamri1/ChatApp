import requests

URL = "http://localhost:5000/api/chat/99/87"


ans = requests.get(url = URL) 
data = ans.json() 
print("and the answer is :\n");
print(data);


