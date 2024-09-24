#pip install cryptography
from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("Enter your master password: ")
key = load_key() + master_pwd.encode()
fer=Fernet(key)

def view():
    with open("passwords.txt", "r") as f: #a mode = append, w = write, r = read
        for line in f.readlines():
            #print(line.strip())
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, "|| passw:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Enter your name: ")
    pwd = input("password: ")

    with open("passwords.txt", "a") as f: #a mode = append, w = write, r = read
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("view or add ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()

    else:
        print ("Invalid input")
        continue
