import hashlib

def password_cracker(hash, n):
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
        print('Trying: ' + word)
        if guess == hash:
            password = word
            break
    print('Password is: ' + str(password))
