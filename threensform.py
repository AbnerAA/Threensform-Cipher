import vigenere
import generator
import utility

def transpose(string):
    new_string = "".append(string[4]).append(string[0]).append(string[5]).append(string[1]).append(string[6]).append(string[2]).append(string[7]).append(string[3])
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
    string = transpose(string)
    return vigenere.caesar_string(string, key, encrypt)

def phase_two(string, key, encrypt):
    left, right = utility.split_block(string, size=6)

    print("Left before vigenere: {}".format(left))
    left = vigenere.extended_vigenere_cipher(left, right, encrypt)
    print("Left after vigenere: {}".format(left))
    left = trigram_substitution(left, key, encrypt)
    right = vigenere.extended_vigenere_cipher(right, left, encrypt)
    right = trigram_substitution(right, key, encrypt)

    return utility.join_block_halves(left, right)