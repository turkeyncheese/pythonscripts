#Python program to run through all possible combinations of 6 digit numbers
#It's a little long but I'm sure someone out there can make it shorter or 
#into a one-liner, ewh, hate those guys...


import datetime

code = str(input('Enter a 6-digit code: '))

start = datetime.datetime.now()

code = code.lstrip('0')
code = int(code)

guess = 999999

for i in range(1, 1000000):
    if guess == code:
        break
    guess = guess - 1

if guess == code:
    if guess < 100000:
        guess = '0' + str(guess)
    elif guess < 10000:
        guess = '00' + str(guess)
    elif guess < 1000:
        guess = '000' + str(guess)
    elif guess < 100:
        guess = '0000' + str(guess)
    elif guess < 10:
        guess = '00000' + str(guess)
    end = datetime.datetime.now()
    print('Password is: ' + str(guess))
    print(f'Time taken to brute force: {end - start} seconds')
else:
    print('Could not find password.')
    print('Password was: ' + str(code))
