from random import randint
import string
from AbstractCipher import Cipher


class Vernam(Cipher):
    def change_text(self, command: str, text: str):
        if command == "crypt":
            key = self.generate_key(len(text))
            print("Your unique key is: ", key)
        else:
            key = self.get_key(len(text))
        alphabet = string.ascii_letters
        n = len(alphabet)
        code = ""
        key = key.split()
        for i, letter in enumerate(text):
            if not letter.isalpha():
                code += letter
                continue
            pos = alphabet.find(letter)
            if command == "crypt":
                pos = (pos + int(key[i])) % n
            else:
                pos = (pos - int(key[i]) + n) % n

            code += alphabet[pos]
        return code

    def crypt(self, text: str) -> str:
        return self.change_text("crypt", text)

    def decrypt(self, text: str) -> str:
        return self.change_text("decrypt", text)

    @staticmethod
    def generate_key(length: int) -> str:
        n = len(string.ascii_lowercase)
        key = []
        for i in range(length):
            key.append(str(randint(0, n)))
        return ' '.join(key)

    @staticmethod
    def get_key(length: int) -> list:
        correct_key = False
        key = []
        while not correct_key:
            key = input("Enter password: ")
            arr = key.split()
            if length != len(arr) or any(not i.isdigit() for i in arr):
                print("Password must be a digits string with the same length!")
            else:
                key = [int(i) for i in arr]
                correct_key = True
        return key

