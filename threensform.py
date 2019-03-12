import vigenere
import generator
import utility

table_count = 6

def transpose(string, encrypt):
    if(encrypt):
        new_string = string[3] + string[0] + string[4] + string[1] + string[5] + string[2]
    else:
        new_string = string[1] + string[3] + string[5] + string[0] + string[2] + string[4]
    return new_string

def trigram_substitution(trigram, trigram_table, encrypt):
    new_trigram = trigram_table[trigram]

    return new_trigram

def threensform(string, key, trigram_tables, iter_counter, encrypt=True):
    if(iter_counter%2 == 0):
        result = phase_one(string, key, encrypt)
    else:
        if(encrypt):
            result = phase_two(string, key, trigram_tables[int(iter_counter/2)], encrypt)
        else:
            result = phase_two(string, key, trigram_tables[table_count - 1 - int(iter_counter/2)], encrypt)
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


def phase_two(string, key, trigram_table, encrypt):
    left, right = utility.split_block(string, size=6)

    if encrypt:
        print("Left before vigenere: {}".format(left))
        left = vigenere.extended_vigenere_cipher(left, right, encrypt)
        print("Left after vigenere: {}".format(left))
        left = trigram_substitution(left, trigram_table, encrypt)
        print("Left after trigram: {}".format(left))
        right = vigenere.extended_vigenere_cipher(right, left, encrypt)
        right = trigram_substitution(right, trigram_table, encrypt)
    else:
        right = trigram_substitution(right, trigram_table, encrypt)
        right = vigenere.extended_vigenere_cipher(right, left, encrypt)
        #print("Left before trigram: {}".format(left))
        left = trigram_substitution(left, trigram_table, encrypt)
        #print("Left before vigenere: {}".format(left))
        left = vigenere.extended_vigenere_cipher(left, right, encrypt)
        #print("Left after vigenere: {}".format(left))

    return utility.join_block_halves(left, right)