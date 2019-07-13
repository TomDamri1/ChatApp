import requests
import subprocess
import os
import socket
from time import sleep
import sys
from threading import Thread
HEADER_LENGTH = 10


class User:
    postURL = "http://localhost:5000/api/chat"
    getURL = "http://localhost:5000/api/chat/"

    def __init__(self, id, name, lastName, IP, motherBoard, password, friendsList):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.IP = IP
        self.motherBoard = motherBoard
        self.password = password
        self.motherBoard = motherBoard
        self.friendsList = friendsList
        self.PORT = 8821
        # open socket with client
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySocket.connect((self.IP, self.PORT))


    def connect(self):
        # pull the friend list from the server
        # pull  my derails from the server
        # create new thread that listen to server for changes
        thread = Thread(target=self.listenToServer)
        thread.start()

    def listenToServer(self):
        while(True):
            # Receive our "header" containing username length, it's size is defined and constant
            msg_header = self.mySocket.recv(HEADER_LENGTH)
            # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            if not len(msg_header):
                print('Connection closed by the server')
                sys.exit()
            # Convert header to int value
            msg_length = int(msg_header.decode('utf-8').strip())
            print(f"msg size is: {msg_length}")
            msg = self.mySocket.recv(msg_length).decode("utf-8")
            print(msg)


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
        #return the name of the motherboard by using bash as administrator
        command = 'dmidecode -t baseboard'
        motherBoardManufacturer = subprocess.check_output('echo %s|sudo -S %s | grep Manufacturer' % (self.password, command), shell=True)
        prodNmane = '\'Product Name\''
        motherBoardProductName = subprocess.check_output('echo %s|sudo -S %s | grep %s' % (self.password, command, prodNmane), shell=True)
        return motherBoardManufacturer.decode("utf-8") + motherBoardProductName.decode("utf-8")

    def findCpu(self):
        #return the name of the CPU by using bash as administrator
        command = 'dmidecode -t processor'
        cpuVersion = subprocess.check_output('echo %s|sudo -S %s | grep Version' % (self.password, command), shell=True)
        return cpuVersion.decode("utf-8")

    def executeCommand(self, command):
        #return the name of the motherboard by using bash as administrator
        newCommand = command
        for i in range(len(command)):
            if command[i] == '|':
                newCommand = newCommand[:i] + " 2>/dev/null " + newCommand[i:]
        newCommand += " 2>/dev/null "
        result = subprocess.check_output('echo %s|sudo -S %s' % (self.password, newCommand), shell=True)
        return result.decode("utf-8")

    def takeAllScreenShot(self):
        #return the name of the motherboard by using bash as administrator
        command = "import -window root -resize 1024x800 -delay 500 screenshot.png"
        os.system('%s' % (command))

    def takeScreenShot(self):
        #return the name of the motherboard by using bash as administrator
        command = "import screenshot.png"
        os.system('%s' % (command))

    def setMotherBoard(self):
        self.motherBoard = self.findMotherBoard()
        #need to write to data base

    def getMyMotherBoard(self):
        return self.motherBoard

    def getMyMotherBoard(self, friend_id):
        # return the friend motherboard
        pass
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

    def sendFile(self):
        pass

password = str(input("Enter your password pls:"))
us1 = User('205509', 'matan', 'davidian', '127.0.0.1', 'intel mother Board', password, ['2312', '12332', '123'])
us1.connect()
'''
print(us1.findMotherBoard())
print(us1.findCpu())
print("choose field to screen shot")
us1.takeScreenShot()
print(us1.executeCommand("ls -l"))
#us1.sendMessage("hello my name is matan third try", '123')
#print(us1.findMotherBoard('123'))
'''