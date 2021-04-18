import string
import typing
from AbstractCipher import Cipher


class Caesar(Cipher):
	@staticmethod
	def make_ceasar_dict(shift: int) -> dict:
		eng_from = string.ascii_letters
		shift %= len(eng_from)
		eng_to = eng_from[shift:] + eng_from[:shift]
		return dict(zip(eng_from, eng_to))

	@staticmethod
	def make_inversed_caesar_dict(shift: int) -> dict:
		eng_from = string.ascii_lowercase+string.ascii_uppercase
		shift %= len(eng_from)
		eng_to = eng_from[shift:] + eng_from[:shift]
		return dict(zip(eng_to, eng_from))

	def crypt(self, text: str) -> str:
		key = self.get_caesar_key()
		out = ""
		transform = self.make_ceasar_dict(key)
		for letter in text:
			if letter.isalpha():
				out += transform[letter]
			else:
				out += letter
		return out

	def decrypt(self, text: str) -> str:
		key = self.get_caesar_key()
		out = ""
		transform = self.make_inversed_caesar_dict(key)
		for letter in text:
			if letter.isalpha():
				out += transform[letter]
			else:
				out += letter
		return out

	@staticmethod
	def get_caesar_key() -> int:
		correct_key = False
		key = None
		while not correct_key:
			input_key = input("Enter password: ")
			if any(not key.isdigit() for key in input_key):
				print("Incorrect key!")
			else:
				key = int(input_key)
				correct_key = True
		return key




