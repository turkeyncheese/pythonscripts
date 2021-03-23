#!/usr/bin/python

pali = str(input("Enter word to be checked: "))
if pali == pali[::-1]:
  print('Yes, ' + pali + ' is a palindrome.')
else:
  print('No, ' + pali + ' is not a palindrome.')
