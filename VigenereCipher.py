import string

def vig_cipher(text, key):
	alphabet = string.ascii_letters
	N = len(alphabet)
	out = ""
	i = 0
	for letter in text:
		if letter.isalpha():
			pos1 = alphabet.find(letter)
			pos2 = alphabet.find(key[i])
			ind = (pos1+pos2)%N
			out += alphabet[ind]
			i += 1
		else:
			out += letter
	return out

def vig_uncipher(text, key):
	alphabet = string.ascii_letters
	N = len(alphabet)
	out = ""
	i = 0
	for letter in text:
		if letter.isalpha():
			pos1 = alphabet.find(letter)
			pos2 = alphabet.find(key[i])
			ind = (pos1-pos2+N)%N
			out += alphabet[ind]
			i += 1
		else:
			out += letter
	return out

def get_vig_key(text):
    correct_key = False
    while not correct_key:
        key = input("Enter password: ")
        if len(text)!=len(key) or any(i.isdigit() for i in key):
            print("Password must be a string with the same length without digits!")
        else:
            correct_key = True
    return key