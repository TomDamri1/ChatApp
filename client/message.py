class Message():
    messageId = 0
    def __init__(self,content,senderId,reciverId,date,conversation):
        self.content = content
        self.senderId = senderId
        self.reciverId = reciverId
        self.date = date
        self.conversation = conversation
        self.messageId = Message.messageId
        Message.messageId += 1
    def sendMessage(self,msg,friend_id):
        pass
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