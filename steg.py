import argparse
import os
import sys


def input_generator(input_file_name: str, message: str):
	chunksize = 20
	if not input_file_name:
		for item in message:
			yield item
	else:
		with open(input_file_name, "r") as f:
			while True:
				chunk = f.read(chunksize)
				for item in chunk:
					yield item
				if not chunk:
					break


def crypt(img_name: str, input_file_name: str, output_img_name: str) -> None:
	img_size = os.stat(img_name).st_size
	message = ""
	if input_file_name:
		text_size = os.stat(input_file_name).st_size
	else:
		print("Enter your text")
		message = sys.stdin.read()
		text_size = len(message)

	degree = int(input("Enter degree(1/2/4/8): "))

	if text_size >= img_size * degree / 8 - 54:
		print("Text is too long!")
		return

	with open(img_name, "rb") as img_bmp, open(output_img_name, "wb") as edited_bmp:

		first54 = img_bmp.read(54)
		edited_bmp.write(first54)

		img_mask = (255 << degree) % 256
		text_mask = 3 << (8 - degree)

		for symbol in input_generator(input_file_name, message):
			symbol = ord(symbol)
			for chunks in range(0, 8, degree):  #write one symbol from message to img
				img_byte = int.from_bytes(img_bmp.read(1), sys.byteorder) & img_mask
				bits = symbol & text_mask
				bits >>= (8-degree)

				img_byte |= bits

				edited_bmp.write(img_byte.to_bytes(1, sys.byteorder))
				symbol <<= degree
		edited_bmp.write(img_bmp.read())


def decrypt(img_name: str, output_file_name: str) -> None:
	with open(img_name, "rb") as img, open(output_file_name, "w") as output_file:
		degree = int(input("Enter degree(1/2/4/8): "))
		img_mask = 2**degree - 1
		symb_number = int(input("Enter length: "))
		img.seek(54)

		for i in range(symb_number):
			cur_symb = 0
			for chunks in range(0, 8, degree):  #write one symbol from message to img
				img_byte = int.from_bytes(img.read(1), sys.byteorder) & img_mask
				cur_symb <<= degree
				cur_symb |= img_byte
			output_file.write(chr(cur_symb))


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("img_name", help="full input image name")
	parser.add_argument("outfile", help="full output file name")
	parser.add_argument("-a", "--action", help="what to do", choices=["crypt", "decrypt"], required=True)
	parser.add_argument("-i", "--inputfile", help="source text file")

	args = parser.parse_args()

	command = args.action
	img_name = args.img_name
	outputfile = args.outfile
	inputfile = args.inputfile
	if command == "crypt":
		crypt(img_name, inputfile, outputfile)
	elif command == "decrypt":
		decrypt(img_name, outputfile)


if __name__ == "__main__":
	main()
