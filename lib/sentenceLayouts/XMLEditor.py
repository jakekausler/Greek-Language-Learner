# -*- coding: utf-8 -*-
'''
Created on Jun 20, 2014

@author: Jake
'''
import xml.etree.ElementTree as ET
from nltk.featstruct import FeatStruct

class NonTerminal:
    def __init__(self,name,children):
        self.name = name
        self.children = children

class Terminal:
    def __init__(self,name,value,features):
        self.name = name
        self.value = value
        self.features = features
        
nodes = []

tree = ET.parse('65.xml')
root = tree.getroot()

for sentence in root.iter('Sentence'):
    for tree in sentence.iter('Tree'):
        for node in tree.iter('Node'):
            if 'Unicode' in node.keys():
                features = FeatStruct()
                for key in node.keys():
                    if key in ['Person','Tense','Voice','Mood','Case','Number','Gender','Degree']:
                        features = features.unify(FeatStruct('['+str(key)+'=\''+str(node.get(key))+'\']'))
                nodes.append(Terminal(node.get('Cat'),node.get('Unicode'),features))
            else:
                name = str(node.get('Cat')) + ('_'+ str(node.get('Rule')) if node.get('Rule')!=None else '') + ('_' + str(node.get('ClType')) if node.get('ClType')!=None else '')
                children = []
                for child in node.getchildren():
                    children.append(child.get('Cat') + ('_'+ str(child.get('Rule')) if child.get('Rule')!=None else '') + ('_' + str(child.get('ClType')) if child.get('ClType')!=None else ''))
                nodes.append(NonTerminal(name,children))
    nodes.append('------')
            
def printCFG(nodes):
    s = ''
    for node in nodes:
        if isinstance(node,Terminal):
            s += node.name + ' --> {' + node.name + '_'
            for key in node.features.keys():
                s += key + '=' + node.features[key] + ','
            s = s[:-1] + '}.\n'
        elif isinstance(node, NonTerminal):
            s += node.name + ' --> '
            for child in node.children:
                s += child + ', '
            s = s[:-2]+'.\n'
        else:
            s += '------\n'
    f = open('test','w')
    f.write(s.encode('utf8'))
    f.close()
    
class Term:
    def __init__(self,name):
        self.name = name
    
class NonTerm:
    def __init__(self,name):
        self.name = name
        self.children = []
    def addChildren(self,s,nodes):
        j = 0
        inChildren = False
        while j < len(children) and inChildren==False:
            i=0
            inPath = True
            while i < len(children[j]) and inPath and len(children[j])==len(s):
                if s[i] != children[j][i].name:
                    inPath=False
                i+=1
            if inPath:
                inChildren=True
            j+=1
        if not inChildren:
            self.children.append([])
            for item in s:
                i=0
                inNodes=False
                while i < len(nodes) and inNodes==False:
                    if nodes[i].name==s:
                        inNodes=True
                        self.children[len(self.children)-1].append(nodes[i])
                    i+=1
                if not inNodes:
                    if len(s)==1 and s[0].startswith('{'):
                        nodes.append(Term(s[0]))
                        self.children[len(self.children)-1].append(nodes[len(nodes)-1])
                    else:
                        for item in s:
                            nodes.append(NonTerm(item))
                            self.children[len(self.children)-1].append(nodes[len(nodes)-1])

def listValuesOfNodes(nodes):
    d = {}
    for node in nodes:
        if not isinstance(node,str):
            if node.name in d.keys():
                if isinstance(node,Terminal):
                    if node.features not in d[node.name]:
                        d[node.name].append(node.features)
                else:
                    if node.children not in d[node.name]:
                        d[node.name].append(node.children)
            else:
                d[node.name] = []
                if isinstance(node,Terminal):
                    if node.features not in d[node.name]:
                        d[node.name].append(node.features)
                else:
                    if node.children not in d[node.name]:
                        d[node.name].append(node.children)
    return d

def listValuesOfNode(name,nodes):
    if any(isinstance(n,Terminal) and n.name == name for n in nodes):
        return 'terminal'
    else:
        d = {}
        for node in nodes:
            if not isinstance(node,str):
                if node.name == name:
                    if node.name in d.keys():
                        if node.children not in d[node.name]:
                            d[node.name].append(node.children)
                    else:
                        d[node.name] = []
                        d[node.name].append(node.children)
    m = {}
    for key in d:
        for i in range(len(d[key])):
            for j in range(len(d[key][i])):
                m = listValuesOfNode(d[key][i][j],nodes)
                d[key][i][j] = m
    return d

printCFG(nodes)
