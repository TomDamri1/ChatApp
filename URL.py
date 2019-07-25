from time import sleep
import os
try:
    # print('try')
    sleep(0.1)
    path = os.path.expanduser('~')
    path = path + '/url.txt'
    f = open(path, 'r')
    if f.mode == 'r':
        URL = f.read()
    f.close()
except Exception as error:
    # print('except')
    print(error)
    URL = "http://linuxchat.herokuapp.com/"
# print('URL is:' + URL)
'''
URL = "http://linuxchat.herokuapp.com/"
URL2 = "http://localhost:5000/"
'''

postURL = URL + "api/chat/"
getURL = URL + "api/chat/"
usersURL = URL + "api/users/"
loginURL = URL + "api/users/login"
addfriendURL = URL + "api/users/addfriend/"
updateURL = URL + "api/users/update/"
removeURL = URL + "api/users/removefriend/"
loguotURL = URL + "api/users/logout/"
registerURL = URL + "api/users/register"