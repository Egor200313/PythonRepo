import argparse
from breaker import CaesarBreaker
from CaesarCipher import Caesar
from VernamCipher import Vernam
from VigenereCipher import Vigenere


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_from", help='Path to input file')
    parser.add_argument("path_to", help='Path to output file')

    parser.add_argument("-c", "--cipher", help="type of cipher", choices=["caesar", "vernam", "vigenere"], required=True)
    parser.add_argument("-a", "--action", help="what to do", choices=["crypt", "derypt", "break"], required=True)

    args = parser.parse_args()

    path = args.path_from
    result_file = args.path_to

    cip = None

    if args.cipher == "caesar":
        cip = Caesar()
    elif args.cipher == "vernam":
        cip = Vernam()
    elif args.cipher == "vigenere":
        cip = Vigenere()

    with open(path, errors='ignore') as f:
        all_text = f.readlines()
        text = ''.join(all_text)

    output = ""
    if args.action == "crypt":
        output = cip.crypt(text)
    elif args.action == "decrypt":
        output = cip.decrypt(text)
    elif args.action == "break" and args.cipher == "caesar":
        train_file = input("Enter full path to train file: ")
        with open(train_file) as f:
            train_text = f.readlines()
        train_text = ''.join(train_text)
        cb = CaesarBreaker(train_text)
        output = cb.break_caesar(text)
    else:
        print("Can break only caesar!")

    with open(result_file, "w") as out:
        out.write(output)


if __name__ == "__main__":
    main()
