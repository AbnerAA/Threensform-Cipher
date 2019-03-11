import cipher
import threensform
import IO
import math

block_length = 12
iterations = 16

def main():
	encrypt = IO.request_mode()
	if encrypt:
		text = IO.request_plaintext()
	else:
		text = IO.request_ciphertext()

	#coba buat mode ECB

	external_key = IO.request_key()
	block_count = math.ceil(1.0*len(text)/block_length)
	i = 0
	new_text = ""

	while i < block_count:
		block = text[(i*block_length):((i+1)*block_length)]
		new_block = cipher.feistel(block, external_key, threensform.threensform, iterations, True)
		new_text = new_text + new_block
		print(new_block)

	if encrypt:
		IO.output_ciphertext(text)
	else:
		IO.output_plaintext(text)

if __name__ == "__main__":
	main()