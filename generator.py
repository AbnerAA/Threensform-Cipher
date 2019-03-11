import random

import itertools
import string

def ascii_chars():
    """Generates a string containing all extended ASCII chars"""
    ascii_chars = list(map(chr, range(256)))
    return ''.join(ascii_chars)


def generate_all_strings(length):
    """Generates all strings of length `length`"""
    alphabet = ascii_chars()

    ngrams = itertools.product(alphabet, repeat=length)
    ngrams = [''.join(ngram_tuple) for ngram_tuple in ngrams]

    return ngrams


def generate_ngram_substitution_table(n, seed, encrypt):
    """Generate substitution table for ngrams of length n"""
    permutations = generate_all_strings(n)
    map_target = permutations[:]
    random.seed(seed)
    random.shuffle(map_target)

    if(encrypt):
    	ngram_pairs = zip(permutations, map_target)
    else:
    	ngram_pairs = zip(map_target, permutations)
    table = {key: value for key, value in ngram_pairs}
    return table