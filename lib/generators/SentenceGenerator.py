# -*- coding: utf-8 -*-
'''
Created on Jun 6, 2014

@author: Jake

Generate sentences based on a sentence model formed with the
SentenceFormer module, with words morphologically formed with the
Generator modules and chosen from the Lexicons.
'''

import random
import VerbGenerator
import NounGenerator
import AdjectiveGenerator
import DeterminerGenerator
import SentenceFormer
import PronounGenerator

def formVerb(potentialVerbs,weighted=False,number=0,person=0,mood=0,tense=0,voice=0,gender=0,case=0):
    '''Form a verb from given or random morphological features.
    
    Keyword arguments:
    potentialVerbs -- List of verbs to try
    weighted -- Whether or not to choose words with weighted random
                generation
    number -- Number of the verb (default is 0). 0 is random, 1 is
              singular, 2 is plural.
    person -- Person of the verb (default is 0). 0 is random, 1 is
              first, 2 is second, 3 is third
    mood -- Mood of the verb (default is 0). 0 is random, 1 is
            indicative, 2 is subjunctive, 3 is optative, 4 is
            imperative, 5 is infinitive, 6 is participle.
    tense -- Tense of the verb (default is 0). 0 is random, 1 is
             present, 2 is imperfect, 3 is aorist, 4 is
             future, 5 is perfect, 8 is pluperfect (had to restructure.
             That's the reason for the skip)
    voice -- Voice of the verb (default is 0). 0 is random, 1 is
             active, 2 is middle, 3 is passive.
    gender -- Gender of the verb (default is 0). 0 is random, 1 is
              masculine, 2 is feminine, 3 is neuter.
    case -- Case of the verb (default is 0). 1 is nominative, 2 is
            genitive, 3 is dative, 4 is accusative, 5 is vocative
            (only in singular).
    verb -- If specified, the verb to be chosen (default is None).
    '''
    
    # If morph features are random, choose their values. If not, make
    # sure they work. If they do not, make them work.
    if mood == 0:
        mood = random.randint(1,6)
    if number == 0:
        if mood == 5:
            number = 0
        else:
            number = random.randint(1,2)
    elif number != 0:
        if mood == 5:
            number = 0
    if person == 0:
        if mood == 5 or mood == 6:
            person = 0
        elif mood == 4:
            person = random.randint(2,3)
        else:
            person = random.randint(1,3)
    elif person != 0:
        if mood == 5 or mood == 6:
            person = 0
        elif mood == 4 and (person != 2 or person != 3):
            person = random.randint(2,3)
    if voice == 0:
        voice = random.randint(1,3)
    if tense == 0:
        if mood == 2 or mood == 4:
            tense = random.choice([1,3,5]) #Present aorist Perfect
        elif mood == 3:
            if voice == 3:
                tense = 3 #aorist
            else:
                tense = random.choice([1,3]) #present aorist
        elif mood == 5:
            if voice == 3:
                tense = random.choice([1,3,5]) #Present aorist Perfect
            else:
                tense = random.choice([1,3,4,5]) #Present future aorist Perfect
        elif mood == 6:
            tense = random.choice([1,3,4,5])#Present future aorist Perfect
        else:
            if voice == 3:
                tense = random.choice([1,2,3,4,5,8]) #any
            elif voice == 1:
                tense = random.choice([1,2,3,4,5,8]) #any
            else:
                tense = random.choice([1,2,3,4,5,8]) #any
    elif tense != 0:
        if mood == 2 and tense not in [1,4,5,6]:
            tense = random.choice([1,3,5])#Present aorist Perfect
        elif mood == 3 and voice == 3 and tense not in [4,5]:
            tense = 3 #aorist
        elif mood == 3 and tense not in [1,4,5]:
            tense = random.choice([1,3])#present aorist
        elif mood == 4 and tense not in [1,4,5,6]:
            tense = random.choice([1,3,5])#Present aorist Perfect
        elif mood == 5 and voice == 3 and tense not in [1,4,5,6]:
            tense = random.choice([1,3,5])#Present aorist Perfect
        elif mood == 5 and tense not in [1,3,4,5,6]:
            tense = random.choice([1,3,4,5])#Present future aorist Perfect
        elif mood == 6 and tense not in [1,3,4,5,6]:
            tense = random.choice([1,3,4,5])#Present future aorist Perfect
        elif mood == 1 and voice == 1 and tense == 9:
            tense = random.choice([1,2,3,4,5,8])#any
        elif mood == 1 and voice == 3 and (tense == 9 or tense == 7):
            tense = random.choice([1,2,3,4,5,8])#any
    if gender == 0:
        if mood == 6:
            gender = random.randint(1,3)
    if case == 0:
        if mood == 6:
            if number == 1:
                case = random.randint(1,5)
            else:
                case = random.randint(1,4)
    
    # Set a list of potential verbs, and choose a random verb from the
    # list until it can match all the features by using the
    # VerbGenerator. If all verbs in the list are tried and none work,
    # return None.
    v=0
    vb = chooseRandomWord(potentialVerbs,weighted)
    if vb == None:
        return None
    del potentialVerbs[vb]
    style=getStyle(vb,'verb')
    while style == None:
        vb = chooseRandomWord(potentialVerbs,weighted)
        if vb == None:
            return None
        del potentialVerbs[vb]
        style=getStyle(vb,'verb')
    verb = (vb,style)
    while v==0:
        if tense == 3: # aorist
            tense = VerbGenerator.whichAorist(vb) + 4 # recognize as first or second aorist
        elif tense == 4: # future
            t = VerbGenerator.whichPerfect(vb)
            if t == 1:
                tense = 3
            else:
                t = 9
        elif tense == 5: # perfect
            tense = VerbGenerator.whichPerfect(vb) + 5
        if mood == 1:
            if number != 0 and person != 0:
                if tense == 1:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ipa')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ipm')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ipp')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                elif tense == 2:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ima')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'imm')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'imp')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                elif tense == 3:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ifa')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ifm')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'if1p')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                elif tense == 9:
                    v = VerbGenerator.formTense(verb[0],verb[1],'if2p')
                    if v != 0:
                        return v[(number-1)*3+(person-1)]
                elif tense == 4:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ia1a')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ia1m')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ia1p')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                elif tense == 5:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ia2a')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ia2m')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ia2p')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                elif tense == 6:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ie1a')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'iem')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'iep')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                elif tense == 7:
                    v = VerbGenerator.formTense(verb[0],verb[1],'ie2a')
                    if v != 0:
                        return v[(number-1)*3+(person-1)]
                elif tense == 8:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ila')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ilm')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ilp')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
        elif mood == 2:
            if number != 0 and person != 0:
                if tense == 1:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'spa')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'spm')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'spp')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                elif tense == 4:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'sa1a')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'sa1m')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'sa1p')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                elif tense == 5:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'sa2a')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'sa2m')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'sa2p')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                elif tense == 6:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'sea')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'sem')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'sep')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
        elif mood == 3:
            if number != 0 and person != 0:
                if tense == 1:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'opa')
                        if v != 0:
                            return v[(number-1)*3+(person-1)] 
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'opm')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                elif tense == 4:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'oa1a')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'oa1m')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'oa1p')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                elif tense == 5:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'oa2a')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'oa2m')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'oa2p')
                        if v != 0:
                            return v[(number-1)*3+(person-1)]
        elif mood == 4:
            if number != 0 and person != 0:
                if tense == 1:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'mpa')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'mpm')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'mpp')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
                elif tense == 4:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ma1a')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ma1m')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ma1p')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
                elif tense == 5:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ma2a')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ma2m')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ma2p')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
                elif tense == 6:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'mea')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'mem')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'mep')
                        if v != 0:
                            return v[(number-1)*2+(person-2)]
        elif mood == 5:
            if tense == 1:
                if voice == 1:
                    v = VerbGenerator.formTense(verb[0],verb[1],'npa')
                    if v != 0:
                        return v
                elif voice == 2:
                    v = VerbGenerator.formTense(verb[0],verb[1],'npm')
                    if v != 0:
                        return v
                elif voice == 3:
                    v = VerbGenerator.formTense(verb[0],verb[1],'npp')
                    if v != 0:
                        return v
            elif tense == 3:
                if voice == 1:
                    v = VerbGenerator.formTense(verb[0],verb[1],'nfa')
                    if v != 0:
                        return v
                elif voice == 2:
                    v = VerbGenerator.formTense(verb[0],verb[1],'nfm')
                    if v != 0:
                        return v
            elif tense == 4:
                if voice == 1:
                    v = VerbGenerator.formTense(verb[0],verb[1],'na1a')
                    if v != 0:
                        return v
                elif voice == 2:
                    v = VerbGenerator.formTense(verb[0],verb[1],'na1m')
                    if v != 0:
                        return v
                elif voice == 3:
                    v = VerbGenerator.formTense(verb[0],verb[1],'na1p')
                    if v != 0:
                        return v
            elif tense == 5:
                if voice == 1:
                    v = VerbGenerator.formTense(verb[0],verb[1],'na2a')
                    if v != 0:
                        return v
                elif voice == 2:
                    v = VerbGenerator.formTense(verb[0],verb[1],'na2m')
                    if v != 0:
                        return v
                elif voice == 3:
                    v = VerbGenerator.formTense(verb[0],verb[1],'na2p')
                    if v != 0:
                        return v
            elif tense == 6:
                if voice == 1:
                    v = VerbGenerator.formTense(verb[0],verb[1],'nea')
                    if v != 0:
                        return v
                elif voice == 2:
                    v = VerbGenerator.formTense(verb[0],verb[1],'nem')
                    if v != 0:
                        return v
                elif voice == 3:
                    v = VerbGenerator.formTense(verb[0],verb[1],'nep')
                    if v != 0:
                        return v
        elif mood == 6:
            if case != 0 and number != 0 and gender != 0:
                if tense == 1:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ppa')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ppm')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'ppp')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                elif tense == 3:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pfa')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pfm')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pfp')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                elif tense == 4:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pa1a')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pa1m')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pa1p')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                elif tense == 5:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pa2a')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pa2m')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pa2p')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                elif tense == 6:
                    if voice == 1:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pea')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                    elif voice == 2:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pem')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
                    elif voice == 3:
                        v = VerbGenerator.formTense(verb[0],verb[1],'pep')
                        if v != 0:
                            return v[(number-1)*5+(case-1)+(gender-1)*9]
        if v==0:
            if len(potentialVerbs)-2 >= 0:
                vb = chooseRandomWord(potentialVerbs,weighted)
                if vb == None:
                    return None
                del potentialVerbs[vb]
                style=getStyle(vb,'verb')
                while style == None:
                    vb = chooseRandomWord(potentialVerbs,weighted)
                    if vb == None:
                        return None
                    del potentialVerbs[vb]
                    style=getStyle(vb,'verb')
                verb = (vb,style)
            else:
                return None

def formNoun(potentialNouns,weighted=False,number=0,case=0,gender=0):
    '''Form a noun from given or random morphological features.
    
    Keyword arguments:
    potentialVerbs -- List of nouns to try
    weighted -- Whether or not to choose words with weighted random
                generation
    number -- Number of the noun (default is 0). 0 is random, 1 is
              singular, 2 is plural.
    case -- Case of the noun (default is 0). 1 is nominative, 2 is
            genitive, 3 is dative, 4 is accusative, 5 is vocative
            (only in singular).
    gender -- Gender of the noun (default is 0). Only used in
              determining if a noun can be potentially chosen, not in
              actually forming the noun. 0 is random, 1 is masculine,
              2 is feminine, 3 is neuter.
    '''
    
    # Choose features for features marked random. Check if features
    # work. If they do not, choose new values.
    if number == 0:
        number = random.randint(1,2)
    if case == 0:
        if number == 1:
            case = random.randint(1,5)
        else:
            case = random.randint(1,4)
    elif case == 5:
        if number == 2:
            case = random.randint(1,4)
    if gender == 0:
        gender = random.randint(1,3)
        
    # Generate a list of potential nouns. Randomly choose a noun from
    # the list until the noun chosen works with the given features or
    # the list is exausted, in which case, return None. 
    nn = chooseRandomWord(potentialNouns,weighted)
    if nn == None:
        return None
    del potentialNouns[nn]
    style=getStyle(nn,'noun')
    while style == None:
        nn = chooseRandomWord(potentialNouns,weighted)
        if nn == None:
            return None
        del potentialNouns[nn]
        style=getStyle(nn,'noun')
    noun = (nn,style)
    n=0
    while n==0:
        n = NounGenerator.generateNounForms(noun[0],noun[1])
        if n != 0:
            retVal = n[(case-1)+(number-1)*5]
            return retVal
        else:
            if len(potentialNouns)-2 >= 0:
                nn = chooseRandomWord(potentialNouns,weighted)
                if nn == None:
                    return None
                del potentialNouns[nn]
                style=getStyle(nn,'noun')
                while style == None:
                    nn = chooseRandomWord(potentialNouns,weighted)
                    if nn == None:
                        return None
                    del potentialNouns[nn]
                    style=getStyle(nn,'noun')
                noun = (nn,style)
            else:
                return None
    
def formAdjective(potentialAdjectives,weighted=False,gender=0,number=0,case=0):
    '''Form an adjective from given or random morphological features.
    
    Keyword arguments:
    potentialVerbs -- List of adjectives to try
    weighted -- Whether or not to choose words with weighted random
                generation
    number -- Number of the adjective (default is 0). 0 is random, 1
              is singular, 2 is plural.
    case -- Case of the adjective (default is 0). 1 is nominative, 2
            is genitive, 3 is dative, 4 is accusative, 5 is vocative
            (only in singular).
    gender -- Gender of the adjective (default is 0). Only used in
              determining if an adjective can be potentially chosen,
              not in actually forming the adjective. 0 is random, 1 is
              masculine, 2 is feminine, 3 is neuter.
    '''
    
    # Choose features for features marked random. Check if features
    # work. If they do not, choose new values.
    if gender == 0:
        gender = random.randint(1,3)
    if number == 0:
        number = random.randint(1,2)
    if case == 0:
        if number == 1:
            case = random.randint(1,5)
        else:
            case = random.randint(1,4)
    elif case == 5:
        if number == 2:
            case = random.randint(1,4)
            
    # Generate a list of potential adjectives. Randomly choose an
    # adjective from the list until the adjective chosen works with
    # the given features or the list is exausted, in which case,
    # return None.
    aj = chooseRandomWord(potentialAdjectives,weighted)
    if aj == None:
        return None
    del potentialAdjectives[aj]
    style=getStyle(aj,'adjective')
    while style == None:
        aj = chooseRandomWord(potentialAdjectives,weighted)
        if aj == None:
            return None
        del potentialAdjectives[aj]
        style=getStyle(aj,'adjective')
    adjective = (aj,style)
    a=0
    while a==0:
        a = AdjectiveGenerator.generateAdjectiveForms(adjective[0],adjective[1])
        if a != 0:
            retVal = a[(number-1)*5+(case-1)+(gender-1)*9]
            return retVal
        else:
            if len(potentialAdjectives)-2 >= 0:
                aj = chooseRandomWord(potentialAdjectives,weighted)
                if aj == None:
                    return None
                del potentialAdjectives[aj]
                style=getStyle(aj,'adjective')
                while style == None:
                    aj = chooseRandomWord(potentialAdjectives,weighted)
                    if aj == None:
                        return None
                    del potentialAdjectives[aj]
                    style=getStyle(aj,'adjective')
                adjective = (aj,style)
            else:
                return None

def formDeterminer(potentialDeterminers,weighted=False,gender=0,number=0,case=0):
    '''Form a determiner from given or random morphological features.
    
    Keyword arguments:
    potentialVerbs -- List of determiners to try
    weighted -- Whether or not to choose words with weighted random
                generation
    number -- Number of the determiner (default is 0). 0 is random, 1
              is singular, 2 is plural.
    case -- Case of the determiner (default is 0). 1 is nominative, 2
            is genitive, 3 is dative, 4 is accusative, 5 is vocative
            (only in singular).
    gender -- Gender of the determiner (default is 0). Only used in
              determining if a determiner can be potentially chosen,
              not in actually forming the determiner. 0 is random, 1
              is masculine, 2 is feminine, 3 is neuter.
    '''
    
    # Choose features for features marked random. Check if features
    # work. If they do not, choose new values.
    if gender == 0:
        gender = random.randint(1,3)
    if number == 0:
        number = random.randint(1,2)
    if case == 0:
        if number == 1:
            case = random.randint(1,5)
        else:
            case = random.randint(1,4)
    elif case == 5:
        if number == 2:
            case = random.randint(1,4)
            
    # Generate a list of potential determiners. Randomly choose a
    # determiner from the list until the determiner chosen works with
    # the given features or the list is exausted, in which case,
    # return None.
    determiner = chooseRandomWord(potentialDeterminers,weighted)
    if determiner == None:
        return None
    del potentialDeterminers[determiner]
    d=0
    while d==0:
        d = DeterminerGenerator.generateDeterminerForms(determiner)
        if d != 0 and d != None:
            retVal = d[(number-1)*5+(case-1)+(gender-1)*9]
            if retVal != 0:
                return retVal
            else:
                d = 0
        else:
            if len(potentialDeterminers)-2 >= 0:
                determiner = chooseRandomWord(potentialDeterminers,weighted)
                if determiner == None:
                    return None
                del potentialDeterminers[determiner]
            else:
                return None

def formPronoun(potentialPronouns,weighted=False,gender=0,number=0,case=0):
    '''Form a pronoun from given or random morphological features.
    
    Keyword arguments:
    potentialVerbs -- List of pronouns to try
    weighted -- Whether or not to choose words with weighted random
                generation
    number -- Number of the pronoun (default is 0). 0 is random, 1 is
              singular, 2 is plural.
    case -- Case of the pronoun (default is 0). 1 is nominative, 2 is
            genitive, 3 is dative, 4 is accusative, 5 is vocative
            (only in singular).
    gender -- Gender of the pronoun (default is 0). Only used in
              determining if a pronoun can be potentially chosen, not
              in actually forming the pronoun. 0 is random, 1 is
              masculine, 2 is feminine, 3 is neuter.
    '''
    
    # Choose features for features marked random. Check if features
    # work. If they do not, choose new values.
    if gender == 0:
        gender = random.randint(1,3)
    if number == 0:
        number = random.randint(1,2)
    if case == 0:
        if number == 1:
            case = random.randint(1,5)
        else:
            case = random.randint(1,4)
            
    # Generate a list of potential pronouns. Randomly choose a pronoun
    # from the list until the pronoun chosen works with the given
    # features or the list is exausted, in which case, return None.
    pronoun = chooseRandomWord(potentialPronouns,weighted)
    if pronoun == None:
        return None
    del potentialPronouns[pronoun]
    p=0
    while p==0:
        p = PronounGenerator.generatePronounForms(pronoun,gender,number,case)
        if p != 0:
            return p
        else:
            if len(potentialPronouns)-2 >= 0:
                pronoun = chooseRandomWord(potentialPronouns,weighted)
                if pronoun == None:
                    return None
                del potentialPronouns[pronoun]
            else:
                return None

def chooseVerb():
    '''Build and return the dictionary of verbs and frequencies from the verb counts.'''
    
    #Open the verb lexicon, build the verb list, and return it.
    f = open('../sentenceLayouts/verbCounts')
    words = {}
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        if line != '':
            words[line[:line.find(':')]] = int(line[line.find(':')+1:])
    f.close()
    return words

def chooseNoun(gender=0):
    '''Build and return the dictionary of nouns and frequencies from the noun counts.
    
    Keyword arguments:
    gender -- The noun gender to search for.
    '''
    
    #Open the noun lexicon, build the noun list with nouns of the
    # specified gender (or all nouns if none is specified), and return
    # it.
    if gender == 0:
        gender = random.randint(1,3)
    f = open('../sentenceLayouts/nounCounts')
    words = {}
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        if line != '':
            if gender == 1 or line[:line.find(':')] in ['Ἀαρών','ἀββά','Ἀκελδαμάχ','ἁλληλουϊά','Ἁρμαγεδών','Ἀσά','Βοανηργές','Γαββαθᾶ','Γεθσημανί','Ἐλμωδάμ','ἐλωι','ἐφφαθά','ζαφθάνι','ηλι','Ἠλί','θάβιτα','Καπερναούμ','Καῦδα','Κλαῦδα','κορβᾶν','κοῦμ','κοῦμι','λαμα','λεμά','Μαγδαλά','Μαγεδών','Μαθθάτ','μαρὰν ἀθᾶ','μαράνα θᾶ','Ναθάν','Νεεμάν','Νευης','ῥαββί','ῥαββονί','ῥαββουνί','ῥαβιθά','ῥακά','ῥαχά','Ῥεμφάν','Ῥεφάν','σαβαχθάνι','Σαβαώθ','Σαμφουρειν','Σαρούχ','Σινά','Σιχάρ','Σιχέμ','Σκαριώτης','Συχέμ','ταλιθά','Χωραζίν','Ὠβήδ','ὡσαννά']:
                words[line[:line.find(':')]] = int(line[line.find(':')+1:])
            elif gender == 2:
                if line[:line.find(':')] in ['n1a','n1b','n1c','n2b'] or line[line.rfind('\t\t')+2:] in ['συκῆ','γῆ','Κῶς','λαῖλαψ','ἀλώπηξ','γυνή','ὄρνιξ','πίναξ','πλάξ','σάρξ','Φῆλιξ','Φοῖνιξ','χοῖνιξ','μάστιξ','πτέρυξ','σάλπιγξ','φάραγξ','φλόξ','θρίξ','ψίξ','ἁγιότης','ἁγνότης','ἀδελφότης','ἀδηλότης','ἁδρότης','αἰσχρότης','ἀκαθάρτης','ἁπλότης','ἀφελότης','βραδύτης','γυμνότης','ἑνότης','ἐσθής','εὐθύτης','θειότης','θεότης','ἱκανότης','ἱλαρότης','ἰσότης','καθαρότης','καινότης','κυριότης','λαμπρότης','ματαιότης','μεγαλειότης','νεότης','νύξ','ὁμοιότης','ὁσιότης','παλαιότης','πιότης','πλάνης','πραότης','πραΰτης','σεμνότης','σκληρότης','τελειότης','χάρις','χρηστότης','ἀκρίς','Ἀντιπατρίς','Ἄρτεμις','ἀσπίς','ἀτμίς','βολίς','Δάμαρις','δισμυριάς','Δορκάς','Ἑβραΐς','Ἑλλάς','ἐλπίς','ἔρις','Ἡρῳδιάς','θυρίς','ἴασπις','ἰκμάς','ἶρις','Ἰωσῆς','κεφαλίς','κλείς','λαμπάς','λεπίς','Λωΐς','μερίς','μοιχαλίς','μυριάς','νῆστις','παγίς','παῖς','παραστάτις','παροψίς','πατρίς','Περσίς','πινακίς','πορφυρόπωλις','πρεσβῦτις','προστάτις','προφῆτις','Πτολεμαΐς','ῥαφίς','ῥυτίς','Σαμαρῖτις','σανίς','σπιλάς','σπυρίς','στιβάς','στοιβάς','συγγενίς','σφραγίς','Τιβεριάς','Τραχωνῖτις','Τρῳάς','ὑπολαμπάς','χιλιάς','χλαμύς','ὄρνις','ἰσχύς','ὀσφῦς','ὀφρῦς','ὗς','ναῦς','νῆστις','ἀγαλλίασις','ἀγανάκτησις','ἀθέτησις','ἄθλησις','αἴνεσις','αἵρεσις','αἴσθησις','ἅλυσις','ἅλωσις','Ἀμφίπολις','ἀνάβλεψις','ἀνάγνωσις','ἀνάδειξις','ἀναίρεσις','ἀνακαίνωσις','ἀνάκρισις','ἀνάλημψις','ἀνάλυσις','ἀνάμνησις','ἀνάπαυσις','ἀνάστασις','ἀνάχυσις','ἀνάψυξις','ἄνεσις','ἄνοιξις','ἀνταπόδοσις','ἀντίθεσις','ἀντίλημψις','ἀπάντησις','ἀπέκδυσις','ἀπόδειξις','ἀπόθεσις','ἀποκάλυψις','ἀποκατάστασις','ἀπόκρισις','ἀπόλαυσις','ἀπολύτρωσις','ἀπόχρησις','αὔξησις','ἄφεσις','ἄφιξις','βάσις','βεβαίωσις','βίωσις','βρῶσις','γένεσις','γέννησις','γνῶσις','δάμαλις','δέησις','Δεκάπολις','δέρρις','διάγνωσις','διαίρεσις','διάκρισις','διήγησις','δικαίωσις','διόρθωσις','δόσις','δύναμις','δύσις','ἔγερσις','ἔκβασις','ἐκδίκησις','ἐκζήτησις','ἐκπλήρωσις','ἔκστασις','ἔλεγξις','ἔλευσις','ἔνδειξις','ἔνδυσις','ἐνδόμησις','ἐνδώμησις','ἐνθύμησις','ἔντευξις','ἐξανάστασις','ἕξις','ἐπανόρθωσις','ἔπαυλις','ἐπίγνωσις','ἐπίθεσις','ἐπίλυσις','ἐπιπόθησις','ἐπίστασις','ἐπισύστασις','ἐπιχείρησις','ἐρήμωσις','ζήτησις','θέλησις','θλῖψις','ἴασις','Ἱεράπολις','καθαίρεσις','κάκωσις','κατάβασις','κατάκρισις','κατάνυξις','κατάπαυσις','κατάρτισις','κατασκήνωσις','κατάσχεσις','κατοίκησις','καῦσις','καύχησις','κίνησις','κλάσις','κλῆσις','κοίμησις','κόλασις','κρίσις','κτίσις','κυβέρνησις','κωμόπολις','λῆμψις','λῆψις','λύσις','λύτρωσις','μέμψις','μετάθεσις','μετάλημψις','μητρόπολις','μόρφωσις','Νεάπολις','νέκρωσις','Νικόπολις','ὁμοίωσις','ὅρασις','ὄρεξις','ὄσφρησις','ὄψις','πανήγυρις','παράβασις','παράδοσις','παράκλησις','παρατήρησις','πάρδαλις','πάρεσις','πεποίθησις','περίθεσις','περιποίησις','πήρωσις','πίστις','ποίησις','πόλις','πόσις','πρᾶξις','πρόγνωσις','πρόθεσις','προσκαρτέρησις','πρόσκλησις','πρόσκλισις','πρόσλημψις','πρόσληψις','πρόσχυσις','πρόφασις','πτόησις','πτῶσις','πύρωσις','πώρωσις','ῥύσις','Σάρδεις','σεμίδαλις','στάσις','συγκατάθεσις','σύγχυσις','συζήτησις','συμφώνησις','συνάντησις','συνείδησις','σύνεσις','Σύρτις','τάξις','ταπείνωσις','τελείωσις','τήρησις','ὕβρις','ὑπάντησις','ὕπαρξις','ὑπόκρισις','ὑπόμνησις','ὑπόστασις','ὑποτύπωσις','ὑστέρησις','φανέρωσις','φάσις','φρόνησις','φύσις','φυσίωσις','πειθώ','Βαβυλών','ἅλων','λεγιών','Σαλαμίς','Σιδών','ὠδίν','γείτων','σινδών','χιών','εἰκών','τρυγών','φρήν','σιαγών','χείρ','γαστήρ','θυγάτηρ','μήτηρ','Λύστρα','Ἁγάρ','Αἰνών','Βηθεσδά','Βηθζαθά','Βηθλέεμ','Βηθσαϊδά','Γεννησαρέτ','Δαλμανουθά','Ἐλισάβετ','Θαμάρ','Ἰεζάβελ','Ἰεριχώ','Ἰερουσαλήμ','Κανά','Καφαρναούμ','Μαγαδάν','Μαριάμ','Ναζαρά','Ναζαρέθ','Ναζαρέτ','Ναΐν','Νινευή','Νινευΐ','Ῥαάβ','Ῥαμά','Ῥαχάβ','Ῥαχήλ','Ῥούθ','Σαλήμ','Σιών','Συχάρ','Ταβιθά','Χανάαν','χαρράν','Χοραζίν']:
                    words[line[:line.find(':')]] = int(line[line.find(':')+1:])
            elif gender == 3:
                if line[:line.find(':')] in ['n1d','n1e','n1f','n1g','n2a'] or line[line.rfind('\t\t')+2:] in ['Ἑρμῆς','ʼΑπελλῆς','βορρᾶς','ὀστοῦν','χειμάρρους','Ἀπολλῶς','Αἰθίοψ','κώνωψ','μώλωψ','σκόλοψ','Ἄραψ','λίψ','ἄνθραξ','δεσμοφύλαξ','θώραξ','κῆρυξ','κίλιξ','κόραξ','σκώληξ','φοῖνιξ','φύλαξ','χάραξ','αἴξ','ἅρπαξ','λάρυγξ','σαρδόνυξ','γέλως','γόης','ἱδρώς','Ἰωσῆς','Κρής','πένης','σής','χρώς','παῖς','πούς','ὄρνις','ἱμάς','Κλήμης','Κρήσκης','ὀδούς','Πούδης','ἄρχων','γέρων','δράκων','θεράπων','λέων','Σαλωμών','Σολομών','Φλέγων','Διοτρέφης','Ἑρμογένης','Σωσθένης','βότρυς','πῆχυς','Στάχυς','Ἀλεξανδρεύς','ἁλιεύς','Ἀντιοχεύς','ἀρχιερεύς','βηρεύς','βασιλεύς','βυρσεύς','γναφεύς','γραμματεύς','γονεύς','Θεσσαλονικεύς','ἱερεύς','ἱππεύς','καταγγελεύς','κεραμεύς','Κολασσαεύς','Κολοσσαεύς','Λαοδικεύς','Νηρεύς','πανδοχεύς','Ταρσεύς','φαρμακεύς','φονεύς','χαλκεύς','βοῦς','νοῦς','πλοῦς','χοῦς','νῆστις','ὄφις','ἀγών','αἰών','ἀμπελών','ἀρραβών','ἀρτέμων','Ἀσσάρων','ἀφεδρών','Γαλλίων','δεῖνα','ἐλαιών','Ἕλλην','εὐρακύλων','εὐροκλύδων','ζήνων','Ἡρῳδίων','καύσων','κεντυρίων','κλύδων','κοιτών','μεγιστάν','μήν','Μνάσων','μυλών','Νέρων','νυμφών','πύθων','πυλών','Σαρών','Σίμων','Σολομών','Τίμων','χειμών','χιτών','ἀλαζών','Ἀπολλύων','ἀρχιποίμην','ἀρχιτέκτων','βραχίων','γείτων','δαίμων','ἡγεμών','Ἰάσων','κανών','λιμήν','Μακεδών','ποιμήν','τέκτων','Φιλήμων','χαλκηδών','ἀρήν','κύων','ἅλς','αὐτόχειρ','Καῖσαρ','μάρτυς','νιπτήρ','ποδινιπτήρ','πρωτόμαρτυς','στατήρ','σωτήρ','φωστήρ','χαρακτήρ','ψευδόμαρτυς','ἀήρ','ἀλέκτωρ','ἀστήρ','δειπνοκλήτωρ','κατήγωρ','κοσμοκράτωρ','κτήτωρ','Νικάνωρ','παντοκράτωρ','πράκτωρ','προπάτωρ','ῥήτωρ','σπεκουλάτωρ','ἀνήρ','πατήρ','Ἀκύλας','Γολγοθᾶ','Ζηνᾶς','Ζεύς','Θυάτειρα','Θυάτιρα','Ἰησοῦς','Λευίς','Λύδδα','Μωσῆς','Μωϋσῆς','Χερούβ','Ἀβαδδών','Ἅβελ','Ἀβιά','Ἀβιαθάρ','Ἀβιούδ','Ἀβραάμ','Ἀδάμ','Ἀδδί','Ἀδμίν','Ἀζώρ','Ἀμιναδάβ','Ἀμών','Ἀμώς','Ἀράμ','Ἀρνί','Ἀρφαξάδ','Ἀσάφ','Ἀσήρ','Ἀχάζ','Ἀχάς','Ἀχίμ','Βάαλ','Βαλαάμ','Βαλάκ','βάρ','Βαράκ','Βαριωνᾶ','Βεεζεβούλ','Βελιάρ','Βενιαμίν','Βεώρ','Βόες','Βόοζ','Βόος','Βοσόρ','Γαβριήλ','Γάδ','Γαμαλιήλ','Γεδεών','Γώγ','Δαβίδ','Δάν','Δανιήλ','Δαυίδ','Ἔβερ','Ἐλεάζαρ','Ἐλιακίμ','Ἐλιέζερ','Ἐλιούδ','Ἐλμαδάμ','Ἐμμανουήλ','Ἑμμώρ','Ἐνώς','Ἑνώχ','Ἑσλί','Ἑσρώμ','Ἐφραίμ','Ζαβουλών','Ζάρα','Ζοροβαβέλ','Ἤρ','Ἠσαῦ','Θάρα','Ἰακώβ','Ἰανναί','Ἰάρετ','Ἰεσσαί','Ἰεφθάε','Ἰσαάκ','Ἰσαχάρ','Ἰσκαριώθ','Ἰσραήλ','Ἰσσαχάρ','Ἰωαθάμ','Ἰωανάν','Ἰωᾶς','Ἰώβ','Ἰωβήδ','Ἰωδά','Ἰωήλ','Ἰων́͂μ','Ἰωράμ','Ἰωρίμ','Ἰωσαφάτ','Ἰωσήφ','Ἰωσήχ','Κάϊν','Καϊνάμ','Καϊνάν','Κεδρών','Κίς','Κόρε','Κωσάμ','Λάμεχ','Λευί','Λώτ','Μάαθ','Μαγώγ','Μαδιάμ','Μαθουσάλα','Μαϊνάν','Μαλελεήλ','Μαναήν','Ματθάν','Ματθάτ','Ματταθά','Μελεά','Μελχί','Μελχισέδεκ','Μεννά','Μιχαήλ','Μολόχ','Ναασσών','Ναγγαί','Ναθάμ','Ναθαναήλ','Ναιμάν','Ναούμ','Ναχώρ','Νεφθαλίμ','Νηρί','Νίγερ','Νῶε','Ῥαγαύ','Ῥαιφάν','Ῥησά','Ῥοβοάμ','Ῥομφά','Ῥουβήν','Σαδώκ','Σαλά','Σαλαθιήλ','Σαλμών','Σαμουήλ','Σαμψών','Σαούλ','Σατάν','Σεμεΐν','Σερούχ','Σήθ','Σήμ','Σιλωάμ','Σκαριώθ','Συμεών','Φάλεκ','Φανουήλ','Φαραώ','Φαρές']:
                    words[line[:line.find(':')]] = int(line[line.find(':')+1:])
            else:
                words[line[:line.find(':')]] = int(line[line.find(':')+1:])
    f.close()
    return words

def chooseAdjective():
    '''Build and return the dictionary of adjectives and frequencies from the adjective counts.'''
    
    #Open the adjective lexicon, build the adjective list, and return it.
    f = open('../sentenceLayouts/adjectiveCounts')
    words = {}
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        if line != '':
            words[line[:line.find(':')]] = int(line[line.find(':')+1:])
    f.close()
    return words

def chooseDeterminer():
    '''Build and return the dictionary of determiners and frequencies from the determiner counts.'''
    
    #Open the determiner lexicon, build the determiner list, and return it.
    f = open('../sentenceLayouts/determinerCounts')
    words = {}
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        if line != '':
            words[line[:line.find(':')]] = int(line[line.find(':')+1:])
    f.close()
    return words

def chooseAdverb(weighted=False):
    '''Return a weighted random adverb based on adverb counts.
    
    Keyword arguments:
    weighted -- Whether or not to choose words with weighted random
                generation
    '''
    
    #Open the adverb lexicon, build the adverb list, and return it.
    f = open('../sentenceLayouts/adverbCounts')
    words = {}
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        if line != '':
            words[line[:line.find(':')]] = int(line[line.find(':')+1:])
    f.close()
    return chooseRandomWord(words,weighted)

def chooseConjunction(weighted=False):
    '''Return a weighted random conjunction based on conjunction counts.
    
    Keyword arguments:
    weighted -- Whether or not to choose words with weighted random
                generation
    '''
    
    #Open the conjunction lexicon, build the conjunction list, and return it.
    f = open('../sentenceLayouts/conjunctionCounts')
    words = {}
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        if line != '':
            words[line[:line.find(':')]] = int(line[line.find(':')+1:])
    f.close()
    return chooseRandomWord(words,weighted)

def chooseInterjection(weighted=False):
    '''Return a weighted random interjection based on interjection counts.
    
    Keyword arguments:
    weighted -- Whether or not to choose words with weighted random
                generation
    '''
    
    #Open the interjection lexicon, build the interjection list, and return it.
    f = open('../sentenceLayouts/interjectionCounts')
    words = {}
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        if line != '':
            words[line[:line.find(':')]] = int(line[line.find(':')+1:])
    f.close()
    return chooseRandomWord(words,weighted)

def chooseNumeral(weighted=False):
    '''Return a weighted random numeral based on numeral counts.
    
    Keyword arguments:
    weighted -- Whether or not to choose words with weighted random
                generation
    '''
    
    #Open the numeral lexicon, build the numeral list, and return it.
    f = open('../sentenceLayouts/numeralCounts')
    words = {}
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        if line != '':
            words[line[:line.find(':')]] = int(line[line.find(':')+1:])
    f.close()
    return chooseRandomWord(words,weighted)

def chooseParticle(weighted=False):
    '''Return a weighted random participle based on participle counts.
    
    Keyword arguments:
    weighted -- Whether or not to choose words with weighted random
                generation
    '''
    
    #Open the participle lexicon, build the participle list, and return it.
    f = open('../sentenceLayouts/participleCounts')
    words = {}
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        if line != '':
            words[line[:line.find(':')]] = int(line[line.find(':')+1:])
    f.close()
    return chooseRandomWord(words)

def choosePreposition(weighted=False):
    '''Return a weighted random preposition based on preposition counts.
    
    Keyword arguments:
    weighted -- Whether or not to choose words with weighted random
                generation
    '''
    
    #Open the preposition lexicon, build the preposition list, and return it.
    f = open('../sentenceLayouts/prepositionCounts')
    words = {}
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        if line != '':
            words[line[:line.find(':')]] = int(line[line.find(':')+1:])
    f.close()
    return chooseRandomWord(words,weighted)

def choosePronoun():
    '''Build and return the dictionary of pronouns and frequencies from the pronoun counts.'''
    
    #Open the pronoun lexicon, build the pronoun list, and return it.
    f = open('../sentenceLayouts/pronounCounts')
    words = {}
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        if line != '':
            words[line[:line.find(':')]] = int(line[line.find(':')+1:])
    f.close()
    return words

def chooseRandomWord(freqDict,weighted=False):
    '''Choose a weighted random word from a dictionary of words and word counts
    
    Keyword arguments:
    freqDict -- Dictionary of words mapped to their frequencies
    weighted -- whether to use weights to generate a random word
    '''
    list = []
    if weighted:
        for key in freqDict:
            list.append((freqDict[key],key))
        total = sum(pair[0] for pair in list)
        r = random.randint(1, total)
        for (count, word) in list:
            r -= count
            if r <= 0:
                retval = word
    else:
        for key in freqDict:
            list.append(key)
        if len(list) > 1:
            r = random.randint(0,len(list)-1)
            retval = list[r]
        else:
            retval = None
    return retval
        
def getStyle(word,pos):
    '''Get the style of a word, from Mounce's Morphology.
    
    Keyword arguments:
    word -- word to analyze
    pos -- stringed part of speech of the word. One of 'verb','noun',
           or 'adjective'
    '''
    if pos == 'verb':
        f = open('../Lexicons/verbs')
        lines = f.readlines()
        for line in lines:
            if line.startswith('\t\t'):
                if line.endswith('\n'):
                    line = line[:-1]
                line = line[2:]
                if line[line.find('\t')+2:] == word:
                    f.close()
                    return line[:line.find('\t')]
        return None
    elif pos == 'noun':
        f = open('../Lexicons/nouns')
        lines = f.readlines()
        for line in lines:
            if line.startswith('\t\t'):
                if line.endswith('\n'):
                    line = line[:-1]
                line = line[2:]
                if line[line.find('\t')+2:] == word:
                    f.close()
                    return line[:line.find('\t')]
        return None
    elif pos == 'adjective':
        f = open('../Lexicons/adjectives')
        lines = f.readlines()
        for line in lines:
            if line.startswith('\t\t'):
                if line.endswith('\n'):
                    line = line[:-1]
                line = line[2:]
                if line[line.find('\t')+2:] == word:
                    f.close()
                    return line[:line.find('\t')]
        return None
    else:
        return None

def readNodes(string):
    '''Build and return a feature-based CFG.
    
    Keyword arguments:
    string -- String of a CFG
    '''
    return SentenceFormer.readCFG(string)

def formSentenceModel(nodes,maxDepth=3):
    '''Form a sentence model.
    
    Keyword arguments:
    nodes -- A CFG already read from file.
    maxDepth -- Maximum recursion depth to travel (default is 3).
    '''
    return SentenceFormer.generateSentence(nodes,maxDepth)

def generateSentence(sentenceModel,weighted=False):
    '''Generate a word-filled sentence from a model.
    
    Keyword arguments:
    sentenceModel -- A model of a sentence formed from a feature-based
                     CFG or sentence
    weighted -- Whether or not to use weighted random word generation
    '''
    
    # For every word in the sentence, fill in a word that matches the
    # part of speech and features specified by the CFG. If any word
    # was unable to be formed, return ['FAILED!'] (a sentence
    # consisting of the single word 'FAILED'.
    sentence = []
    for word in sentenceModel:
        typ = word[:word.find('_')] if word.find('_')!=-1 else word
        if typ == 'verb':
            number=person=mood=tense=voice=gender=case=0
            verb = None
            if word.find('Number=') != -1:
                subword = word[word.find('Number='):]
                number = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:]) 
            if word.find('Person=') != -1:
                subword = word[word.find('Person='):]
                person = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Mood=') != -1:
                subword = word[word.find('Mood='):]
                mood = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Tense=') != -1:
                subword = word[word.find('Tense='):]
                tense = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Voice=') != -1:
                subword = word[word.find('Voice='):]
                voice = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Gender=') != -1:
                subword = word[word.find('Gender='):]
                gender = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Case=') != -1:
                subword = word[word.find('Case='):]
                case = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            sentence.append(formVerb(chooseVerb(),weighted,number,person,mood,tense,voice,gender,case))
        elif typ == 'noun':
            number=case=gender=0
            if word.find('Number=')!=-1:
                subword = word[word.find('Number='):]
                number = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Case=')!=-1:
                subword = word[word.find('Case='):]
                case = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Gender=')!=-1:
                subword = word[word.find('Gender='):]
                gender = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            sentence.append(formNoun(chooseNoun(gender),weighted,number,case,gender))
        elif typ == 'adj':
            number=case=gender=0
            if word.find('Number=')!=-1:
                subword = word[word.find('Number='):]
                number = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Case=')!=-1:
                subword = word[word.find('Case='):]
                case = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Gender=')!=-1:
                subword = word[word.find('Gender='):]
                gender = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            sentence.append(formAdjective(chooseAdjective(),weighted,gender,number,case))
        elif typ == 'det':
            number=case=gender=0
            if word.find('Number=')!=-1:
                subword = word[word.find('Number='):]
                number = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Case=')!=-1:
                subword = word[word.find('Case='):]
                case = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Gender=')!=-1:
                subword = word[word.find('Gender='):]
                gender = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            sentence.append(formDeterminer(chooseDeterminer(),weighted,gender,number,case))
        elif typ == 'adv':
            # sentence.append(chooseRandomWord(chooseAdverb(),weighted))
            sentence.append(chooseAdverb(weighted))
        elif typ == 'conj':
            # sentence.append(chooseRandomWord(chooseConjunction(),weighted))
            sentence.append(chooseConjunction(weighted))
        elif typ == 'intj':
            # sentence.append(chooseRandomWord(chooseInterjection(),weighted))
            sentence.append(chooseInterjection(weighted))
        elif typ == 'num':
            # sentence.append(chooseRandomWord(chooseNumeral(),weighted))
            sentence.append(chooseNumeral(weighted))
        elif typ == 'ptcl':
            # sentence.append(chooseRandomWord(chooseParticle(),weighted))
            sentence.append(chooseParticle(weighted))
        elif typ == 'prep':
            # sentence.append(chooseRandomWord(choosePreposition(),weighted))
            sentence.append(choosePreposition(weighted))
        elif typ == 'pron':
            number=case=gender=0
            if word.find('Number=')!=-1:
                subword = word[word.find('Number='):]
                number = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Case=')!=-1:
                subword = word[word.find('Case='):]
                case = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            if word.find('Gender=')!=-1:
                subword = word[word.find('Gender='):]
                gender = int(subword[subword.find('=')+1:subword.find(',')]) if subword.find(',') != -1 else int(subword[subword.find('=')+1:])
            sentence.append(formPronoun(choosePronoun(),weighted,gender,number,case))
        else:
            sentence.append(None)
    if any(w == None or w == 0 or w == '0' or w == '?' for w in sentence):
        return ['FAILED!']
    else:
        return sentence

def stringSentence(sentence):
    '''Turn a sentence (list of words) into a string.
    
    Keyword arguments:
    sentence -- List of words to be stringified.
    '''
    
    s = ''
    for word in sentence:
        s += str(word) + ' '
    return s[:-1] + '.'

def autogenerateSentence(numToMake=1,weighted=False,fn='Grammar.fcfg'):
    '''Generate a list of sentences in one function call.
    
    Keyword arguments:
    numToMake -- Number of sentences to generate (default is 1).
    weighted -- Whether or not to use weighted random word generation
                (default False)
    fn -- File name of the grammar (default is 'Grammar.fcfg'). Should
          be a list of sentence models, separated by a line labeled 'STOP'
    '''
    
    # Make the specified number of sentences, redoing any that fail,
    # so that every sentence returned is complete.
    f = open(fn)
    sentenceModels = f.read().split('\nSTOP\n')
    f.close()
    
    sentences = []
    for i in range(numToMake):
        nodes = readNodes(sentenceModels[random.randint(0,len(sentenceModels)-1)])
        nodes = readNodes(sentenceModels[0])
        sent = generateSentence(formSentenceModel(nodes))
        while (sent[0] == 'FAILED!'):
            sent = generateSentence(formSentenceModel(nodes))
        sentences.append(stringSentence(sent))
    return sentences

def autogenerateSentencesFromModelFile(numToMake=1,weighted=False,modelFile='models'):
    '''Generate sentences from a file of template sentence models.
    
    Keyword arguments:
    numToMake -- Number of sentences to generate (Default 1)
    weighted -- Whether or not to use weighted random word generation
                (Default False)
    modelFile -- Name of the file that contains sentence model
                 templates (default 'models')
    '''
    
    f = open(modelFile)
    lines = f.readlines()
    f.close()
    
    sentences = []
    for i in range(numToMake):
        line = lines[random.randint(0,len(lines)-1)][2:-3].split('\', \'')
        sent = line[1:]
        full = generateSentence(sent)
        reference = line[0]
        while full[0] == 'FAILED!':
            line = lines[random.randint(0,len(lines)-1)][2:-3].split('\', \'')
            sent = line[1:]
            full = generateSentence(sent)
            reference = line[0]
        sentences.append((full,reference))
    return sentences

# for s in autogenerateSentence(numToMake=5,fn='cfgs'):
#     print s
# for s in autogenerateSentencesFromModelFile(numToMake=5,weighted=False):
#     st = ''
#     for w in s[0]:
#         st += w + ' '
#     print st[:-1] + '. ' + str(s[1])