import requests

id1 = '87'
id2 = '99'
URL = "http://localhost:5000/api/chat/"+id2+"/"+id1

def get_messages(id1 , id2):
    URL = "http://localhost:5000/api/chat/" + id2 + "/" + id1


    ans = requests.get(url=URL)
    data = ans.json()
    l = []
    print(get_messages(id1, id2)['chat'])
    for i in get_messages(id1, id2)['chat']:
        if 'senderName' in i.keys():
            print(i['senderName'], ':', i['text'])
            l.append(i)

    return l


if __name__ == '__main__':
    """
    ans = requests.get(url = URL)
    data = ans.json()
    print("and the answer is :\n");
    print(data);
    """
    print(get_messages(id1,id2))






