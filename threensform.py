import vigenere
import generator
import utility

def transpose(string):
    new_string = "".append(string[4]).append(string[0]).append(string[5]).append(string[1]).append(string[6]).append(string[2]).append(string[7]).append(string[3])
    return new_string

def trigram_substitution(trigram, key, encrypt):
    table = generate_ngram_substitution_table(3, make_seed(key), encrypt)

    new_trigram = table[trigram]

    return trigram

def threensform(string, key, iter, encrypt):
        if(i%2 == 0):
            phase_one(string, key, encrypt)
        else:
            phase_two(string, key, encrypt)

def phase_one(string, key, encrypt):
    string = transpose(string)
    caesar_string(string, key, encrypt)

def phase_two(string, key, encrypt):
    left, right = split_block(string, size=6)

    left = extended_vigenere_cipher(left, right, encrypt)
    left = trigram_substitution(trigram, key, encrypt)
    right = extended_vigenere_cipher(right, left, encrypt)
    right = trigram_substitution(trigram, key, encrypt)
