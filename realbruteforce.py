import hashlib

def password_cracker(hash, n, show):
    characters = 'abcdefghijklmnopqrstuvwxyz' #or all characters you wish to try
    passwords = []
    for current in range(n):
        a = [i for i in characters]
        for y in range(current):
            a = [x + i for i in characters for x in a]
        passwords += a

    for word in passwords:
        object = hashlib.md5(word.encode())
        guess = object.hexdigest()
        if show == 'Yes':
            print('Trying: ' + word)
        if guess == hash:
            password = word
            break
    return 'Password is: ' + str(password)

hash = str(input('Enter your MD5 hash: '))
n = int(input('How long of a password would you like to try?: '))
show = str(input('Show all passwords? (Yes/No): '))
print(password_cracker(hash, n, show))
