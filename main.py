# import modules

from cryptography.fernet import Fernet
import time
import timg
import os

# writing code here

obj = timg.Renderer()
obj.load_image_from_file("logo.png")
obj.resize(100, 30)
obj.render(timg.ASCIIMethod)

def main_menu():
    print("-----------------------------------------------------------")
    print("                            Menu                           ")
    print("-----------------------------------------------------------")
    print("1. Encrypt your File")
    print("2. Decrypt your File")
    print("-----------------------------------------------------------")
    menu_option = int(input("Enter your choice: "))
    return menu_option

def encryption():
    key = Fernet.generate_key()
    user_file = str(input("Enter your file path: "))
    location = user_file.split("/")
    no_of_element = int(len(location))
    location.pop(no_of_element-1)
    location.pop(0)
    updated_location = str("/"+"/".join(location)+"/")
    key_file = os.path.join(updated_location, "enc_key.key")
    with open(key_file, 'wb') as filekey:
        filekey.write(key)
    with open(key_file, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    file = user_file
    with open(file, 'rb') as input_file:
        original = input_file.read()
    encrypted = fernet.encrypt(original)
    with open(user_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        print("\n[+] your file is successfully encrypted.")


def decryption():
    enc_file = str(input("provide the location for your encrypted file: "))
    enc_key = str(input("provide the location of key file (.key extension): "))
    with open(enc_key, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(enc_file, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    print("We are Decrypting your file...")
    time.sleep(3)
    decrypted = fernet.decrypt(encrypted)
    with open(enc_file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    print("We are removing your key")
    time.sleep(2)
    os.remove(enc_key)
    print("[+] Your file decryption is successful")


return_menu_option = main_menu()

if return_menu_option == 1:
    encryption()
elif return_menu_option == 2:
    decryption()
else:
    print("Wrong Choice, Try Again ?(y/n)")
    yes_and_no = str(input("Your choice: "))
    if yes_and_no == "y" and "Y":
        main_menu()
    elif yes_and_no == 'n' and "N":
        exit()




