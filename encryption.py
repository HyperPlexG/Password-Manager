from cryptography.fernet import Fernet
from dotenv import load_dotenv, set_key, find_dotenv
import os
import hashlib


# Creating a .env file if not present
with open(".env", "a") as file:
    pass

dotenv_file = find_dotenv()                             #looking for files with .env exactly
load_dotenv(dotenv_file)                                #take environment variables from .env

# Master Password Hash and Check
def DoesHashExist():
    try:
        if os.environ["master"] != "":                  #os.environ returns a dictionary having user’s environmental variable as key and their values as value.
            return True
    except:
        return False


def generate_hash():
    if DoesHashExist() == False:
        print("Set your Master Password\n")
        masterPass = input("Set Master Password: ")
        print("\nPlease do not forget this password, as otherwise your passwords cannot be recovered")
        print("-" * 40)
        sha256_MasterPass = hashlib.sha256(masterPass.encode()).hexdigest()                                 #The SHA hash functions encode it and then using hexdigest(), hexadecimal equivalent encoded string is printed.
        os.environ["master"] = sha256_MasterPass
        set_key(dotenv_file, "master", os.environ["master"])


def check_hash():
    hash = os.environ["master"]
    MasterPasswordInputNow = input("Enter the Master Password: ")
    MasterPasswordInputNowHashed = hashlib.sha256(MasterPasswordInputNow.encode()).hexdigest()
    if MasterPasswordInputNowHashed == hash:
        return True
    else:
        return False


# Secret key Generation
def DoesKeyExist():
    try:
        if os.environ["key"]:
            return True
    except:
        return False


def generateKey():
    if not (DoesKeyExist()):
        key = Fernet.generate_key()
        key_str = str(key, "utf-8")
        os.environ["key"] = key_str
        set_key(dotenv_file, "key", os.environ["key"])


def loadKey():
    key = bytes(os.environ["key"], "utf-8")
    return key


def encryptPass(passw):
    key = loadKey()
    fernet = Fernet(key)
    encodedPass = passw.encode()
    encryptedPass = fernet.encrypt(encodedPass)
    return encryptedPass


def decryptPass(encryptedPass):
    key = loadKey()
    fernet = Fernet(key)
    decryptedPass = fernet.decrypt(encryptedPass)
    passw = decryptedPass.decode()
    return passw