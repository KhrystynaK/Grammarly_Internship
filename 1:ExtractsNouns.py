'''
From WordNet extracts all nouns
and writes them into a new txt file
'''

import nltk
from nltk.corpus import wordnet as wn
my_file=open('English_nouns.txt','a')
for synset in list(wn.all_synsets('n')):
    my_file.write(synset.name()[:-5]+"\n")
my_file.close()
