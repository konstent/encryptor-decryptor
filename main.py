# import modules
import fernet as fernet
from cryptography.fernet import Fernet
import time
import timg

# writing code here
obj = timg.Renderer()
obj.load_image_from_file("logo.png")
obj.resize(100, 30)
obj.render(timg.ASCIIMethod)

def menu():
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
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    file = str(input("Provide the location of file you want to encrypt: "))
    with open(file, 'rb') as input_file:
        original = input_file.read()
    encrypted = fernet.encrypt(original)
    with open('encrypted.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        print("\n[+] your file is successfully encrypted and saved in encrypted.txt")
        print("INFO: Don't run encryption on other file, first decrypt your encrypted file\n")
        print("Redirect you to main menu in 5 seconds...\n")
        time.sleep(5)
    menu()


def decryption():
    def decryption_menu():
        print("\n-----------------------------------------------------------")
        print("                        Sub-Menu"                           )
        print("-----------------------------------------------------------")
        print("1. Decrypt Other File")
        print("2. Decrypt default file which is saved in encrypted.txt")
        choice = int(input("Your Choice: "))
        return choice
    client_choice = decryption_menu()
    if client_choice == 1:
        enc_file = str(input("provide the location for your encrypted file: "))
        enc_key = str(input("provide the location of key file (.key extension): "))
        with open(enc_key, 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        with open(enc_file, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        print("We are Decrypting your file")
        time.sleep(3)
        decrypted = fernet.decrypt(encrypted)
        with open('other_decrypted.txt', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        print("[+] Your file decrypton is successful, check your decrypted file in other_decrypted.txt")
    elif client_choice == 2:
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        with open('encrypted.txt', 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open('decrypted.txt', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
    else:
        print("Wrong Choice, Try Again...")
        time.sleep(2)
        decryption_menu()
return_menu_option = menu()

if return_menu_option == 1:
    encryption()
elif return_menu_option == 2:
    decryption()
else:
    print("Wrong Choice, Try Again ?(y/n)")
    yes_and_no = str(input("Your choice: "))
    if yes_and_no == "y" and "Y":
        menu()
    elif yes_and_no == 'n' and "N":
        exit()





