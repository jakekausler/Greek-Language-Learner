# -*- coding: utf-8 -*-
'''
Created on Oct 21, 2014

@author: Jake
'''

import SentenceGenerator
import SemanticSentenceGenerator2
import random
import sys

def makeVerbList(domain):
    '''
    Make a frequency dictionary of verbs of a given domain
    
    Keyword Arguments:
    domain -- domain to search
    '''
    f = open('../Semantics/lexicon')
    lines = f.readlines()
    f.close()
    lines = lines[lines.index('V\n'):]
    domainIndex = lines.index('\t'+domain+'\n')
    verbs = {}
    i = domainIndex+1
    cont = True
    while cont:
        if not lines[i].startswith('\t\t') or lines[i] == '\n':
            cont = False
        else:
            verbs[lines[i][2:lines[i].find(':')].replace('(','').replace(')','')] = int(lines[i][lines[i].find(':')+1:-1])
        i+=1
    return verbs

def makeNounList(domain):
    '''
    Make a frequency dictionary of nouns of a given domain
    
    Keyword Arguments:
    domain -- domain to search
    '''
    f = open('../Semantics/lexicon')
    lines = f.readlines()
    f.close()
    lines = lines[lines.index('N\n'):]
    domainIndex = lines.index('\t'+domain+'\n')
    nouns = {}
    i = domainIndex+1
    cont = True
    while cont:
        if not lines[i].startswith('\t\t') or lines[i] == '\n':
            cont = False
        else:
            nouns[lines[i][2:lines[i].find(':')].replace('(','').replace(')','')] = int(lines[i][lines[i].find(':')+1:-1])
        i+=1
    return nouns

def makeAdjectivesList(domain):
    '''
    Make a frequency dictionary of adjectives of a given domain
    
    Keyword Arguments:
    domain -- domain to search
    '''
    f = open('../Semantics/lexicon')
    lines = f.readlines()
    f.close()
    lines = lines[lines.index('A\n'):]
    domainIndex = lines.index('\t'+domain+'\n')
    adjectives = {}
    i = domainIndex+1
    cont = True
    while cont:
        if not lines[i].startswith('\t\t') or lines[i] == '\n':
            cont = False
        else:
            adjectives[lines[i][2:lines[i].find(':')].replace('(','').replace(')','')] = int(lines[i][lines[i].find(':')+1:-1])
        i+=1
    return adjectives

def makePronounsList(domain):
    '''
    Make a frequency dictionary of pronouns of a given domain.
    Determiners, because of the labelling sceme, are also found using
    this function
    
    Keyword Arguments:
    domain -- domain to search
    '''
    f = open('../Semantics/lexicon')
    lines = f.readlines()
    f.close()
    lines = lines[lines.index('R\n'):]
    domainIndex = lines.index('\t'+domain+'\n')
    pronouns = {}
    i = domainIndex+1
    cont = True
    while cont:
        if not lines[i].startswith('\t\t') or lines[i] == '\n':
            cont = False
        else:
            pronouns[lines[i][2:lines[i].find(':')].replace('(','').replace(')','')] = int(lines[i][lines[i].find(':')+1:-1])
        i+=1
    return pronouns

def makeAdverbList(domain):
    '''
    Make a frequency dictionary of adverbs of a given domain
    
    Keyword Arguments:
    domain -- domain to search
    '''
    f = open('../Semantics/lexicon')
    lines = f.readlines()
    f.close()
    lines = lines[lines.index('D\n'):]
    domainIndex = lines.index('\t'+domain+'\n')
    adverbs = {}
    i = domainIndex+1
    cont = True
    while cont:
        if not lines[i].startswith('\t\t') or lines[i] == '\n':
            cont = False
        else:
            adverbs[lines[i][2:lines[i].find(':')].replace('(','').replace(')','')] = int(lines[i][lines[i].find(':')+1:-1])
        i+=1
    return adverbs

def makeInterjectionList(domain):
    '''
    Make a frequency dictionary of interjections of a given domain
    
    Keyword Arguments:
    domain -- domain to search
    '''
    f = open('../Semantics/lexicon')
    lines = f.readlines()
    f.close()
    lines = lines[lines.index('I\n'):]
    domainIndex = lines.index('\t'+domain+'\n')
    interjections = {}
    i = domainIndex+1
    cont = True
    while cont:
        if not lines[i].startswith('\t\t') or lines[i] == '\n':
            cont = False
        else:
            interjections[lines[i][2:lines[i].find(':')].replace('(','').replace(')','')] = int(lines[i][lines[i].find(':')+1:-1])
        i+=1
    return interjections

def makeConjunctionList(domain):
    '''
    Make a frequency dictionary of conjunctions of a given domain
    
    Keyword Arguments:
    domain -- domain to search
    '''
    f = open('../Semantics/lexicon')
    lines = f.readlines()
    f.close()
    lines = lines[lines.index('C\n'):]
    domainIndex = lines.index('\t'+domain+'\n')
    conjunctions = {}
    i = domainIndex+1
    cont = True
    while cont:
        if not lines[i].startswith('\t\t') or lines[i] == '\n':
            cont = False
        else:
            conjunctions[lines[i][2:lines[i].find(':')].replace('(','').replace(')','')] = int(lines[i][lines[i].find(':')+1:-1])
        i+=1
    return conjunctions

def makePrepositionList(domain):
    '''
    Make a frequency dictionary of prepositions of a given domain
    
    Keyword Arguments:
    domain -- domain to search
    '''
    f = open('../Semantics/lexicon')
    lines = f.readlines()
    f.close()
    lines = lines[lines.index('P\n'):]
    domainIndex = lines.index('\t'+domain+'\n')
    prepositions = {}
    i = domainIndex+1
    cont = True
    while cont:
        if not lines[i].startswith('\t\t') or lines[i] == '\n':
            cont = False
        else:
            prepositions[lines[i][2:lines[i].find(':')].replace('(','').replace(')','')] = int(lines[i][lines[i].find(':')+1:-1])
        i+=1
    return prepositions

def makeParticleList(domain):
    '''
    Make a frequency dictionary of particles of a given domain
    
    Keyword Arguments:
    domain -- domain to search
    '''
    f = open('../Semantics/lexicon')
    lines = f.readlines()
    f.close()
    lines = lines[lines.index('X\n'):]
    domainIndex = lines.index('\t'+domain+'\n')
    particles = {}
    i = domainIndex+1
    cont = True
    while cont:
        if not lines[i].startswith('\t\t') or lines[i] == '\n':
            cont = False
        else:
            particles[lines[i][2:lines[i].find(':')].replace('(','').replace(')','')] = int(lines[i][lines[i].find(':')+1:-1])
        i+=1
    return particles

def makeNumberList(domain):
    '''
    Make a frequency dictionary of numbers of a given domain
    
    Keyword Arguments:
    domain -- domain to search
    '''
    f = open('../Semantics/lexicon')
    lines = f.readlines()
    f.close()
    numbers = {}
    while '\tNumber\n' in lines:
        lines = lines[lines.index('\tNumber\n')+1:]
        i = 0
        cont = True
        while cont:
            if not lines[i].startswith('\t\t') or lines[i] == '\n':
                cont = False
            else:
                if lines[i][2:lines[i].find(':')] in numbers.keys():
                    numbers[lines[i][2:lines[i].find(':')].replace('(','').replace(')','')] += int(lines[i][lines[i].find(':')+1:-1])
                else:
                    numbers[lines[i][2:lines[i].find(':')].replace('(','').replace(')','')] = int(lines[i][lines[i].find(':')+1:-1])
            i+=1
    return numbers

def getCFGFromFile(cfgFile='../Semantics/grammar.fcfg'):
    '''
    Creates a CFG from a given file.
    
    Keyword Arguments:
    cfgFile -- File from which to construct the cfg.
    '''
    cfg = SemanticSentenceGenerator2.CFG()
    cfg.constructGrammar(cfgFile)
    return cfg

def getSentenceModel(cfg,startSymbol='S',depth=100):
    '''
    Get a non-empty sentence model from a given cfg.
    
    Keyword Arguments:
    cfg -- the cfg object from which the sentence should be generated
    startSymbol -- The starting symbol of the grammar (default is 'S')
    depth -- Maximum recursive depth the grammar should go when
             constructing the sentence model. 
    '''
    model = cfg.genRandomSentenceConvergentFS(startSymbol,depth=depth)
    while model == None:
        model = cfg.genRandomSentenceConvergentFS(startSymbol,depth=depth)
    return model[0]

def fillSentenceModel(model):
    '''
    Supply a conjugated word for each word in the model
    
    Keyword Argument:
    model -- The sentence model to fill in
    '''
    sentence = []
    attribs = ['Case','Gender','Number','Person','Voice','Tense','Mood']
    map = {'Nominative':1,'Genitive':2,'Dative':3,'Accusative':4,'Vocative':5,
           'Masculine':1,'Feminine':2,'Neuter':3,
           'Singular':1,'Plural':2,
           'First':1,'Second':2,'Third':3,
           'Active':1,'Middle':2,'Passive':3,
           'Present':1,'Imperfect':2,'Aorist':3,'Future':4,'Perfect':5,'Pluperfect':8,
           'Indicative':1,'Subjunctive':2,'Optative':3,'Imperative':4,'Infinitive':5,'Participle':6}
    for word in model:
        pos = word[1:word.find('_')]
        word = word[word.find('=')+2:]
        domain = word[:word.find('\'')]
        word = word[word.find('\'')+1:]
        fs = {}
        while word[0] == ',':
            word = word[1:]
            for attr in attribs:
                if word.startswith(attr):
                    word = word[word.find('\'')+1:]
                    fs[attr] = word[:word.find('\'')]
                    word = word[word.find('\'')+1:]
        for f in fs.keys():
            fs[f] = map[fs[f]]
        for attr in attribs:
            if attr not in fs.keys():
                fs[attr] = 0
        if pos == 'adv':
            sentence.append(random.choice(makeAdverbList(domain).keys()))
        elif pos == 'noun':
            w = SentenceGenerator.formNoun(makeNounList(domain), number=fs['Number'], case=fs['Case'], gender=fs['Gender'])
            if w == None:
                return None
            else:
                sentence.append(w)
        elif pos == 'ptcl':
            sentence.append(random.choice(makeParticleList(domain).keys()))
        elif pos == 'det':
            w = SentenceGenerator.formDeterminer(makePronounsList(domain), number=fs['Number'], case=fs['Case'], gender=fs['Gender'])
            if w == None:
                return None
            else:
                sentence.append(w)
        elif pos == 'num':
            sentence.append(random.choice(makeNumberList(domain).keys()))
        elif pos == 'intj':
            sentence.append(random.choice(makeInterjectionList(domain).keys()))
        elif pos == 'pron':
            w = SentenceGenerator.formPronoun(makePronounsList(domain), number=fs['Number'], case=fs['Case'], gender=fs['Gender'])
            if w == None:
                return None
            else:
                sentence.append(w)
        elif pos == 'verb':
            w = SentenceGenerator.formVerb(makeVerbList(domain), number=fs['Number'], person=fs['Person'], mood=fs['Mood'], tense=fs['Tense'], voice=fs['Voice'], gender=fs['Gender'], case=fs['Case'])
            if w == None:
                return None
            else:
                sentence.append(w)
        elif pos == 'conj':
            sentence.append(random.choice(makeConjunctionList(domain).keys()))
        elif pos == 'adj':
            w = SentenceGenerator.formAdjective(makeAdjectivesList(domain), number=fs['Number'], case=fs['Case'], gender=fs['Gender'])
            if w == None:
                return None
            else:
                sentence.append(w)
        elif pos == 'prep':
            sentence.append(random.choice(makePrepositionList(domain).keys()))
    return sentence

def makeSentence(minimumLength=1,cfg=None):
    '''
    Return a sentence (list of words).
    
    Keyword Arguments:
    minimumLength -- The minimum number of words to be in the sentence
    cfg -- The cfg object to use when creating the sentence. Specifying
           one saves time
    '''
    if cfg == None:
        cfg = getCFGFromFile()
    s = fillSentenceModel(getSentenceModel(cfg))
    while s == None or len(s) < minimumLength:
        try:
            s = fillSentenceModel(getSentenceModel(cfg))
            i=0
            while s != None and i < len(s):
                if type(s[i]) == int:
                    s = None
                i+=1
        except IndexError:
            s = None
    return s

def makeSentences(numberToMake=1,minimumLength=1,grammarFile='../Semantics/grammar.fcfg',trace=False):
    '''
    Make a certain number of sentences, returned as a list of sentences
    
    Keyword Arguments:
    numberToMake -- Number of sentences to make
    minimumLength -- The minimum number of words to be in each sentence
    grammarFile -- Location of the grammar to use 
    '''
    sentences = []
    cfg = getCFGFromFile(grammarFile)
    for i in range(numberToMake):
        sentences.append(makeSentence(minimumLength,cfg))
        if trace:
            print i+1,'of',numberToMake
    return sentences

# def __init__():
#     n = sys.argv[1] if len(sys.argv) > 1 else 1
#     minLength = sys.argv[2] if len(sys.argv) > 2 else 5
#     retval = ''
#     sentences = makeSentences(n,minLength)
#     for s in sentences:
#         for w in s:
#             print w
#             retval += w + ' '
#         retval += '\n'
#     return retval