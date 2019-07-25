import requests
import subprocess
import URL


def connect(user_id, password, sudo_password):
    """
    1. check if the user exist in the server
    2. check if the sudo password is correct
    :param user_id: the user that try to connect
    :param password: the password of the user
    :param sudo_password: the sudo password of the user "admin user"
    :return: True if the user_id + password is exist, and sudo_password correct, False if not
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
        elif r.json()['Login'] == 'No login found':
            return False
        elif r.json()['Login'] == "Logged in successfully ":
            return True
        else:
            print("user check on server return diff msg")
            return "user check on server return diff msg"
    if not user_password_check():
        return 'Wrong username or password'
    elif not sudo_password_check(sudo_password):
        return 'wrong sudo password'

    return True
