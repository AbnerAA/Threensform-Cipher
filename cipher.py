import utility
import vigenere
import threensform
import math

key_length = 12

def string_xor(string1, string2):
    char_pairs = zip(string1, string2)

    result_string = []

    for a, b in char_pairs:
        xor_result = chr(ord(a) ^ ord(b))
        result_string.append(xor_result)
    
    return ''.join(result_string)


def feistel(block, external_key, cipher_function, iters=12, mode=1, encrypt=True):
    left_half, right_half = utility.split_block(block)

    for i in range(iters):
        print(i)
        if encrypt:
            key = external_key[i]
            right_half = cipher_function(right_half, key, i, encrypt)
            left_half = string_xor(left_half, right_half)
        else:
            key = external_key[key_length-i-1]
            right_half = string_xor(right_half, left_half)
            left_half = cipher_function(left_half, key, i+1, encrypt)


        if(i < iters):
            temp = right_half
            right_half = left_half
            left_half = temp

    return utility.join_block_halves(left_half, right_half)

def block_cipher(text, external_key, cipher_function, block_length=12, iters=12, mode=1, encrypt=True):
    
    if mode == 1:
        new_text = block_cipher_ecb(text, external_key, cipher_function, block_length=12, iters=12, encrypt=True)
    elif mode == 2:
        new_text = block_cipher_cbc(text, external_key, cipher_function, block_length=12, iters=12, encrypt=True)
    elif mode == 3:
        new_text = block_cipher_cfb(text, external_key, cipher_function, block_length=12, iters=12, encrypt=True)
    elif mode == 4:
        new_text = block_cipher_ofb(text, external_key, cipher_function, block_length=12, iters=12, encrypt=True)
    elif mode == 5:
        new_text = block_cipher_counter(text, external_key, cipher_function, block_length=12, iters=12, encrypt=True)

    return new_text

def block_cipher_ecb(text, external_key, cipher_function, block_length=12, iters=12, encrypt=True):
    block_count = math.ceil(1.0*len(text)/block_length)
    i = 0
    new_text = ""

    while i < block_count:
        block = text[(i*block_length):((i+1)*block_length)]
        new_block = feistel(block, external_key, cipher_function, iters, mode, encrypt)
        new_text = new_text + new_block
        i += 1

    return new_text

def block_cipher_cbc(text, external_key, cipher_function, block_length=12, iters=12, encrypt=True):
    block_count = math.ceil(1.0*len(text)/block_length)
    i = 0
    new_text = ""

    #create IV from key
    seed = utility.make_seed(external_key)
    feedback = generator.generate_initial_value(block_length, seed)

    while i < block_count:
        block = text[(i*block_length):((i+1)*block_length)]

        if encrypt:
            block = string_xor(block, feedback)

        new_block = feistel(block, external_key, cipher_function, iters, mode, encrypt)
        i += 1

        if encrypt:
            feedback = new_block
        else:
            new_block = string_xor(new_block, feedback)
            feedback = block

        new_text = new_text + new_block

    return new_text

def block_cipher_cfb(text, external_key, cipher_function, block_length=12, iters=12, encrypt=True):
    block_count = math.ceil(1.0*len(text)/block_length)
    i = 0
    new_text = ""

    #create IV from key
    seed = utility.make_seed(external_key)
    feedback = generator.generate_initial_value(block_length, seed)

    while i < block_count:
        block = text[(i*block_length):((i+1)*block_length)]

        new_block = feistel(feedback, external_key, cipher_function, iters, mode, True)

        new_block = string_xor(block, new_block)

        if encrypt:
            feedback = new_block
        else:
            feedback = block

        new_text = new_text + new_block
        i += 1

    return new_text

def block_cipher_ofb(text, external_key, cipher_function, block_length=12, iters=12, encrypt=True):
    block_count = math.ceil(1.0*len(text)/block_length)
    i = 0
    new_text = ""

    #create IV from key
    seed = utility.make_seed(external_key)
    feedback = generator.generate_initial_value(block_length, seed)

    while i < block_count:
        block = text[(i*block_length):((i+1)*block_length)]
        feedback = feistel(feedback, external_key, cipher_function, iters, mode, True)
        new_block = string_xor(block, feedback)
        new_text = new_text + new_block
        i += 1

    return new_text

def block_cipher_counter(text, external_key, cipher_function, block_length=12, iters=12, encrypt=True):
    block_count = math.ceil(1.0*len(text)/block_length)
    i = 0
    new_text = ""

    #create IV from key
    seed = utility.make_seed(external_key)
    counter = generator.generate_initial_value(block_length, seed)

    while i < block_count:
        block = text[(i*block_length):((i+1)*block_length)]
        new_block = feistel(counter, external_key, cipher_function, iters, mode, True)
        new_block = string_xor(block, new_block)
        new_text = new_text + new_block
        i += 1
        counter += 1

    return new_text