import requests

id1 = 'testUser'
id2 = 'testUser2'
URL = "http://localhost:5000/api/chat/"+id2+"/"+id1

def get_messages(id1 , id2):
    URL = "http://localhost:5000/api/chat/" + id2 + "/" + id1


    ans = requests.get(url=URL)
    data = ans.json()
    l = []
    print(data)

    for i in data['chat']:
        if 'senderName' in i.keys():
            msg = [i['senderName'] , i['text']]
            l.append(msg)

    return l



if __name__ == '__main__':
    """
    ans = requests.get(url = URL)
    data = ans.json()
    print("and the answer is :\n");
    print(data);
    """
    print(get_messages(id1,id2))






