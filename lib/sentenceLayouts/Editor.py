# -*- coding: utf-8 -*-
'''
Created on Jun 24, 2014

@author: Jake
'''
import xml.etree.ElementTree as ET
from nltk import FeatStruct
from generators import VerbGenerator

def getMaxDepth(root):
    maxDepth = 0
    for node in root.iter('Node'):
        if int(node.get('Depth')) > maxDepth:
            maxDepth = int(node.get('Depth'))
    return maxDepth

def mergeChildren(childNodes):
    features = []
    for child in childNodes:
        features.append(FeatStruct())
        for feature in ['Person','Tense','Voice','Mood','Case','Number','Gender','Degree']:
            if child.get(feature) != None:
                features[len(features)-1]=features[len(features)-1].unify(FeatStruct('['+str(feature)+'='+str(child.get(feature))+']'))
    retFeature = FeatStruct()
    for feature in features:
        retFeature = smartUnify(retFeature,feature)
    return retFeature

def dictFeatures(featStruct):
    d = {}
    if featStruct != None:
        for f in featStruct:
            d[f] = featStruct[f]
    return d

def smartUnify(f1,f2):
    feature = FeatStruct()
    for key in f1:
        if key in f2:
            if f1[key] == f2[key]:
                feature = feature.unify(FeatStruct('['+str(key)+'='+str(f1[key])+']'))
#         else:
#             feature = feature.unify(FeatStruct('['+key+'='+f1[key]+']'))
    if f1 == FeatStruct():
        for key in f2:
            if key not in feature:# and key not in f1:
                feature = feature.unify(FeatStruct('['+str(key)+'='+str(f2[key])+']'))
#     if 'Case' in f1 and f1['Case'] == 'Genitive' and 'Case' in f2 and f2['Case'] == 'Nominative':
#     print str(f1).replace('\n','').replace(' ','') + ' + ' + str(f2).replace('\n','').replace(' ','') + ' = ' + str(feature).replace('\n','').replace(' ','')
    return feature

def matchFeature(feature):
    d = {'Nominative':1,'Genitive':2,'Dative':3,'Accusative':4,'Vocative':5,'Singular':1,'Plural':2,'First':1,'Second':2,'Third':3,'Active':1,'Middle':2,'Passive':3,'Masculine':1,'Feminine':2,'Neuter':3,'Indicative':1,'Subjunctive':2,'Optative':3,'Imperative':4,'Infinitive':5,'Participle':6,'Present':1,'Imperfect':2,'Future':3,'FirstFuture':3,'FirstAorist':4,'SecondAorist':5,'Perfect':6,'FirstPerfect':6,'SecondPerfect':7,'Pluperfect':8,'SecondFuture':9}
    return d[feature] if feature in d else 0

def runEditor(input,output):
    tree = ET.parse(input)
    root=tree.getroot()
    
    for node in root.iter('Node'):
        if len(node.getchildren()) == 0:
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
                    new = matchFeature(node.get(feature))
                    if new == 0:
                        print feature, node.get(feature)
                    node.set(feature,'F'+str(new)+'F')
    
    maxDepth = getMaxDepth(root)
    for i in range(maxDepth):
        print "Completed round " + str(i) + " of " + str(maxDepth)
        for node in root.iter('Node'):
            if len(node.getchildren()) != 0:
                features = dictFeatures(mergeChildren(node.getchildren()))
    #             if node.get('nodeId') == '650010010020030':
    #                 print node.get('nodeId'), features
                if features != {} and len(node.getchildren()) != 0:
    #                 print features
                    for feature in ['Person','Tense','Voice','Mood','Case','Number','Gender','Degree']:
                        if feature in features.keys():
                            node.set(feature,features[feature])
                        else:
                            if node.get(feature) != None:
                                del node.attrib[feature]
    tree.write(output,'utf-8')