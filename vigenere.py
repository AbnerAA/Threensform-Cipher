def ascii_to_num (char):
	#mengubah huruf ascii menjadi angka 0-255
	num = ord(char)
	return num

def num_to_ascii (num):
	#mengubah angka 0-255 menjadi ascii
	char = chr(num)
	return char

def extended_caesar_cipher (char, key, encrypt):
	num = ascii_to_num(char)
	key_num = ascii_to_num(key)
	if encrypt:
		num = (num + key_num) % 256
	else:
		num = (num - key_num) % 256
	new_char = num_to_ascii(num)
	return new_char

def caesar_string(string, key, encrypt):
	new_string = ""
	for i, char in enumerate(string):
		new_string = new_string + extended_caesar_cipher(char, key[i], encrypt)

	return new_string

def extended_vigenere_cipher(text, key, encrypt):
	new_text = ""
	n = len(key)
	for i, char in enumerate(text):
		i = i % n
		new_char = extended_caesar_cipher(char, key[i], encrypt)
		new_text = new_text + new_char

	return new_text