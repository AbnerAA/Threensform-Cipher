import cipher
import threensform

def main():
	filename = input("file : ")
	keyfile = input("key file : ")
	output_file = "output.txt"

	#coba buat mode ECB

	kf = open(keyfile, 'rb')
	external_key = kf.read()

	with open(filename, 'rb') as f:
		while True:
			block = retrieve_block(f)
			if not block:
				break
			cipher_function(block, external_key)

if __name__ == "__main__":
	main()