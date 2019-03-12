import cipher
import threensform
import IO
import generator
import math

block_length = 12
iterations = 12

def main():
	encrypt = IO.request_mode()
	if encrypt:
		text = IO.request_plaintext()
	else:
		text = IO.request_ciphertext()

	mode = IO.request_feistel_mode()

	#coba buat mode ECB

	external_key = IO.request_key()

	print("Generating tables...")
	if(mode <= 2):
		trigram_tables = generator.initiate_tables(3, external_key, encrypt)
	else:
		trigram_tables = generator.initiate_tables(3, external_key, True)
	print("Table generation finished.")

	new_text = cipher.block_cipher(text, external_key, trigram_tables, threensform.threensform, block_length, iterations, mode, encrypt)
	

	if encrypt:
		IO.output_ciphertext(new_text)
	else:
		IO.output_plaintext(new_text)

if __name__ == "__main__":
	main()