# !/usr/bin/env python3

# Purpose: To generate a password

import string
from random import *
import random

# Get requirements
print("\nMinimums")
length = int(input("What is the minimum password length? -> "))
uppercase_minimum = int(input("How many upper case characters? -> "))
numbers_minimum = int(input("How many numbers? -> "))
special_minimum = int(input("How many special characters? -> "))

print("\nSpecial Cases")
special_characters = input("What special characters can be used? -> ")

lowercase = ''.join(choice(string.ascii_lowercase) for x in range(randint(length,length+4)))
uppercase = ''.join(choice(string.ascii_uppercase) for x in range(randint(uppercase_minimum,uppercase_minimum+4)))
numbers = ''.join(choice(string.digits) for x in range(randint(numbers_minimum,numbers_minimum+4)))
special = ''.join(choice(special_characters) for x in range(randint(special_minimum,special_minimum+4)))

# Compile chosen characters
password = lowercase + uppercase + numbers + special

# Randomize the string and print to user
password = ''.join(random.sample(password, len(password)))
print(password)
