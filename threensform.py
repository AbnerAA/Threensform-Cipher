import vigenere
import generator
import utility

def transpose(string, encrypt):
    if(encrypt):
        new_string = string[3] + string[0] + string[4] + string[1] + string[5] + string[2]
    else:
        new_string = string[1] + string[3] + string[5] + string[0] + string[2] + string[4]
    return new_string

def trigram_substitution(trigram, key, encrypt):
    table = utility.read_table(utility.make_seed(key))

    new_trigram = table[trigram]

    return new_trigram

def threensform(string, key, iter_counter, encrypt=True):
    if(iter_counter%2 == 0):
        result = phase_one(string, key, encrypt)
    else:
        result = phase_two(string, key, encrypt)
    return result

def phase_one(string, key, encrypt):
    if encrypt:
        #print("Before transpose: {}".format(string))
        new_string = transpose(string, encrypt)
        #print("After transpose: {}".format(new_string))
        new_string = vigenere.caesar_string(new_string, key, encrypt)
        #print("After caesar: {}".format(new_string))
    else:
        #print("Before caesar: {}".format(string))
        new_string = vigenere.caesar_string(string, key, encrypt)
        #print("After caesar: {}".format(new_string))
        new_string = transpose(new_string, encrypt)
        #print("After transpose: {}".format(new_string))

    return new_string


def phase_two(string, key, encrypt):
    left, right = utility.split_block(string, size=6)

    if encrypt:
        #print("Left before vigenere: {}".format(left))
        left = vigenere.extended_vigenere_cipher(left, right, encrypt)
        #print("Left after vigenere: {}".format(left))
        left = trigram_substitution(left, key, encrypt)
        right = vigenere.extended_vigenere_cipher(right, left, encrypt)
        right = trigram_substitution(right, key, encrypt)
    else:
        right = trigram_substitution(right, key, encrypt)
        right = vigenere.extended_vigenere_cipher(right, left, encrypt)
        left = trigram_substitution(left, key, encrypt)
        #print("Left before vigenere: {}".format(left))
        left = vigenere.extended_vigenere_cipher(left, right, encrypt)
        #print("Left after vigenere: {}".format(left))

    return utility.join_block_halves(left, right)