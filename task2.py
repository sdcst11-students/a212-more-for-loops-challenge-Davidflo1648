#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"

attempts = 0
max_attempts = 3

for i in range(max_attempts):
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if username == expectedUsername and password == expectedPassword:
        print("Access Granted.")
        break
    else:
        print("Access Denied.")
else:
    print("You got locked out.")