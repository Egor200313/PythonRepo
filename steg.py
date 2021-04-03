import os
import sys


def crypt(img_name, input_file_name, output_img_name):
	img_size = os.stat(img_name).st_size
	text_size = os.stat(input_file_name).st_size
	degree = int(input("Enter degree(1/2/4/8): "))
	if (text_size >= img_size * degree / 8 - 54):
		print("Text is too long!")
		return

	img_bmp = open(img_name, "rb")
	edited_bmp = open(output_img_name, "wb")
	source_file = open(input_file_name, "r", errors='ignore')
	message = source_file.readlines()
	message = ''.join(message)

	first54 = img_bmp.read(54)
	edited_bmp.write(first54)


	img_mask = (255<<degree)%256
	text_mask = 3<<(8-degree)


	for symbol in message:
		symbol = ord(symbol)
		for chunks in range(0, 8, degree):#write one symbol from message to img
			img_byte = int.from_bytes(img_bmp.read(1), sys.byteorder) & img_mask
			bits = symbol & text_mask
			bits >>= (8-degree)

			img_byte |= bits

			edited_bmp.write(img_byte.to_bytes(1, sys.byteorder))
			symbol <<= degree
	edited_bmp.write(img_bmp.read())

	source_file.close()
	img_bmp.close()
	edited_bmp.close()

def decrypt(img_name, output_file_name):
	img = open(img_name, "rb")
	output_file = open(output_file_name, "w")

	degree = int(input("Enter degree(1/2/4/8): "))
	img_mask = 2**degree - 1
	symb_number = int(input("Enter legnth: "))
	img.seek(54)

	for i in range(symb_number):
		cur_symb = 0
		for chunks in range(0, 8, degree):#write one symbol from message to img
			img_byte = int.from_bytes(img.read(1), sys.byteorder) & img_mask
			cur_symb<<=degree
			cur_symb |= img_byte
		output_file.write(chr(cur_symb))

	img.close()
	output_file.close()

command = sys.argv[1]
if command=="crypt":
	img_name = input("Enter full img name: ")
	input_file = input("Enter full text file name: ")
	output_img = input("Enter output img name: ")
	crypt(img_name, input_file, output_img)
elif command=="decrypt":
	img_name = input("Enter full img name: ")
	output_text = input("Enter output file name: ")
	decrypt(img_name, output_text)
else:
	print("command not found")






























