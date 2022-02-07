import os
import random
import math
import secrets
#Mastermind in Python 3.10


#Config
LengthOfGame = 4 # Allows dynamics
AllowedGuesses = 10

#Internal Vars
true = True # Did this because almost every other language is lowercase and its annoying to write
false = False
Passcode = []
Guesses = 0
CurrentNum = 0;
GuessStorage = []

#Functions
def CheckNumber(Guess, Index):
    if (Passcode[Index] == Guess):
        return true
    else:
        return false

def CheckExistence(Number):
    for i in range(len(Passcode)): # This is generally considered "inefficient", but it gets the job done well enough
        if (Passcode[i] < CurrentNum):
            continue
        else:
            if Number == Passcode[i]:
                return true
    return false

def GeneratePasscode(Length):
    for i in range(Length):
        Passcode.append(secrets.randbelow(9)) # Uses python encryption library because why not?
        random.shuffle(Passcode) # Shuffle after every iteration

GeneratePasscode(LengthOfGame) # Generate the starting passcode
print("Welcome to mastermind! I have generated a random " + str(LengthOfGame) + "-digit code, think you can guess it? You have " + str(AllowedGuesses) + " tries, good luck!")

# Main Loop
while true:
    UserGuess = input("Please guess a number: ")
    if (Guesses == AllowedGuesses):
        print("You ran out of guesses! The code was " + (''.join(str(x) for x in Passcode)) + "! It took you " + str(Guesses) + " tries!")
        break
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