import secrets
import string

print("Hello, welcome to this password generator")

while True: 
    try:
        length = input("Chose lenght of your password: (short: 8 characters, medium: 16 characters and long: 25 characters!) short/mid/long ")
    except ValueError:
        print("Error: Incorrect input, pleas try again!.")
        continue
    if length == "short":
        length is 8
    elif length == "mid":
        length is 16
    elif len == "long":
        length  is 25


       
    chars = string.ascii_letters
    chars += string.digits
    chars += string.punctuation 

    password = ""

    for i in range(length) :
        password += secrets.choice(chars)

    print("Your random password is:", password)

    repeat = input("Do you want to generate another password? (yes/no) :")
    if repeat == "no":
        print("End, thank you for using this password generator")
        break