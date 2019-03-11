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