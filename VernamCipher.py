from random import randint
import string
from AbstractCipher import Cipher


class Vernam(Cipher):
    def crypt(self, text):
        key = self.generate_key(len(text))
        print("Your unique key is: ", key)
        alphabet = string.ascii_letters
        n = len(alphabet)
        i = 0
        code = ""
        key = key.split()
        for letter in text:
            if not letter.isalpha():
                code += letter
                i += 1
                continue
            pos = alphabet.find(letter)
            pos = (pos + int(key[i])) % n
            code += alphabet[pos]
            i += 1
        return code

    def decrypt(self, text):
        key = self.get_key(len(text))
        alphabet = string.ascii_letters
        n = len(alphabet)
        i = 0
        code = ""
        for letter in text:
            if not letter.isalpha():
                code += letter
                i += 1
                continue
            pos = alphabet.find(letter)
            pos = (pos - int(key[i]) + n) % n
            code += alphabet[pos]
            i += 1
        return code

    @staticmethod
    def generate_key(length):
        n = len(string.ascii_letters)
        key = []
        for i in range(length):
            key.append(str(randint(0, n)))
        return ' '.join(key)

    @staticmethod
    def get_key(length):
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

