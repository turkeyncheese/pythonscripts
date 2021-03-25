import random
import string

mode = int(input("Enter 1 for just uppercase letters, 2 for lowercase, 3 for both, and 4 for all characters: "))
length = int(input("How long would you like your password to be? (integer): "))
amount = int(input("How many passwords would you like to generate? (integer): "))

def random_password(mode, length, amount):
    if mode == 1:
        characters = string.ascii_uppercase
    elif mode == 2:
        characters = string.ascii_lowercase
    elif mode == 3:
        characters = string.ascii_letters
    elif mode == 4:
        characters = string.ascii_letters + string.punctuation + string.digits
    for i in range(amount):
        print(''.join(random.choice(characters) for i in range(length)))

random_password(mode, length, amount)
