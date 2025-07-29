import random
import string

print("Hello, welcome to this password generator")

while True: 
    length = int(input("Enter Length: "))
    if  length > 128:
        print("Sorry, password is too long. Read this article too learn what the best length for a password is: https://bitwarden.com/blog/how-long-should-my-password-be/ ")
        continue
    
    if  length < 8:
        print("Sorry, password is too short. Read this article too learn what the best length for a password is: https://bitwarden.com/blog/how-long-should-my-password-be/ ")
        continue
       
    chars = string.ascii_letters
    chars += string.digits
    chars += string.punctuation 

    password = ""

    for i in range(length) :
        password += random.choice(chars)

    print("Your random password is:", password)   

    repeat = input("Do you want to generate another password? (yes/no) :")
    if repeat == "no":
        print("End, thank you for using this password generator")
        break