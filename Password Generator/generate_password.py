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

lowercase = ''.join(choice(string.ascii_lowercase) for x in range(randint(length,len(string.ascii_lowercase))))
uppercase = ''.join(choice(string.ascii_uppercase) for x in range(randint(uppercase_minimum,len(string.ascii_uppercase))))
numbers = ''.join(choice(string.digits) for x in range(randint(numbers_minimum,len(string.digits))))
special = ''.join(choice(special_characters) for x in range(randint(special_minimum,len(special_characters))))

# Compile chosen characters
password = lowercase + uppercase + numbers + special

# Randomize the string and print to user
password = ''.join(random.sample(password, len(password)))
print(password)
