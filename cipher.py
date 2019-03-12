import utility
import vigenere
import threensform
import math


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
        key = external_key[i]
        if encrypt:
            right_half = cipher_function(right_half, key, i, encrypt)
            left_half = string_xor(left_half, right_half)
        else:
            left_half = cipher_function(left_half, key, i, encrypt)
            left_half = string_xor(left_half, right_half)

        temp = right_half
        right_half = left_half
        left_half = temp

    return utility.join_block_halves(left_half, right_half)

def block_cipher(text, external_key, cipher_function, block_length=12, iters=12, mode=1, encrypt=True):
    block_count = math.ceil(1.0*len(text)/block_length)
    i = 0
    new_text = ""

    feedback = [0 for i in range(block_length)]
    while i < block_count:
        block = text[(i*block_length):((i+1)*block_length)]
        if (mode == 2 and i > 0):
            block = string_xor(block, feedback)
        new_block = feistel(block, external_key, cipher_function, iters, mode, encrypt)
        new_text = new_text + new_block
        i += 1

        if (mode == 2):
            feedback = new_block

    return new_text