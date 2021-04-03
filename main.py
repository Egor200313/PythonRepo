import sys
import string
from collections import Counter
from breaker import *
from CaesarCipher import *
from VigenereCipher import *
from VernamCipher import *

path = sys.argv[1]
command = sys.argv[2]
result_file = sys.argv[3]


def compare(text1, text2):
    i = 0
    correct = 0
    for letter in text1:
        if letter == text2[i]:
            correct += 1
        i += 1
    print((correct/i)*100, '%')


with open(path, errors='ignore') as f:
    all = f.readlines()
    text = ''.join(all)
    correct_key = False
    if command == "-C":
        key = get_caesar_key("caesar")
        output = caesar_cipher(text, key)
        
    if command == "-CE":
        key = get_caesar_key("caesar")
        output = caesar_uncipher(text, key)

    if command == "-CH":
        output = break_caesar(text)

    if command == "-V":
        key = get_vig_key(text)
        output = vig_cipher(text, key)

    if command == "-VE":
        key = get_vig_key(text)
        output = vig_uncipher(text, key)

    if command == "-Ver":
        key = generate_key(len(text))
        print("Your random key: ", key)
        output = ver_cipher(text, key)

    if command == "-VerE":
        key = input("Enter password: ")
        output = ver_uncipher(text, key)

    #ff = open("text.txt", "r", errors='ignore')
    #txt = ff.readlines()
    #txt = ''.join(txt)
    #print(len(txt), len(output))
    #compare(txt, output)
    out = open(result_file, "w")
    out.write(output)
    out.close()