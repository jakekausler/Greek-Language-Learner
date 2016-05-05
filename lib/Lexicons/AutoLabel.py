# -*- coding: utf-8 -*-
'''
Created on Apr 29, 2014

@author: Jake
'''

import re

#Automatically label duplicate words
def autoLabel(oldFile,newFile,regex=r'n[123][a-h]\t\t'):
    of = open(oldFile)
    nf = open(newFile,'r+')
    d = {}
    wordMatch = regex
    lines = of.readlines()
    for line in lines:
        if re.match(wordMatch,line):
            d[line[line.find('\t')+2:-1]] = line[:line.find('\t')]
    headingMatch = r'^[A-Za-z][A-Za-z][^\t]'
    subHeadingMatch = r'\t[A-Za-z][A-za-z]'
    emptySubHeadingMatch = r'\t\n'
    emptyWordMatch = r'\t\t'
    s = ''
    count = 0
    for line in lines:
        if re.match(headingMatch,line):
            s += line
        elif re.match(subHeadingMatch,line):
            s += line
        elif re.match(emptySubHeadingMatch,line):
            s += line
        elif re.match(wordMatch,line):
            s += line
        elif re.match(emptyWordMatch,line):
            if line[2:-1] in d:
                s += '' + d[line[2:-1]] + line
#             elif line[2:-1] in ['ἅλας','κέρας','πέρας','τέρας']:
#                 s += '' + 'n3c' + line
#             elif line[2:-1] in ['ὕδωρ','ὄvap','φρέαρ','φῶς','οὖς','γάλα','γόνυ','μέλι','κρέας','ἱμάς','Κρήσκης','Πούδης','Κλήμης','ὀδούς','χάρις']:
#                 s += '' + 'n3c' + line
#             elif line[2:-1] in ['ἀλαζών','Ἀπολλῦων','ἀρχιποίμην','ἀρχιτέκτων','βραχίων','γείτων','δαίμων','εἰκών','ἡγεμών','Ἰσάων','κανών','λιμήν','Μακεδών','ποιμήν','σιαγών','σινδών','τέκτων','τρυγών','Φιλήμων','φπήν','χαλκηδών','χιών','ἀρήν','ἀρνός','κυων','ἀνήρ','γαστήρ','θυγάτηρ','μήτηρ','πατήρ']:
#                 s += '' + 'n3f' + line
#             elif line[2:-1] in ['Ἀκύλας','Γολγοθᾶ','Ζηνάς','Ζεύς','Θυάτειρα','Θυάτιρα','Ἰησοῦς','Λευίς','Λύδδα','Λύστρα','Μωσῆς','Μωϋσῆς']:
#                 s += '' + 'n3g' + line
            else:
                s += line
                count += 1
#    for key in d:
#        nf.write(key + ': ' + d[key] + '\n')
    nf.write(str(count) + '\n' + s)
    of.close()
    nf.close()
    
def countWords(file):
    f = open(file)
    count = 0
    for line in f:
        if re.match(r'.*\t\t',line):
            count += 1
    f.close()
    return count

def label(of,nf,df):
    old = open(of)
    new = open(nf,'r+')
    dictf = open(df)
    d = {}
    for line in dictf:
        d[line[:line.find('\t')]] = line[line.find('\t')+1:-1]
    s = ''
    headingMatch = r'^[A-Za-z][A-Za-z][^\t]'
    subHeadingMatch = r'\t[A-Za-z][A-za-z]'
    emptySubHeadingMatch = r'\t\n'
    emptyWordMatch = r'\t\t'
    for line in old:
        if re.match(headingMatch,line):
            s += line
        elif re.match(subHeadingMatch,line):
            s += line
        elif re.match(emptySubHeadingMatch,line):
            s += line
        elif re.match(r'[a-z][a-z]*[0-9][a-z]*\t\t',line):
            s += line
        elif re.match(emptyWordMatch,line):
            if line[2:-1] in d:
                entry = d[line[2:-1]]
                if entry.find(',') != -1:
                    s += entry[:entry.find(',')] + line
                    entry = entry[entry.find(',')+1:]
                    if entry.find(',') != -1:
                        s += entry[:entry.find(',')] + line
                        entry = entry[entry.find(',')+1:]
                    else:
                        s += entry + line
                else:
                    s += entry + line
    new.write(s)
    new.close()
    old.close()              
            
def makeDict(file):
    f = open(file)
    d = {}
    for line in f:
        if line[:line.find('\t')] in d.keys():
            d[line[:line.find('\t')]] = d[line[:line.find('\t')]] + ',' + line[line.find('\t')+1:-1]
        else:
            d[line[:line.find('\t')]] = line[line.find('\t')+1:-1]
    f.close()
    return d

f = open('PreFiles/labeledWords','r+')
s = ''
d = makeDict('PreFiles/pre-format')
for key in d:
    if isinstance(d[key],list):
        s += key + str(d[key]) + '\n'
    else:
        s += key + '\t' + d[key] + '\n'
f.write(s)
f.close()

label('conjunctions','PreFiles/blanks2','PreFiles/labeledWords')
#autoLabel('nouns','PreFiles/labeledWords',r'n[123][a-h]\t\t')

n=countWords('nouns')
print 'Nouns: ' + str(n)
v=countWords('verbs')
print 'Verbs: ' + str(v)
j=countWords('adjectives')
print 'Adjectives: ' + str(j)
d=countWords('adverbs')
print 'Adverbs: ' + str(d)
p=countWords('prepositions')
print 'Prepositions: ' + str(p)
o=countWords('pronouns')
print 'Pronouns: ' + str(o)
c=countWords('conjunctions')
print 'Conjunctions: ' + str(c)
i=countWords('interjections')
print 'Interjections: ' + str(i)
u=countWords('numerals')
print 'Numerals: ' + str(u)
r=countWords('particles')
print 'Particles: ' + str(r)
print
np=countWords('nounphrases')
print 'Noun Phrases: ' + str(np)
pp=countWords('prepositionalphrases')
print 'Prepositional Phrases: ' + str(pp)
print
print 'Total: ' + str(j+d+c+i+np+n+u+r+pp+p+o+v)