from random import randint
import string

def ver_cipher(text, key):
	alphabet = string.ascii_letters
	N = len(alphabet)
	i = 0
	code = ""
	key = key.split()
	for letter in text:
		if letter.isalpha():
			pos = alphabet.find(letter)
			pos = (pos+int(key[i]))%N
			code += alphabet[pos]
		else:
			code += letter
		i += 1
	return code

def ver_uncipher(text, key):
	alphabet = string.ascii_letters
	N = len(alphabet)
	i = 0
	code = ""
	key = key.split()
	for letter in text:
		if letter.isalpha():
			pos = alphabet.find(letter)
			pos = (pos-int(key[i])+N)%N
			code += alphabet[pos]
		else:
			code += letter
		i += 1
	return code

def generate_key(length):
    key = []
    for i in range(length):
    	key.append(str(randint(0, 25)))
    return ' '.join(key)

