'''
Created on Jun 25, 2014

@author: Jake
'''
import Editor
import xml.etree.ElementTree as ET
from generators import VerbGenerator
from operator import itemgetter

def makeModels(input,output):
    tree = ET.parse(input)
    root = tree.getroot()
    sentences = []
    for sentence in root.iter('Sentence'):
        sentences.append([sentence.get('ID')])
        for node in sentence.iter('Node'):
            if len(node.getchildren()) == 0:
                sentences[len(sentences)-1].append((makeWord(node),int(node.get('morphId'))))
    s = ''
    for sentence in sentences:
        ref = sentence[0]
        sentence = sentence[1:]
        sentence = sorted(sentence,key=itemgetter(1))
        for i in range(len(sentence)):
            sentence[i] = sentence[i][0]
        sentence = [ref]+sentence
        s += str(sentence) + '\n'
    f = open(output,'a')
    f.write(s)
    f.close()
    
def makeWord(node):
    word = ''
    word += node.get('Cat') + '_'
    for feature in ['Person','Tense','Voice','Mood','Case','Number','Gender']:
        if node.get(feature) != None:
            if feature == 'Tense' and (node.get(feature) == 'Aorist' or (node.get(feature) == 'Future' and node.get('Mood') == 'Indicative' and node.get('Voice') == 'Passive') or (node.get(feature) == 'Perfect' and node.get('Mood') == 'Indicative' and node.get('Voice') == 'Passive')):
                if node.get(feature) == 'Aorist':
                    which = VerbGenerator.whichAorist(node.get('UnicodeLemma'))
                    if which == 0 or which == 1:
                        node.set(feature,'FirstAorist')
                    else:
                        node.set(feature,'SecondAorist')
                elif node.get(feature) == 'Future' or node.get(feature) == 'Perfect':
                    which = VerbGenerator.whichPerfect(node.get('UnicodeLemma'))
                    if node.get(feature) == 'Future':
                        if which == 0 or which == 1:
                            node.set(feature,'FirstFuture')
                        else:
                            node.set(feature,'SecondFuture')
                    else:
                        if which == 0 or which == 1:
                            node.set(feature,'FirstPerfect')
                        else:
                            node.set(feature,'SecondPerfect')
            new = Editor.matchFeature(node.get(feature))
            word += feature + '=' + str(new) + ','
    return word[:-1]