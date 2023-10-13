#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
import random
number = random.randint(1, 100)
attempts = 0
max_attempts = 10

for i in range(max_attempts):
    guess = int(input("Enter a number: "))

    if guess < number:
        print("Too low. Try again!")
    elif guess > number:
        print("Too high. Try again!")
    else:
        print(f"Congratulations! You guessed the number, which is {number}!")
        break
else:
    print(f"Game Over! \nYou failed all your attemps, the correct number was {number}")

