#!/usr/bin/python

Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
UpperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LowerLetters = 'abcdefghijklmnopqrstuvwxyz'

def piglatin(text, mode):
	out = []
	words = text.split(' ')
	count = 1
	for word in words:
		for letter in word:
			if letter not in Letters:
				count = 0
		if count == 0:
			out.append(word)
		elif word[0] in 'aeiouAEIOU':
			out.append(word + "way")
		else:
			b = word[0].lower()
			a = word[1:].lower()
			out.append(a + b + "ay")
	return ' '.join(out)

def vigenere(text, key, mode):
	key_len = len(key)
	key_ints = [ord(i) for i in key]
	text_ints = [ord(i) for i in text]
	out = ''
	for i in range(len(text_ints)):
		adder = key_ints[i % key_len]
		if str(mode) == 'Decrypt':
			adder *= -1
		new = (text_ints[i] - 32 + adder) % 95
		out += chr(new + 32)

	if str(mode) != 'Decrypt' and str(mode) != 'Encrypt':
		return 'Invalid input for mode.'
	else:
		return out

def decimalToBinary(n):
	return bin(n).replace("0b", "")

def binaryToDecimal(n):
	return int(n, 2)

def caesar(text, shift):
	out = ''
	for char in text:
		if char.isupper() == True:
			out += chr((ord(char) + shift - 65) % 26 + 65)
		elif char.islower() == True:
			out += chr((ord(char) + shift - 97) % 26 + 97)
		else:
			out += str(char)
	return out

def morse(text, mode):
	Morse = {'A':'.-', 'B':'-...',
		'C':'-.-.', 'D':'-..', 'E':'.',
		'F':'..-.', 'G':'--.', 'H':'....',
		'I':'..', 'J':'.---', 'K':'-.-',
		'L':'.-..', 'M':'--', 'N':'-.',
		'O':'---', 'P':'.--.', 'Q':'--.-',
		'R':'.-.', 'S':'...', 'T':'-',
		'U':'..-', 'V':'...-', 'W':'.--',
		'X':'-..-', 'Y':'-.--', 'Z':'--..',
		'1':'.----', '2':'..---', '3':'...--',
		'4':'....-', '5':'.....', '6':'-....',
		'7':'--...', '8':'---..', '9':'----.',
		'0':'-----', ', ':'--..--', '.':'.-.-.-',
		'?':'..--..', '/':'-..-.', '-':'-....-',
		'(':'-.--.', ')':'-.--.-'}

	if str(mode) == 'Encrypt':
		out = ''
		for char in text:
			if char != ' ':
				out += Morse[char.upper()] + ' '
			else:
				out += ' '
		return out

	elif str(mode) == 'Decrypt':
		text += ' '
		decipher = ''
		citext = ''
		for letter in text:
			if letter != ' ':
				i = 0
				citext += letter
			else:
				i += 1
				if i == 2 :
					decipher += ' '
				else:
					decipher += list(Morse.keys())[list(Morse.values()).index(citext)]
					citext = ''

		return decipher

	else:
		return "Invalid input for mode."

print("\033c")
print("1. Binary to Decimal")
print("2. Decimal to Binary")
print("3. Caesar Cipher")
print("4. Morse Code")
print("5. Pig Latin")
print("6. Vigenere Cipher")
print(' ')
choice = int(input("Choose one of the above (1 - 6): "))

if choice == 1:
	n = str(input("Enter binary string: "))
	print(binaryToDecimal(n))
  
elif choice == 2:
	n = int(input("Enter a number: "))
	print(decimalToBinary(n))
  
elif choice == 3:
	mode = str(input("Encrypt or Decrypt?: "))
  
	if mode == 'Decrypt':
		text = str(input("Enter your text: "))
		for i in range(1, 26):
			print(f"Shift {i}: {caesar(text, i)}")
      
	elif mode == 'Encrypt':
		shift = int(input("Enter your shift (1 - 25): "))
		text = str(input("Enter your text: "))
		print(caesar(text, shift))
    
	else:
		print('Invalid input for mode.')

elif choice == 4:
	mode = str(input("Encrypt or Decrypt?: "))
	text = str(input("Enter your message: "))
	print(morse(text.upper(), mode))
  
elif choice == 5:
	text = str(input("Enter your text: "))
	print(piglatin(text))
  
elif choice == 6:
	mode = str(input("Encrypt or Decrypt?: "))
	text = str(input("Enter your text: "))
	key = str(input("Enter your key: "))
	print(vigenere(text, key, mode))
  
else:
	print("Invalid choice.")
