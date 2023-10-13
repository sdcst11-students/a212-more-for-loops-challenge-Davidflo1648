#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]

username = input("Enter your username: ")

if username in users:
    index = users.index(username)

    password = input("Enter your password: ")

    if password == passwords[index]:
        print("Login successful!")
    else:
        print("Incorrect password. Login failed.")
else:
    print("Username not found. Login failed.")
