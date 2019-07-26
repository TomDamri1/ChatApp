import requests
import socketio
import subprocess
import os
from collections import deque
from threading import Thread, Condition, Lock
import URL
#import time
#import socket
#HEADER_LENGTH = 10


"""
An singleton class represent the connect user
"""


class User:
    can_exit_safe = False
    # hold singleton instance
    __instance = None
    # queue that store all the receive messages
    q = deque()
    # for waiting if q is empty, notify when get new message

    cv = Condition()
    sio = socketio.Client()
    sio.connect(URL.URL)

    @staticmethod
    def get_instance():
        """ Static access method. """
        return User.__instance

    """Decorator to register an event handler.
    """
    @staticmethod
    @sio.event
    def message(data):
        User.cv.acquire()
        #print('new message received!')
        User.q.append(data)
        User.cv.notify()
        User.cv.release()

    def __init__(self, id, password, sudo_password):
        if User.__instance is not None:
            raise Exception("This class is a singleton!")
        self.id = id
        self.password = password
        self.sudo_password = sudo_password
        self.show_ssh_res = True

        # queue of simple msgs for chat windows
        self.my_queue = deque()
        lock_for_my_queue = Lock()
        self.my_queue_waiter = Condition(lock_for_my_queue)

        # queue of sender name for main windows
        self.sender_queue = deque()

        # queue of ssh requests msgs
        self.ssh_requests_command_queue = deque()  # for waiting if ssh_requests_command_queue is empty, notify when get new command
        lock_for_ssh_requests_command_queue = Lock()
        self.command_request = Condition(lock_for_ssh_requests_command_queue)

        # queue of ssh results msgs
        self.ssh_results_command_queue = deque()
        lock_for_ssh_results_command_queue = Lock()
        self.ssh_results_command_queue_waiter = Condition(lock_for_ssh_results_command_queue)

        # set of requests for approve control
        self.approve_control_requests = set()
        lock_for_approve_control_requests = Lock()
        self.approve_control_requests_waiter = Condition(lock_for_approve_control_requests)

        # set of approve control
        self.approved_control = set()

        # queues for connect/disconnect status realtime
        self.connect_friend_queue = deque()
        self.disconnect_friend_queue = deque()
        lock_for_connect_status = Lock()
        self.connect_status_waiter = Condition(lock_for_connect_status)

        self.set_external_ip()
        self.set_internal_ip()
        self.set_motherboard()
        self.set_cpu()
        # update my details(external_ip, internal_ip, motherboard, cpu) on server
        update_url = URL.updateURL + self.id
        PARAMS = {'externalIP': self.external_ip, 'internalIP': self.internal_ip, 'CPU': self.cpu, 'motherboard': self.motherboard}
        r = requests.post(url=update_url, json=PARAMS)  # sending data to the server
        #print(r.json())
        # open socket with client
        '''
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySocket.connect(('127.0.0.1',8823))
        '''
        self.connect()
        User.__instance = self

#    def __str__(self):
#        return 'name:' + self.name + " last name:" + self.last_name

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
        thread1.daemon = True
        thread2 = Thread(target=self.execute_command_from_ssh_requests_command_queue)
        thread2.daemon = True
        thread1.start()
        thread2.start()
        # announce my friend i am connected
        params = {'ID': self.id, "otherID": "broadcast",
                  'chat': {"senderName": self.name, "text": "i am connected!@#$"}}
        #print(params)
        r = requests.post(url=URL.postURL, json=params)
        return_msg = r.text
        #print(return_msg)

    def execute_command_from_ssh_requests_command_queue(self):
        #print("got in execute command")
        while True:
            # queue not empty - get new message
            if len(self.ssh_requests_command_queue) > 0:
                #print("execute_command got a command")
                data = self.ssh_requests_command_queue.pop()
                try:
                    result = self.execute_command(data['chat']['text'][16:])
                except:
                    result = "no respond"
                if result != '':
                    new_msg = {"sender_id": data['ID'], "ssh_cmd": result}
                    if self.show_ssh_res:
                        self.ssh_results_command_queue.append(new_msg)
                        self.ssh_results_command_queue_waiter.acquire()
                        self.ssh_results_command_queue_waiter.notify()
                        self.ssh_results_command_queue_waiter.release()
                    self.send_message(data['ID'], result)
            else:
                #print("execute_command go to sleep")
                self.command_request.acquire()
                self.command_request.wait()
                self.command_request.release()
                # print("execute_command woke up")
    def get_friend_status(self):
        friends_status = dict()
        friends = self.get_friends()
        # print("my friends:", end=' ')
        # print(friends)
        for friend in friends:
            '''
            user_data_from_server = requests.get(url=(URL.usersURL + "/" + friend))
            data = user_data_from_server.json()
            # print(data)
            status = data['isLogged']
            '''
            friends_status[friend] = self.check_friend_status(friend)
        return friends_status

    def check_friend_status(self, friend_id):
        user_data_from_server = requests.get(url=(URL.usersURL + "/" + friend_id))
        data = user_data_from_server.json()
        # print(data)
        status = data['isLogged']
        return status

    def listen_to_server(self):
        while True:
            # queue not empty - got new message
            if len(User.q) != 0:
                # pop the new msg
                data = User.q.pop()
                # check if the message designated to me
                if data['otherID'] == self.id:
                    # check the kind of the message - ordinary or control
                    if str(data['chat']['text']) == 'can i control yours computer?@#$<<':
                        self.approve_control_requests.add(data['ID'])
                        self.approve_control_requests_waiter.acquire()
                        self.approve_control_requests_waiter.notify()
                        self.approve_control_requests_waiter.release()
                        '''
                        new_msg = {"sender_id": data['ID'], "sender_name": data['chat']['senderName'],
                                   "text": "can i control yours computer? (press 'yes' or 'no' button)"}
                        self.my_queue.append(new_msg)
                        self.my_queue_waiter.acquire()
                        self.my_queue_waiter.notifyAll()
                        self.my_queue_waiter.release()
                        '''
                    elif str(data['chat']['text']).startswith('ssh control@#$<<') and data['ID'] in self.approved_control:
                        self.ssh_requests_command_queue.append(data)
                        self.command_request.acquire()
                        self.command_request.notify()
                        self.command_request.release()
                    elif str(data['chat']['text']).startswith('ssh control@#$<<'):
                        new_msg = {"sender_id": data['ID'], "sender_name": data['chat']['senderName'],
                                   "text": "send the bush command " + data['chat']['text'][16:]
                                                                       + " but it didnt execute"}
                        self.my_queue.append(new_msg)
                        self.my_queue_waiter.acquire()
                        self.my_queue_waiter.notify()
                        self.my_queue_waiter.release()
                    else:
                        new_msg = {"sender_id": data['ID'], "sender_name": data['chat']['senderName'],
                                   "text": data['chat']['text']}
                        self.my_queue.append(new_msg)
                        # for alert to main windows that the user get a new msg
                        self.sender_queue.append(new_msg["sender_id"])
                        self.my_queue_waiter.acquire()
                        self.my_queue_waiter.notifyAll()
                        self.my_queue_waiter.release()
                        '''
                        if len(self.my_dict_of_queue[data['ID']]) > 0:
                            self.my_dict_of_queue[data['ID']] = deque()
                            self.my_dict_of_queue[data['ID']].append(data['chat'])
                            self.my_queue_waiter.acquire()
                            self.my_queue_waiter.notify()
                            self.command_request.release()
                        else:
                            self.my_dict_of_queue[data['ID']].append(data['chat'])
                            self.my_queue_waiter.acquire()
                            self.my_queue_waiter.notify()
                            self.command_request.release()
                        '''
                # my friend announce to me he is disconnect/connect
                elif data['otherID'] == "broadcast" and data['ID'] in self.friends_list:
                    if str(data['chat']['text']) == 'i am connected!@#$':
                        new_msg = {"sender_id": data['ID']}
                        self.connect_friend_queue.append(new_msg)
                        self.connect_status_waiter.acquire()
                        self.connect_status_waiter.notify()
                        self.connect_status_waiter.release()
                    elif str(data['chat']['text']) == 'i am disconnected!@#$':
                        new_msg = {"sender_id": data['ID']}
                        self.disconnect_friend_queue.append(new_msg)
                        #time.sleep(.1)
                        self.connect_status_waiter.acquire()
                        self.connect_status_waiter.notify()
                        self.connect_status_waiter.release()
            # queue empty thread go to sleep, avoid busy waiting
            else:
                User.cv.acquire()
                User.cv.wait()
                User.cv.release()
        '''
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
        '''

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
            if msg != "":
                params = {'ID': self.id, "otherID": friend_id, 'chat': {"senderName": self.name, "text": msg} }
                #print(params)
                r = requests.post(url=URL.postURL, json=params)
                return_msg = r.text
                #print(return_msg)
                pastebin_url = r.text
                #print("now get")
                url = URL.postURL+self.id+"/"+friend_id
                #url = f"http://localhost:5000/api/chat/{self.id}/{friend_id}"

                ans = requests.get(url=url)
                data = r.json()
                #print("and the answer is :\n")
                #print(data)
        else:
            pass
            # print("ERROR can't to send a message to friend that not in your's friendsList")

    def send_ssh_message(self, friend_id, msg):
        msg = 'ssh control@#$<<' + msg
        params = {'ID': self.id, "otherID": friend_id, 'chat': {"senderName": self.name, "text": msg}}
        r = requests.post(url=URL.postURL, json=params)
        return_msg = r.text
        #print(return_msg)


    def get_message(self, friend_id):
        # Params : friend ID - the id of the friend that the message will be send to.
        # return the content of the message
        curURL = URL.getURL + "{}/{}".format(self.id, friend_id)
        r = requests.get(url=curURL)
        data = r.json()
        if data:
            list_of_msg = []
            if data['chat']:
                for i in data['chat']:
                    if 'senderName' in i.keys():
                        msg = [i['senderName'], i['text']]
                        list_of_msg.append(msg)
            return list_of_msg

    def get_friends(self):
        return self.friends_list

    def approve_control(self, friend_id, decision):
        '''
        :param friend_id: the id of the friend that ask for control
        :param decision: the user decision if approve to the ask (True or False)
        :return:
        '''
        #print(decision, end=' ')
        if decision:
            self.approved_control.add(friend_id)
            #print("approved control : " + str(self.approved_control))
            self.approve_control_requests.discard(friend_id)
            #print("queue of approved control requests : " + str(self.approve_control_requests))
        else:
            self.approve_control_requests.discard(friend_id)
            #print("approved control : " + str(self.approved_control))
            #print("queue of approved control requests : " + str(self.approve_control_requests))


    def remove_control(self, friend_id):
        '''
        :param friend_id: he id of the friend that you want to remove from approved_control set
        :return: string
        '''
        if friend_id in self.approved_control:
            self.approved_control.discard(friend_id)
            return friend_id +"removed from approved_control set"
        else:
            return friend_id +"did not add control on your computer"

    def ask_for_control(self, friend_id):
        params = {'ID': self.id, "otherID": friend_id, 'chat': {"senderName": self.name, "text": 'can i control yours computer?@#$<<'}}
        r = requests.post(url=URL.postURL, json=params)
        #print(r)

    def find_motherboard(self):
        try:
            #return the name of the motherboard by using bash as administrator
            command = 'dmidecode -t baseboard'
            motherboard_manufacturer = subprocess.check_output('echo %s|sudo -S %s | grep Manufacturer' % (self.sudo_password, command), shell=True)
            prod_name = '\'Product Name\''
            motherboard_product_name = subprocess.check_output('echo %s|sudo -S %s | grep %s' % (self.sudo_password, command, prod_name), shell=True)
            my_motherboard = (motherboard_manufacturer.decode("utf-8")[1:] + motherboard_product_name.decode("utf-8")[1:]).strip()
        except:
            # print("field to find my motherboard")
            my_motherboard = '-----'
        return my_motherboard

    def find_cpu(self):
        try:
            #return the name of the CPU by using bash as administrator
            command = 'dmidecode -t processor'
            cpu_version = subprocess.check_output('echo %s|sudo -S %s | grep Version' % (self.sudo_password, command), shell=True)
            my_cpu = (cpu_version.decode("utf-8")[1:]).strip()# remove /t
        except:
            my_cpu = '----'
        return my_cpu

    def find_external_ip(self):
        #return the name of the CPU by using bash as administrator
        try:
            command = 'dig +short myip.opendns.com @resolver1.opendns.com'
            external_ip = subprocess.check_output('echo %s|sudo -S %s' % (self.sudo_password, command), shell=True)
            my_external_ip = (external_ip.decode("utf-8")).strip()
        except:
            my_external_ip = '---'
        return my_external_ip

    def find_internal_ip(self):
        try:
            #return the name of the CPU by using bash as administrator
            command = 'hostname -I'
            internal_ip = subprocess.check_output('echo %s|sudo -S %s' % (self.sudo_password, command), shell=True)
            my_internal_ip = (internal_ip.decode("utf-8"))
            print(my_internal_ip)
            ''''
            print(my_internal_ip)
            print("1")
            print("ip len:" + str(len(my_internal_ip)))
            '''
            # print("my_internal_ip: " + my_internal_ip)
            if len(my_internal_ip) > 30:
                my_internal_ip = my_internal_ip[:29]
        except:
            my_internal_ip = '----'
        return my_internal_ip

    def execute_command(self, command):
        #return the name of the motherboard by using bash as administrator
        new_command = command
        for i in range(len(command)):
            if command[i] == '|':
                new_command = new_command[:i] + " 2>/dev/null " + new_command[i:]
        new_command += " 2>/dev/null "
        result = subprocess.check_output('echo %s|sudo -S %s' % (self.password, new_command), shell=True)
        if isinstance(result, bytes):
            decode_result = result.decode("utf-8")
        else:
            decode_result = "no response"
        return decode_result

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
        self.motherboard = self.find_motherboard()
        #need to write to data base

    def set_cpu(self):
        self.cpu = self.find_cpu()
        # need to write to data base

    def set_external_ip(self):
        self.external_ip = self.find_external_ip()
        # need to write to data base

    def set_internal_ip(self):
        self.internal_ip = self.find_internal_ip()
        # need to write to data base

    def get_my_motherboard(self):
        return self.motherboard

    def get_my_cpu(self):
        return self.cpu

    def get_my_external_ip(self):
        return self.external_ip

    def get_my_internal_ip(self):
        return self.internal_ip

    def get_friend_motherboard(self, friend_id):
        try:
            # return the friend motherboard
            friend_data_from_server = requests.get(url=(URL.usersURL + "/" + friend_id))
            data = friend_data_from_server.json()
            friend_motherboard = data['motherboard']
            if len(friend_motherboard)>75:
                friend_motherboard = friend_motherboard[:75]+'...'
        except:
            friend_motherboard = '----'
        return friend_motherboard

    def get_friend_cpu(self, friend_id):
        try:
            # return the friend cpu
            friend_data_from_server = requests.get(url=(URL.usersURL + "/" + friend_id))
            data = friend_data_from_server.json()
            friend_cpu = data['CPU']
            if len(friend_cpu)>75 :
                friend_cpu = friend_cpu[:75]+'...'
        except:
            friend_cpu = '----'
        return friend_cpu

    def get_friend_external_ip(self, friend_id):
        try:
            # return the friend external ip
            friend_data_from_server = requests.get(url=(URL.usersURL + "/" + friend_id))
            data = friend_data_from_server.json()
            friend_external_ip = data['externalIP']
        except:
            friend_external_ip = "-------"
        return friend_external_ip

    def get_friend_internal_ip(self, friend_id):
        try:
            # return the friend internal ip
            friend_data_from_server = requests.get(url=(URL.usersURL + "/" + friend_id))
            data = friend_data_from_server.json()
            friend_internal_ip = data['internalIP']
            if len(friend_internal_ip) > 15:
                friend_internal_ip = friend_internal_ip[:15] + "..."
        except:
            friend_internal_ip = '----'
        return friend_internal_ip

    def get_friend_name(self, friend_id):
        try:
            # return the friend name
            friend_data_from_server = requests.get(url=(URL.usersURL + "/" + friend_id))
            data = friend_data_from_server.json()
            friend_name = data['name']
        except:
            friend_name = '----'
        return friend_name

    def get_friend_last_name(self, friend_id):
        try:
            # return the friend name
            friend_data_from_server = requests.get(url=(URL.usersURL + "/" + friend_id))
            data = friend_data_from_server.json()
            friend_last_name = data['lastname']
        except:
            friend_last_name = '----'
        return friend_last_name

    def add_friend(self, friend_id):
        if friend_id == self.id:
            return False
        if friend_id not in self.friends_list:
            #-------------------------------------------------------need add check if the friend is exist
            #check_fried_exist =
            # add the friend to the friends data base
            add_friend_url = URL.addfriendURL + self.id
            PARAMS = {'friend': friend_id}
            r = requests.post(url=add_friend_url, json=PARAMS)  # sending data to the server
            r = r.json()
            # add result
            # print(r)
            #if r['Failed'] != 'true':
            #   if the friend is exist
            if 'Success' in r.keys():
                self.friends_list.append(friend_id)
                return True
        return False


    def remove_friend(self, friend_id):
        # Param : friend_id that need to be deleted from the friend list
        if friend_id in self.friends_list:
            try:
                remove_url = URL.removeURL + self.id
                PARAMS = {'friend': friend_id}
                r = requests.delete(url=remove_url, json=PARAMS)  # sending data to the server
                self.friends_list.remove(friend_id)
                # print(r)
            except ValueError as e:
                pass
                # print(e)
        else:
            return "Error : " + friend_id + "not in yours friend list"

    def send_file(self):
        pass

    def disconnect(self):
        '''
        very imported to use that func when user disconnected for data security
        and for update my friend i am disconnected
        '''
        url = URL.loguotURL + self.id
        r = requests.post(url=url)
        #print(r.json())

        params = {'ID': self.id, "otherID": "broadcast", 'chat': {"senderName": self.name, "text": "i am disconnected!@#$"}}
        #print(params)
        r = requests.post(url=URL.postURL, json=params)
        # return_msg = r.text
        # print(return_msg)
        User.sio.disconnect()
        __instance = None
        User.can_exit_safe = True

    def disconnect_from_chat(self):
        User.sio.disconnect()

if __name__ == '__main__':
    """
    result = connect('testUser', '12345', '2323')
    if isinstance(result, str):
        print(result)
    else:
        result.send_message('testUser2','what your name?')
        print(result.getMessage('testUser2'))
        #print(User.get_instance().get_my_cpu())
        #print(User.get_instance().get_friend_external_ip('mtd'))
        #print(User.get_instance().get_friend_internal_ip('mtd'))
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
    """
