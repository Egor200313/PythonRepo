import string
from AbstractCipher import Cipher


class Vigenere(Cipher):
	@staticmethod
	def get_vig_key(length):
		correct_key = False
		key = ""
		while not correct_key:
			key = input("Enter password: ")
			try:
				key.encode('ascii')
			except UnicodeEncodeError:
				print("Not ascii string!")
				continue
			if length != len(key) or any(i.isdigit() for i in key):
				print("Password must be a string with the same length without digits!")
			else:
				correct_key = True
		return key

	def crypt(self, text):
		key = self.get_vig_key(len(text))
		alphabet = string.ascii_letters
		n = len(alphabet)
		out = ""
		i = 0
		for letter in text:
			if not letter.isalpha():
				out += letter
				continue
			pos1 = alphabet.find(letter)
			pos2 = alphabet.find(key[i])
			ind = (pos1+pos2) % n
			out += alphabet[ind]
			i += 1
		return out

	def decrypt(self, text):
		key = self.get_vig_key(text)
		alphabet = string.ascii_letters
		n = len(alphabet)
		out = ""
		i = 0
		for letter in text:
			if not letter.isalpha():
				out += letter
				continue
			pos1 = alphabet.find(letter)
			pos2 = alphabet.find(key[i])
			ind = (pos1 - pos2 + n) % n
			out += alphabet[ind]
			i += 1
		return out

