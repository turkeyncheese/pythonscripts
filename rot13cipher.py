def rot13(text):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        out = ''
        for letter in text:
                if letter.islower():
                        index = ord(letter)
                        newLetter = alpha[((index + 13) % len(alpha))]
                        out += newLetter.lower()
                elif letter.isupper():
                        index = ord(letter)
                        newLetter = alpha[((index + 13) % len(alpha))]
                        out += newLetter.upper()
                else:
                        out += letter
        return out
                        
        
