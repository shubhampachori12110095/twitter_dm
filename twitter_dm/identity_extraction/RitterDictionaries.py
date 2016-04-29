import sys
import os
import string
import re
from collections import defaultdict
from glob import glob

def normalize(s):
    s = re.sub(r" 's", "'s", s)
    return re.sub(r'^the ', '', s.replace('.',''), re.IGNORECASE)

class Dictionaries:

    def __init__(self, dict_dir=None, list_of_files=None):
        self.word2dictionaries = defaultdict(set)
        self.dictionaries = []

        if dict_dir:
            list_of_files = glob(dict_dir)

        for fil in list_of_files:
            fil_basename = os.path.basename(fil)
            if re.search(r'.conf~?$', fil):       #Skip .conf files
                continue
            self.dictionaries.append(fil)
            for line in open(fil,'rU'):
                word = line.rstrip('\n')
                word = word.strip(' ').lower()
                word = normalize(word)
                self.word2dictionaries[word].add(fil_basename)
        print 'DICTS:', self.dictionaries

    def GetDictVector(self, word):
        if not word:
            return set()

        return self.word2dictionaries.get(word, set())