import utility


def string_xor(string1, string2):
    char_pairs = zip(string1, string2)

    result_string = []

    for a, b in char_pairs:
        xor_result = chr(ord(a) ^ ord(b))
        result_string.append(xor_result)
    
    return ''.join(result_string)


def feistel(block, cipher_function, iters=16):
    left_half, right_half = utility.split_block(block)

    for _ in range(16):
        right_half = cipher_function(right_half)
        left_half = string_xor(left_half, right_half)

        temp = right_half
        right_half = left_half
        left_half = temp

    return utility.join_block_halves(left_half, right_half)