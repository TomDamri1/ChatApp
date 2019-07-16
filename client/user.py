import requests
import socketio
import subprocess
import os
import socket
from time import sleep
import queue
from collections import deque
import sys
from threading import Thread, Condition
import URL
HEADER_LENGTH = 10


"""
An singleton class represent the connect user
"""


class User:
    # hold singleton instance
    __instance = None
    # queue that store all the receive messages
    q = deque()
    # for waiting if q is empty, notify when get new message
    cv = Condition()
    sio = socketio.Client()
    sio.connect(URL.URL)
    # factory method limit the instance of user to one.
    @staticmethod
    def get_instance(id, password, sudo_password):
        """ Static access method. """
        if User.__instance is None:
            User(id, password, sudo_password)
        return User.__instance

    """Decorator to register an event handler.
    """
    @staticmethod
    @sio.event
    def message(data):
        User.cv.acquire()
        print('new message received!')
        User.q.append(data)
        User.cv.notify()
        User.cv.release()

    def __init__(self, id, password, sudo_password):
        if User.__instance is not None:
            raise Exception("This class is a singleton!")
        self.my_queue = deque()
        self.ssh_requests_command_queue = deque()
        # for waiting if ssh_requests_command_queue is empty, notify when get new command
        self.command_request = Condition()
        self.ssh_results_command_queue = deque()
        self.id = id
        self.password = password
        self.sudo_password = sudo_password
        self.approve_control_requests = set()
        self.approved_control = set()
        self.set_external_ip()
        self.set_internal_ip()
        self.set_motherboard()
        self.set_cpu()
        # open socket with client
        '''
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySocket.connect(('127.0.0.1',8823))
        '''
        self.connect()
        User.__instance = self

    def __str__(self):
        return 'name:' + self.name + " last name:" + self.last_name

    def connect(self):
        # pull the friend list from the server
        # pull  my derails from the server
        # create new thread that listen to server for changes
        user_data_from_server = requests.get(url=(URL.usersURL + "/" + self.id))
        data = user_data_from_server.json()
        self.name = data['name']
        self.last_name = data['lastname']
        self.friends_list = data['friends']
        thread1 = Thread(target=self.listen_to_server)
        thread1.start()
        thread2 = Thread(target=self.execute_command_from_ssh_requests_command_queue)
        thread2.start()

    def execute_command_from_ssh_requests_command_queue(self):
        while True:
            # queue not empty - got new message
            if len(self.ssh_requests_command_queue) != 0:
                data = self.ssh_requests_command_queue.pop()
                result = self.execute_command(data['chat']['text'][16:])
                if result != '':
                    self.ssh_results_command_queue.append(data['ID'] + ' ' + result)
            else:
                self.command_request.acquire()
                self.command_request.wait()
                self.command_request.release()

    def listen_to_server(self):
        while True:
            # queue not empty - got new message
            if len(User.q) != 0:
                data = User.q.pop()
                #check if the message designated to me
                if data['otherID'] == self.id:
                    #check the kind of the message - ordinary or control
                    if str(data['chat']['test']) == 'can i control yours computer?@#$<<':
                        self.approve_control_requests.add(data['otherID'])
                    elif str(data['chat']['test']).startswith('ssh control@#$<<') and data['otherID'] in self.approved_control:
                        self.ssh_requests_command_queue.append(data)
                        self.command_request.acquire()
                        self.command_request.notify()
                        self.command_request.release()
                    else:
                        self.my_queue.append(data['chat'])
            # queue empty thread go to sleep, avoid busy waiting
            else:
                User.cv.acquire()
                User.cv.wait()
                User.cv.release()
        """
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
            self.q.put(msg)
        """

    def send_message(self, friend_id, msg):
        if friend_id in self.friends_list:
            """
            username = self.id.encode('utf-8')
            username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
            self.mySocket.send(username_header + username)

            message = msg.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            self.mySocket.send(message_header + message)
            """
            params = {'ID': self.id, "otherID": friend_id, 'chat': [{"senderName": self.name, "text": msg}, ]}
            r = requests.post(url=URL.postURL, json=params)
            return_msg = r.text
            print(return_msg)
        else:
            print("ERROR can't to send a message to friend that not in your's friendsList")

    """
    def getMessage(self, friend_id):
        # Params : friend ID - the id of the friend that the message will be send to.
        # return the content of the message
        curURL = URL.getURL + "{}/{}".format(self.id, friend_id)
        r = requests.get(url=curURL)
        data = r.json()
        text = data['chat'][0]["text"]
        return text
    """

    def get_friends(self):
        return self.friends_list

    def approve_control(self, friend_id, decision):
        '''
        :param friend_id: the id of the friend that ask for control
        :param decision: the user decision if approve to the ask (True or False)
        :return:
        '''
        if decision:
            self.approved_control.add(friend_id)
            self.approve_control_requests.discard(friend_id)
        else:
            self.approve_control_requests.discard(friend_id)

    def remove_control(self, friend_id):
        '''
        :param friend_id: he id of the friend that you want to remove from approved_control set
        :return: string
        '''
        if friend_id in self.approved_control:
            self.approved_control.discard(friend_id)
            return friend_id +"removed from approved_control set"
        else:
            return friend_id +"didn\'t add control on your computer"

    def ask_for_control(self, friend_id):
        params = {'ID': self.id, "otherID": friend_id, 'chat': [{"senderName": self.name, "text": 'can i control you\'rs computer?@#$<<'}, ]}
        r = requests.post(url=URL.postURL, json=params)
        print(r)

    def find_motherboard(self):
        #return the name of the motherboard by using bash as administrator
        command = 'dmidecode -t baseboard'
        motherboard_manufacturer = subprocess.check_output('echo %s|sudo -S %s | grep Manufacturer' % (self.password, command), shell=True)
        prod_name = '\'Product Name\''
        motherboard_product_name = subprocess.check_output('echo %s|sudo -S %s | grep %s' % (self.password, command, prod_name), shell=True)
        return motherboard_manufacturer.decode("utf-8") + motherboard_product_name.decode("utf-8")

    def find_cpu(self):
        #return the name of the CPU by using bash as administrator
        command = 'dmidecode -t processor'
        cpu_version = subprocess.check_output('echo %s|sudo -S %s | grep Version' % (self.password, command), shell=True)
        return cpu_version.decode("utf-8")

    def find_external_ip(self):
        #return the name of the CPU by using bash as administrator
        command = 'dig +short myip.opendns.com @resolver1.opendns.com'
        external_ip = subprocess.check_output('echo %s|sudo -S %s' % (self.password, command), shell=True)
        return external_ip.decode("utf-8")

    def find_internal_ip(self):
        #return the name of the CPU by using bash as administrator
        command = 'hostname -I'
        internal_ip = subprocess.check_output('echo %s|sudo -S %s' % (self.password, command), shell=True)
        return internal_ip.decode("utf-8")

    def execute_command(self, command):
        #return the name of the motherboard by using bash as administrator
        new_command = command
        for i in range(len(command)):
            if command[i] == '|':
                new_command = new_command[:i] + " 2>/dev/null " + new_command[i:]
        new_command += " 2>/dev/null "
        result = subprocess.check_output('echo %s|sudo -S %s' % (self.password, new_command), shell=True)
        return result.decode("utf-8")

    def take_all_screenshot(self):
        '''
        :return: screenshot of all screen by using bash as administrator
        '''
        command = "import -window root -resize 1024x800 -delay 500 screenshot.png"
        os.system('%s' % (command))

    def take_screenshot(self):
        '''
        :return: screenshot of grab area by using bash as administrator
        '''
        command = "import screenshot.png"
        os.system('%s' % (command))

    def set_motherboard(self):
        self.motherBoard = self.findMotherBoard()
        #need to write to data base

    def set_cpu(self):
        self.cpu = self.findCpu()
        # need to write to data base

    def set_external_ip(self):
        self.ExternalIp = self.find_external_ip()
        # need to write to data base

    def set_internal_ip(self):
        self.InternalIp = self.find_internal_ip()
        # need to write to data base

    def get_my_motherboard(self):
        return self.motherBoard

    def get_friend_motherboard(self, friend_id):
        # return the friend motherboard
        friend_data_from_server = requests.get(url=(URL.usersURL + "/" + friend_id))
        data = friend_data_from_server.json()
        friend_motherboard = data['motherboard']
        return friend_motherboard

    def get_friend_cpu(self, friend_id):
        # return the friend cpu
        friend_data_from_server = requests.get(url=(URL.usersURL + "/" + friend_id))
        data = friend_data_from_server.json()
        friend_cpu = data['cpu']
        return friend_cpu

    def add_friend(self, friend_id):
        self.friends_list.append(friend_id)
        # add the friend to the friends data base
        add_friend_url = URL.addfriendURL + self.id
        PARAMS = {'friend': friend_id}
        r = requests.post(url=add_friend_url, json=PARAMS)  # sending data to the server
        # add result
        return r.text

    def delete_friend(self, friend_id):
        # Param : friend_id that need to be deleted from the friend list
        try:
            self.friends_list.remove(friend_id)
            # need to delete the friend from the friends data base
        except ValueError as e:
            print(e)

    def send_file(self):
        pass

    def disconnect(self):
        pass


def connect(user_id , password , sudo_password):
    """
    send to alex
    1. check if exist
    2. pull the user data
    3. init User , and return it
    :param user_id:
    :param password:
    :return:
    """
    def sudo_password_check(sudo_password):
        command = 'dmidecode -t baseboard'
        try:
            result = subprocess.check_output(
            'echo %s|sudo -S %s 2>/dev/null' % (sudo_password, command), shell=True)
            return True

        except:
            return False

    def user_password_check():
        """
        check if user exist
        :return: False if doesn't exist or True if exist
        """
        PARAMS = {'id': user_id, 'password': password}
        r = requests.post(url=URL.loginURL, json=PARAMS)  # sending data to the server
        if r.json()['Login'] == 'Login Failed Wrong password':
            return False
        return True

    if not user_password_check():
        return 'Wrong username or password'
    elif not sudo_password_check(sudo_password):
        return 'wrong sudo password'

    usr = User(user_id, password, sudo_password)
    return usr


result = connect('mtd123', '123', '1313')
while isinstance(result, str):
    print(result)

#result.sendMessage('user', 'hello my name is matan')

'''
#us1.connect()
us1.sendMessage("user 1 send a message", '123')

print(us1.findMotherBoard())
print(us1.findCpu())
print("choose field to screen shot")
us1.takeScreenShot()
print(us1.executeCommand("ls -l"))
#us1.sendMessage("hello my name is matan third try", '123')
#print(us1.findMotherBoard('123'))
ans = requests.get(url="http://localhost:5000/api/users/1")
data = ans.json()
print(data)
'''