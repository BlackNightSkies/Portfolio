# !/usr/bin/env python3

# Purpose: To generate a password

import string
from random import *
import random

# Get requirements
print("\nMinimums")
while True:
    length = input("What is the minimum password length? -> ")
    try:
        length = int(length)
    except ValueError:
        print("Please enter an integer.")
        continue
    else:
        break
while True:
    uppercase_minimum = input("How many uppercase characters? -> ")
    try:
        uppercase_minimum = int(uppercase_minimum)
    except ValueError:
        print("Please enter an integer.")
        continue
    else:
        break
while True:
    numbers_minimum = input("How many numbers? -> ")
    try:
        numbers_minimum = int(numbers_minimum)
    except ValueError:
        print("Please enter an integer.")
        continue
    else:
        break
while True:
    special_minimum = input("How many special characters? -> ")
    try:
        special_minimum = int(special_minimum)
    except ValueError:
        print("Please enter an integer.")
        continue
    else:
        break

print("\nSpecial Cases")
special_characters = input("What special characters are allowed? -> ")

lowercase = ''.join(choice(string.ascii_lowercase) for x in range(randint(length,length+4)))
uppercase = ''.join(choice(string.ascii_uppercase) for x in range(randint(uppercase_minimum,uppercase_minimum+4)))
numbers = ''.join(choice(string.digits) for x in range(randint(numbers_minimum,numbers_minimum+4)))
special = ''.join(choice(special_characters) for x in range(randint(special_minimum,special_minimum+4)))

# Compile chosen characters
password = lowercase + uppercase + numbers + special

# Randomize the string and print to user
password = ''.join(random.sample(password, len(password)))
print("\nPassword: ", password)
