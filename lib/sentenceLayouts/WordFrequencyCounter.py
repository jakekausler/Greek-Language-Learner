# -*- coding: utf-8 -*-
'''
Created on Jun 25, 2014

@author: Jake
'''

import xml.etree.ElementTree as ET
import sys
import operator
from decimal import Decimal
import math

def countFrequencies(input):
    tree = ET.parse(input)
    root = tree.getroot()
    
    return countToDict(root)
    
    
def countToDict(root):
    d = {}
    for node in root.iter('Node'):
        if len(node.getchildren()) == 0:
            if node.get('UnicodeLemma') in d:
                d[node.get('UnicodeLemma')] += 1
            else:
                d[node.get('UnicodeLemma')] = 1
    return d

def writeFrequencies(d,output):
    s = ''
    for item in d:
        if item[0].endswith(')'):
            item = (item[0][:item[0].find('(')]+item[0][item[0].find('(')+1:item[0].find(')')],item[1])
        s += item[0].encode('utf-8') + ':' + str(item[1]) + '\n'
    f = open(output,'w')
    f.write(s)
    f.close()
    
def combineFrequencies(listOfDicts):
    d = {}
    for dict in listOfDicts:
        for key in dict:
            if key in d:
                d[key] += dict[key]
            else:
                d[key] = dict[key]
    return d

def dictCountsToProbabilities(dict):
    total = 0
    for key in dict:
        total += dict[key]
    d = {}
    for key in dict:
        d[key] = Decimal(dict[key])/Decimal(total)
    return d
    
def allWrites(listOfInputs,output):
    d = []
    i=0
    total = len(listOfInputs)
    for f in listOfInputs:
        d.append(countFrequencies(f))
        print 'Finished dict ' + str(i+1) + ' of ' + str(total)
        i+=1
    full = sortDict(dictCountsToProbabilities(combineFrequencies(d)))
    writeFrequencies(full,output)
    
def sortDict(dictionary):
    return sorted(dictionary.iteritems(), key=operator.itemgetter(1))

def allWritePOSFrequencies(listOfInputs):
    d = []
    i=0
    total = len(listOfInputs)
    for f in listOfInputs:
        d.append(countPOSFrequencies(f))
        print 'Finished dict ' + str(i+1) + ' of ' + str(total)
        i+=1
    full = sortPOSDict(combinePOSDicts(d))
    writePOSFrequencies(full)
    
def countPOSFrequencies(input):
    tree = ET.parse(input)
    root = tree.getroot()
    
    return countPOSToDict(root)

def countPOSToDict(root):
    d = {}
    for node in root.iter('Node'):
        if len(node.getchildren()) == 0:
            if node.get('Cat') in d:
                if node.get('UnicodeLemma') in d[node.get('Cat')]:
                    d[node.get('Cat')][node.get('UnicodeLemma')] += 1
                else:
                    d[node.get('Cat')][node.get('UnicodeLemma')] = 1
            else:
                d[node.get('Cat')] = {}
                d[node.get('Cat')][node.get('UnicodeLemma')] = 1
    return d

def combinePOSDicts(listOfDicts):
    d = {}
    for dict in listOfDicts:
        for cat in dict:
            for key in dict[cat]:
                if cat in d:
                    if key in d[cat]:
                        d[cat][key] += dict[cat][key]
                    else:
                        d[cat][key] = dict[cat][key]
                else:
                    d[cat] = {}
                    d[cat][key] = dict[cat][key]
    return d

def dictPOSCountsToProbabilities(dict):
    d = {}
    for cat in dict:
        total = 0
        for key in dict[cat]:
            total += dict[cat][key]
        d[cat] = {}
        for key in dict[cat]:
            d[cat][key] = Decimal(dict[cat][key])/Decimal(total)
    return d

def sortPOSDict(dict):
    d = {}
    for cat in dict:
        d[cat] = sorted(dict[cat].iteritems(), key=operator.itemgetter(1))
    return d

def writePOSFrequencies(dictOfPOSFrequencies,adjectiveFile='adjectiveCounts',adverbFile='adverbCounts',conjunctionFile='conjunctionCounts',determinerFile='determinerCounts',interjectionFile='interjectionCounts',nounFile='nounCounts',numeralFile='numeralCounts',participleFile='participleCounts',prepositionFile='prepositionCounts',pronounFile='pronounCounts',verbFile='verbCounts'):
    for cat in dictOfPOSFrequencies:
        dictOfPOSFrequencies[cat] = normalizeList(dictOfPOSFrequencies[cat],stDev(dictOfPOSFrequencies[cat])+average(dictOfPOSFrequencies[cat]))
        print cat,stDev(dictOfPOSFrequencies[cat]),average(dictOfPOSFrequencies[cat]),min(dictOfPOSFrequencies[cat]),max(dictOfPOSFrequencies[cat])
        s = ''
        for item in dictOfPOSFrequencies[cat]:
            if item[0].endswith(')'):
                item = (item[0][:item[0].find('(')]+item[0][item[0].find('(')+1:item[0].find(')')],item[1])
            s += item[0].encode('utf-8') + ':' + str(item[1]) + '\n'
        if cat == 'adv':
            f = open(adverbFile,'w')
            f.write(s)
            f.close()
        elif cat == 'adj':
            f = open(adjectiveFile,'w')
            f.write(s)
            f.close()
        elif cat == 'conj':
            f = open(conjunctionFile,'w')
            f.write(s)
            f.close()
        elif cat == 'det':
            f = open(determinerFile,'w')
            f.write(s)
            f.close()
        elif cat == 'intj':
            f = open(interjectionFile,'w')
            f.write(s)
            f.close()
        elif cat == 'noun':
            f = open(nounFile,'w')
            f.write(s)
            f.close()
        elif cat == 'num':
            f = open(numeralFile,'w')
            f.write(s)
            f.close()
        elif cat == 'ptcl':
            f = open(participleFile,'w')
            f.write(s)
            f.close()
        elif cat == 'prep':
            f = open(prepositionFile,'w')
            f.write(s)
            f.close()
        elif cat == 'pron':
            f = open(pronounFile,'w')
            f.write(s)
            f.close()
        elif cat == 'verb':
            f = open(verbFile,'w')
            f.write(s)
            f.close()
            
def average(listOfWordFrequencies):
    total = 0
    num = 0
    for item in listOfWordFrequencies:
        total += item[1]
        num += 1
    return float(total)/float(num)

def stDev(listOfWordFrequencies):
    avg = average(listOfWordFrequencies)
    total = 0
    num = 0
    for item in listOfWordFrequencies:
        total += math.pow((item[1]-avg),2)
        num += 1
    return math.sqrt(total/float(num))

#Normalizes (scales) data to be between 1 and the newMax. Rounds up to the next integer
def normalizeList(listOfWordFrequencies,newMax):
    mn = min(listOfWordFrequencies)
    mx = max(listOfWordFrequencies)
    for i in range(len(listOfWordFrequencies)):
        listOfWordFrequencies[i] = (listOfWordFrequencies[i][0],int(newMax*((float(listOfWordFrequencies[i][1])-float(mn))/(float(mx)-float(mn))))+1)
    return listOfWordFrequencies

def min(listOfWordFrequencies):
    value = listOfWordFrequencies[0][1]
    for item in listOfWordFrequencies:
        if item[1] < value:
            value = item[1]
    return value

def max(listOfWordFrequencies):
    value = listOfWordFrequencies[0][1]
    for item in listOfWordFrequencies:
        if item[1] > value:
            value = item[1]
    return value