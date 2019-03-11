import cipher
import threensform
import IO

def main():
	encrypt = request_mode()
	if encrypt:
		text = request_plaintext()
	else:
		text = request_ciphertext()

	#coba buat mode ECB

	external_key = request_key()
	block_count = len(text)/12
	i = 0
	new_text = ""

	while i < block_count:
		block = text[(i*12):((i+1)*12)]
		new_block = feistel(block, threensform, 16, True)
		new_text = new_text + new_block

	if encrypt:
		output_ciphertext(text)
	else:
		output_plaintext(text)

if __name__ == "__main__":
	main()