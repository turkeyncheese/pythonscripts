import datetime

code = str(input('Enter a 6-digit code: '))

if len(code) == 6:
    for char in code:
        if char not in '1234567890':
            print(code + ' is not a 6-digit number.')
            exit()
elif len(code) != 6:
    print(code + ' is not a 6-digit number.')
    exit()
        
start = datetime.datetime.now()

code = code.lstrip('0')
code = int(code)

guess = 999999

for i in range(1, 1000000):
    if guess == code:
        break
    guess = guess - 1

if guess == code:
    if guess < 100000 and guess > 9999:
        guess = '0' + str(guess)
    elif guess < 10000 and guess > 999:
        guess = '00' + str(guess)
    elif guess < 1000 and guess > 99:
        guess = '000' + str(guess)
    elif guess < 100 and guess > 9:
        guess = '0000' + str(guess)
    elif guess < 10:
        guess = '00000' + str(guess)
    end = datetime.datetime.now()
    print('Password is: ' + str(guess))
    print(f'Time taken to brute force: {end - start} seconds')
