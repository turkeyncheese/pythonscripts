#!/usr/bin/python

text = str(input("Enter text: "))
count = 0
for char in text:
  if char in 'aeiouAeiou':
    count += 1
print(f'There are {count} vowels and {len(text) - count} consonants.')
