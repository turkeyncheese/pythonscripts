#!/usr/bin/python

import random

Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def sub():
    brute = str(input("Would you like to brute force? (Yes / No): "))
    if brute == "Yes":
        text = str(input("Enter your encrypted text: "))
        testSize = int(input("How many times would you like to try and brute force? (Integer): "))
        bruteforce(text, testSize)
    else:        
        text = str(input("Enter your message: "))
        mode = str(input("Encrypt or Decrypt?: "))
        key = ''
    
        while checkKey(key) is False:
            key = str(input("Enter a 26 character ALPHA key or leave blank for random key: "))
            if key == '':
                key = randomKey()
            if checkKey(key) is False:
                print("There was an error in your key.")
        print("Key: " + key)
        print("Output:")
        print(cipher(text, key, mode))
    
def randomKey():
    randomList = list(Letters)
    random.shuffle(randomList)
    return ''.join(randomList)

def checkKey(key, alpha):
    keyString = ''.join(sorted(list(key)))
    return keyString == Letters

def cipher(text, key, mode):
    out = ''
    chars_1 = Letters
    chars_2 = key
    if str(mode) == 'Decrypt':
        chars_1, chars_2 = chars_2, chars_1
    for char in text:
        if char.upper() in chars_1:
            index = chars_1.find(char.upper())
            if char.isupper():
                out += chars_2[index].upper()
            else:
                out += chars_2[index].lower()
        else:
            out += char
    return out

def bruteforce(encrypted, testSize):
    for i in range(1, testSize + 1):
        key = randomKey()
        out = cipher(encrypted, key, "Decrypt")
        print(f'Test {}:\nKey: {}\nOutput: {}'.format(i, key, out))
    print("DONE!")
