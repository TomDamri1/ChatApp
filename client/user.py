import requests
class User():
    URL = "http://LocalHosr:15888/api/chat"
    def __init__(self,id,name,lastName,ip,motherBoard,password,friendsList):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.ip = ip
        self.motherBoard = motherBoard
        self.password = password
        self.motherBoard = motherBoard
        self.friendsList = friendsList
    def sendMessage(self,msg,friend_id):
        PARAMS = {'ID': id, "otherID": friend_id, 'chat': msg}
        r = requests.post(url=User.URL, params=PARAMS)
        data = r.json()

    def getMessage(self,friend_id):
        pass
    def getFriends(self):
        pass
    def approveControl(self):
        pass
    def getControl(self,friend_id):
        pass
    def getmotherBoard(self,friend_id):
        pass
    def addFriend(self, friend_id):
        pass
    def deleteFriend(self, friend_id):
        pass