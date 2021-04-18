import argparse
from breaker import break_caesar
from CaesarCipher import Caesar
from VernamCipher import Vernam
from VigenereCipher import Vigenere


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_from", help='Path to input file')
    parser.add_argument("path_to", help='Path to output file')

    parser.add_argument("-c", "--cipher", help="type of cipher", required=True)
    parser.add_argument("-a", "--action", help="what to do", required=True)

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
    else:
        print("cipher not found")

    with open(path, errors='ignore') as f:
        all_text = f.readlines()
        text = ''.join(all_text)

    output = ""
    if args.action == "crypt":
        output = cip.crypt(text)
    elif args.action == "decrypt":
        output = cip.decrypt(text)
    elif args.action == "break" and args.cipher == "caesar":
        output = break_caesar(text)
    else:
        print("command not found")

    with open(result_file, "w") as out:
        out.write(output)


if __name__ == "__main__":
    main()
