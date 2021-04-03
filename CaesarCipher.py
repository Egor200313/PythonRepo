import string
def make_ceasar_dict(shift):
	eng_from = string.ascii_lowercase+string.ascii_uppercase
	shift %= len(eng_from)
	eng_to = eng_from[shift:]+eng_from[:shift]
	return dict(zip(eng_from, eng_to))

def make_reversed_caesar_dict(shift):
	eng_from = string.ascii_lowercase+string.ascii_uppercase
	shift %= len(eng_from)
	eng_to = eng_from[shift:]+eng_from[:shift]
	return dict(zip(eng_to, eng_from))

def caesar_cipher(text, key):
	out = ""
	transform = make_ceasar_dict(key)
	print(transform)
	for letter in text:
		#print(letter)
		if letter.isalpha():
			#print(letter, transform[letter])
			out += transform[letter]
		else:
			out += letter
	return out

def caesar_uncipher(text, key):
	out = ""
	transform = make_reversed_caesar_dict(key)
	for letter in text:
		if letter.isalpha():
			#print(letter, transform[letter])
			out += transform[letter]
		else:
			out += letter
	return out

def get_caesar_key():
    correct_key = False
    while not correct_key:
        key = int(input("Enter password: "))
        if not key.isdigit():
            key = int(input("Enter password: "))
        else:
            correct_key= True
    
    return key




