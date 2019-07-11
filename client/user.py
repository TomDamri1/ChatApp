import requests
import os
import subprocess
import time
class User:
    postURL = "http://localhost:5000/api/chat"
    getURL= "http://localhost:5000/api/chat/"

    def __init__(self, id, name, lastName, ip, motherBoard, password, friendsList):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.ip = ip
        self.motherBoard = motherBoard
        self.password = password
        self.motherBoard = motherBoard
        self.friendsList = friendsList

    def sendMessage(self, msg, friend_id):
        if friend_id in self.friendsList:
            PARAMS = {'ID': self.id, "otherID": friend_id, 'chat': [{"senderName": self.name, "text": msg}, ]}
            r = requests.post(url=User.postURL, json=PARAMS)
            pastebin_url = r.text
            print(pastebin_url)
        else:
            print("ERROR can't to send a message to friend that not in your's friendsList")

    def getMessage(self, friend_id):
        # Params : friend ID - the id of the friend that the message will be send to.
        # return the content of the message
        curURL = User.getURL + "{}/{}".format(self.id, friend_id)
        r = requests.get(url=curURL)
        data = r.json()
        text = data['chat'][0]["text"]
        return text

    def getFriends(self):
        return self.friendsList

    def approveControl(self):
        pass

    def getControl(self, friend_id):
        pass

    def findMotherBoard(self):
        #return the name of the motherboard by using bash
        sudoPassword = '1212'
        command = 'dmidecode -t baseboard'
        motherBoardManufacturer = subprocess.check_output('%s|sudo -S %s | grep Manufacturer &>/dev/null' % (sudoPassword, command), shell=True)
        prodNmane = '\'Product Name\''
        motherBoardProductName = subprocess.check_output('%s|sudo -S %s | grep %s &>/dev/null' % (sudoPassword, command, prodNmane), shell=True)
        return motherBoardManufacturer.decode("utf-8") + motherBoardProductName.decode("utf-8")

    def setmotherBoard(self):
        self.motherBoard = self.findMotherBoard()

    def getmotherBoard(self, friend_id):
        return self.motherBoard

    def addFriend(self, friend_id):
        self.friendsList.append(friend_id)
        # need to add the friend to the friends data base

    def deleteFriend(self, friend_id):
        # Param : friend_id that need to be deleted from the friend list
        try:
            self.friendsList.remove(friend_id)
            # need to delete the friend from the friends data base
        except ValueError as e:
            print(e)

    def connect(self):
        # pull the friend list and my derails from the server
        pass


us1 = User('205509', 'matan', 'davidian', '0.0.0.0', 'intel mother Board', '123123', ['2312', '12332', '123'])
print(us1.findMotherBoard())
#us1.sendMessage("hello my name is matan third try", '123')
#print(us1.findMotherBoard('123'))

