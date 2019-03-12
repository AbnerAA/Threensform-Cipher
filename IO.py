import pickle

def request_mode():
    print("Select mode :")
    print("1. Encrypt")
    print("2. Decrypt")
    input_mode = int(input("Select a number: "))

    if input_mode == 1:
        encrypt = True
    elif input_mode == 2:
        encrypt = False

    return encrypt

def request_feistel_mode():
    print("Select feistel mode :")
    print("1. ECB")
    print("2. CBC")
    print("3. CFB")
    print("4. OFB")
    print("5. Counter Mode")
    input_mode = int(input("Select a number: "))

    return input_mode

def request_key():
    print("Select key source:")
    print("1. File")
    print("2. Typed Message")
    input_mode = int(input("Select a number: "))

    if input_mode == 1:
        filename = input("Please enter the filename: ")
        input_file = open(filename, 'rb')
        external_key = input_file.read().decode()
    elif input_mode == 2:
        external_key = input("Please enter the key: ")

    return external_key

def request_plaintext():
    print("Select plaintext source:")
    print("1. File")
    print("2. Typed Message")
    input_mode = int(input("Select a number: "))

    if input_mode == 1:
        filename = input("Please enter the filename: ")
        input_file = open(filename, 'rb')
        message = input_file.read().decode()
    elif input_mode == 2:
        message = input("Please enter the plaintext: ")

    return message


def request_ciphertext():
    print("Select ciphertext source:")
    print("1. File")
    print("2. Typed Message")
    input_mode = int(input("Select a number: "))

    if input_mode == 1:
        filename = input("Please enter the filename: ")
        input_file = open(filename, 'rb')
        message = input_file.read().decode()
    elif input_mode == 2:
        message = input("Please enter the ciphertext: ")

    return message


def output_ciphertext(ciphertext):
    print("Select where to output ciphertext:")
    print("1. File")
    print("2. Terminal")
    output_mode = int(input("Select a number: "))

    if output_mode == 1:
        filename = input("Please enter the filename: ")
        input_file = open(filename, 'wb')
        input_file.write(ciphertext.encode('utf-8'))
    elif output_mode == 2:
        print(ciphertext)


def output_plaintext(plaintext):
    print("Select where to output plaintext:")
    print("1. File")
    print("2. Terminal")
    output_mode = int(input("Select a number: "))

    if output_mode == 1:
        filename = input("Please enter the filename: ")
        input_file = open(filename, 'wb')
        input_file.write(plaintext.encode('utf-8'))
    elif output_mode == 2:
        print(plaintext)

def request_seed():
    seed = input("Enter the seed to initialize the block cipher: ")

    seed = sum(map(ord, seed))

    return seed


def save_table(table):
    with open('table.pkl', 'wb') as table_file:
        pickle.dump(table, table_file, protocol=pickle.HIGHEST_PROTOCOL)


def load_table():
    with open('table.pkl', 'rb') as table_file:
        return pickle.load(table_file)