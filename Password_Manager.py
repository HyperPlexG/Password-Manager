from menu import menu, store, find, find_email
from encryption import generate_hash, check_hash
import sys

generate_hash()
if not check_hash():
    print("Wrong Password")
    sys.exit()
while True:
    choice = menu()
    if choice == "1":
        store()
    elif choice == "2":
        find()
    elif choice == "3":
        find_email()
    elif choice.lower() == "q":
        print("Exiting...")
        break
    else:
        print("-" * 20)
        print("Please enter a valid option")
        