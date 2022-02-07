import os
import random
import math
import secrets

#Mastermind in Python
true = True # Did this because almost every other language is lowercase and its annoying to write
false = False
Passcode = []
Guesses = 0
CurrentNum = 0;
GuessStorage = []
LengthOfGame = 4 # Allows dynamics

#Functions
def CheckNumber(Guess, Index):
    if (Passcode[Index] == Guess):
        return true
    else:
        return false

def CheckExistence(Number):
    if Number in Passcode:
        return true
    else:
        return false

def GeneratePasscode(Length):
    for i in range(Length):
        Passcode.append(secrets.randbelow(9)) # Uses python encryption library because why not?
        random.shuffle(Passcode) # Shuffle after every iteration

    for i in range(len(Passcode)):
        random.shuffle(Passcode) # Maybe a bit more for extra randomness...

GeneratePasscode(LengthOfGame) # Generate the starting passcode
print("Welcome to mastermind! I have generated a random 4-digit code, think you can guess it? You have 10 tries, good luck!")
while true:
    UserGuess = input("Please guess a number: ")
    Guesses = Guesses + 1
    if CheckNumber(int(UserGuess), CurrentNum):
        print("Thats correct! Good job!")
        GuessStorage.append(int(UserGuess))
        CurrentNum = CurrentNum + 1
    elif CheckNumber(int(UserGuess), CurrentNum) == false and CheckExistence(int(UserGuess)):
        print("That number is correct, but it isn't in the right place! Try again!")
    else:
        print("Nope! Try again!")

    if (GuessStorage == Passcode):
        print("Congrats, you cracked the code! The code was " + (''.join(str(x) for x in Passcode)) + "! It took you " + str(Guesses) + " tries!")
        break