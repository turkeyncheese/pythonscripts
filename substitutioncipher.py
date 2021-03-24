#!/usr/bin/python

import random

Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def randomKey():
    randomList = list(Letters)
    random.shuffle(randomList)
    return ''.join(randomList)

def checkKey(key, alpha):
    keyString = ''.join(sorted(list(key)))
    return keyString == Letters

def encode(text, key):
    out = ''
    chars_1 = Letters
    chars_2

def bruteforce(encrypted, testSize):
    for i in range(1, testSize + 1):
        key = randomKey()
        print(f'Test {}:\nKey: {}\nOutput: {}'.format(i, key, out))
