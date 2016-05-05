# -*- coding: utf-8 -*-
'''
Created on Jun 24, 2014

@author: Jake
'''
from nltk import FeatStruct
import xml.etree.ElementTree as ET
from generators import VerbGenerator

def formName(node):
    return str(node.get('Cat')) + ('_'+ str(node.get('Rule')) if node.get('Rule')!=None else '') + ('_' + str(node.get('ClType')) if node.get('ClType')!=None else '')

def formFeatures(node):
    s = '['
    for feature in ['Person','Tense','Voice','Mood','Case','Number','Gender']:
        if node.get(feature) != None:
            s += feature + '=' + node.get(feature) + ','
    return s[:-1] + ']' if len(s) > 1 else s + ']'

def formTerminal(node):
    s = '{'
    s += node.get('Cat') + '_'
    for feature in ['Person','Tense','Voice','Mood','Case','Number','Gender']:
        if node.get(feature) != None:
            s += feature + '=' + node.get(feature) + ','
    return s[:-1] + '}'
    
def formLine(node,sentence):
    s = formName(node) + formFeatures(node) + ' --> '
    if len(node.getchildren()) == 0:
        s += formTerminal(node) + '.\n'
    else:
        for child in node.getchildren():
            s += formName(child) + formFeatures(child) + ', '
        s = s[:-2] + '.\n'
    if s[:-1] not in sentence.split('\n'):
        return s
    else:
        return ''

def writeCFGs(input,output):
    tree = ET.parse(input)
    root=tree.getroot()
    
    sentenceCFGs = []
    
    for sentence in root.iter('Sentence'):
        s = sentence.get('ID') + '\n'
        for node in sentence.iter('Node'):
            s += formLine(node,s)
        sentenceCFGs.append(s)
    
    s = ''
    for sentence in sentenceCFGs:
        s += sentence + '\n' + 'STOP\n'
    s += '\n'
    
    f = open(output,'a')
    f.write(s)
    f.close()