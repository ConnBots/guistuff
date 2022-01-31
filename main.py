from logging.config import valid_ident
from multiprocessing.sharedctypes import Value
from termcolor import colored
import time
import sys
import random

print(colored('Welcome to the terminal.', 'yellow'))

time.sleep(2)

print(colored('Please enter your access code', 'cyan'))

Val = input("Code: ")
if Val == "123":

    time.sleep(2)

    print(colored('Sucess, logging you in', 'red'))
    
else:
    print("Wrong code")
