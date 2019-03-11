from generator import *

table_file = open('table.txt', 'wb')

table = generate_ngram_substitution_table(3)
table = '\n'.join(table)
table_file.write(table.encode('utf-8'))