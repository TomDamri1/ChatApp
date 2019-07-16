import requests

URL = "http://localhost:5000/api/users/1"


ans = requests.get(url = URL) 
data = ans.json() 
print("and the answer is :\n");
print(data)


