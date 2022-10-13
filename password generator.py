# Ask user if they wish to generate a password
# If yes, ask for length
# Generate password
# Print password
# If initial response is no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)


    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Yes/No): ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program has finished")
    quit()
else:
    print("Invalid input, user must input Yes or No")
    quit()