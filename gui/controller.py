from gui.controlled.login_ui import Ui_LoginPage
from gui.controlled.mainWindow_ui import Ui_mainWindow
import threading
import os
from multiprocessing import Process


loggin_in_process = Process(target=os.system , args=("python3 controlled/login_ui.py",))
loggin_in_process.start()
loggin_in_process.join()
f= open("info.file" , "r")
user_id = f.readline()


