'''
Created on May 6, 2014

@author: Jake
'''

import collections, re

def buildUnifiedLexicon(nf,*files):
    d = {}
    for file in files:
        f = open(file)
        for line in f:
            if (line.startswith('\t\t')):
                if line[line.rfind('\t')+1:-1] not in d:
                    d[line[line.rfind('\t')+1:-1]] = line[2:line.rfind('\t\t')]
                elif d[line[line.rfind('\t')+1:-1]].find(line[2:line.rfind('\t\t')]) == -1:
                    d[line[line.rfind('\t')+1:-1]] = d[line[line.rfind('\t')+1:-1]] + ',' + line[2:line.rfind('\t\t')]
        f.close()
    n = open(nf,'r+')
    s = ''
    o = collections.OrderedDict(sorted(d.items()))
    for item in o:
        if re.match(r'^[^a-z]',item):
            s += item + '\t' + o[item] + '\n'
    n.write(s[:-1])
    n.close()

buildUnifiedLexicon('PreFiles/blanks2','adjectives','adverbs','conjunctions','interjections','nouns','numerals','particles','prepositions','pronouns','verbs')