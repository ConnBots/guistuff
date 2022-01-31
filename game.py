from termcolor import colored
import time
import sys
import random

print(colored('Welcome to the game...','red'))
time.sleep(1)
print(colored('How would you like to play?', 'red'))

print("Your play options: ")
print("1: Storymode (SM)")
print("2: Adventure Mode (AM)")

# Questions related to above.

gameoption = input("Enter: ")

if gameoption == "SM": # Checks to see if player entered SM as their gamemode.
    print(colored('Starting Game.', 'yellow'))
    time.sleep(1)
    
    words = "Welcome."
    for char in words:
     time.sleep(0.1)
     sys.stdout.write(char)
     sys.stdout.flush()

    print("")

    time.sleep(1)

    words1 = "You see a monster in the forest, what is your move?"
    for char in words1:
     time.sleep(0.1)
     sys.stdout.write(char)
     sys.stdout.flush()

    time.sleep(1)

    print("")

    print("Your moves: Attack (A) Run Away (RA)")

    action1 = input("Your Move: ")

    if action1 == "A": # Checks to see if the user picked Attack as their option. 
    
     words2 = "You run into the forest and attack"
     for char in words2:
      time.sleep(0.1)
      sys.stdout.write(char)
      sys.stdout.flush()