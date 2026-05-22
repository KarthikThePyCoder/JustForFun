import random
import time
import string

# Define the list of characters
characters = string.ascii_uppercase + string.ascii_uppercase + string.digits + string.punctuation
print('This is a random character generator. It generates any symbol on your keyboard! I hope you do not get something weird..')
time.sleep(3)
print(random.choice(characters))