#!/usr/bin/python3
 
import sys
 
again = 0

while again == 0:
    if len(sys.argv) > 0:
        for word in words:
            if word[0] in 'aeiouAEIOU':
                    print(word + "way", end = " ")
            else:
                b = word[0].lower()
                a = word[1:].lower()
                print(b + a + "ay", end = " ")
    else:
        words = str(input("Input Sentence:")).split()
        for word in words:
            if word[0] in consonants:
                 if word[0].upper() == True:
                    b = word[0].lower()
                    a = word[1:].lower()
                    print(a + b + "ay", end = " ")
                else:
                    b = word[0].lower()
                    a = word[1:].lower()
                    print(a + b + "ay", end = " ")
            else:
                print(word + "way", end = " ")
    print()
    print()
    again = int(input("Enter 0 to translate another sentence, and 1 to exit: "))
