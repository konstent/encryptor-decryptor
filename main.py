# import modules

from cryptography.fernet import Fernet
import time
import timg
import os
import base64

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
    print("3. Encrypt your Text")
    print("4. Decrypt your Text")
    print("-----------------------------------------------------------")
    menu_option = int(input("Enter your choice: "))
    return menu_option

def encryption():
    key = Fernet.generate_key()
    save_path = "/Users/taha/Desktop"
    user_file = str(input("Enter your file path: "))
    key_file = os.path.join(save_path, "enc_key.key")
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

def text_encryption():
    Simple_Text = input("Enter Your Simple Text: ")  # Example = Good Morning
    base64_encrypted_text = base64.b85encode(Simple_Text.encode("utf-8"))
    print("[+] Your Text is successfully Encrypted")
    print("It's Your Encrypted Text: ", base64_encrypted_text)

def text_decryption():
    base64_encrypted_text = input("Enter Your Encrypted Text: ")
    base64_decryptted_text = base64.b85decode(base64_encrypted_text).decode("utf-8")
    print("We are decrypting your text...")
    time.sleep(3)
    print("Your text decryption is successful")
    print("It's Your Decrypted Text: ", base64_decryptted_text)


return_menu_option = main_menu()

if return_menu_option == 1:
    encryption()
elif return_menu_option == 2:
    decryption()
elif return_menu_option == 3:
    text_encryption()
elif return_menu_option == 4:
    text_decryption()
else:
    print("Wrong Choice, Try Again ?(y/n)")
    yes_and_no = str(input("Your choice: "))
    if yes_and_no == "y" and "Y":
        main_menu()
    elif yes_and_no == 'n' and "N":
        exit()


