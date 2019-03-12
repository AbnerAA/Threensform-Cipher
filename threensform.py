import vigenere
import generator
import utility

def transpose(string):
    new_string = string[3] + string[0] + string[4] + string[1] + string[5] + string[2]
    return new_string

def trigram_substitution(trigram, key, encrypt):
    table = generator.generate_ngram_substitution_table(3, utility.make_seed(key), encrypt)

    new_trigram = table[trigram]

    return new_trigram

def threensform(string, key, iter_counter, encrypt=True):
    if(iter_counter%2 == 0):
        print("Here")
        result = phase_one(string, key, encrypt)
        print("Result: {}".format(result))
    else:
        result = phase_two(string, key, encrypt)
    return result

def phase_one(string, key, encrypt):
    if encrypt:
        new_string = transpose(string)
        new_string = vigenere.caesar_string(new_string, key, encrypt)
    else:
        new_string = vigenere.caesar_string(string, key, encrypt)
        new_string = transpose(new_string)

    return new_string


def phase_two(string, key, encrypt):
    left, right = utility.split_block(string, size=6)

    if encrypt:
        print("Left before vigenere: {}".format(left))
        left = vigenere.extended_vigenere_cipher(left, right, encrypt)
        print("Left after vigenere: {}".format(left))
        left = trigram_substitution(left, key, encrypt)
        right = vigenere.extended_vigenere_cipher(right, left, encrypt)
        right = trigram_substitution(right, key, encrypt)
    else:
        right = trigram_substitution(right, key, encrypt)
        right = vigenere.extended_vigenere_cipher(right, left, encrypt)
        left = trigram_substitution(left, key, encrypt)
        print("Left before vigenere: {}".format(left))
        left = vigenere.extended_vigenere_cipher(left, right, encrypt)
        print("Left after vigenere: {}".format(left))

    return utility.join_block_halves(left, right)