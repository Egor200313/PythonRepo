import string
from AbstractCipher import Cipher


class Caesar(Cipher):

	def __init__(self):
		key = self.get_caesar_key()
		self.crypt_dict = self.make_ceasar_dict(key)
		self.decrypt_dict = self.make_inversed_caesar_dict(key)

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

	def change_text(self, command: str, text: str) -> str:
		out = ""
		if command == "crypt":
			cur_dict = self.crypt_dict
		else:
			cur_dict = self.decrypt_dict
		for letter in text:
			if letter.isalpha():
				out += cur_dict[letter]
			else:
				out += letter
		return out

	def crypt(self, text: str) -> str:
		return self.change_text("crypt", text)

	def decrypt(self, text: str) -> str:
		return self.change_text("decrypt", text)

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




