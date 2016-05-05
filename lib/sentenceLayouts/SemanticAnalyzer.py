# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2014

@author: Jake
'''
import xml.etree.ElementTree as ET

def getTreeRoot(input):
    tree = ET.parse(input)
    return tree.getroot()

def writeParts(parts,output):
    s = ''
    for rule in parts:
        s += rule + ':\n'
        for phrase in parts[rule]:
            s += '\t' + phrase + '\t'
    f = open(output,'w')
    f.write(s)
    f.close()

def stringNode(node):
    s = []
    if len(node.getchildren()) == 0:
        s.append(node.get('Cat') + ' || ' + node.get('Unicode').encode('utf-8') + ' || ' + node.get('UnicodeLemma').encode('utf-8')) 
    else:
        if node.get('Rule') != None:
            s.append(node.get('Rule'))
        for child in node.getchildren():
            print child.get('Cat')
            s += getHead(child)
    return s

def getHead(node):
    if len(node.getchildren()) == 0:
        return stringNode(node)
    else:
        head = int(node.get('Head'))
        print node.get('Cat')
        return getHead(node.getchildren()[head])

root = getTreeRoot('65.xml')
for node in root.iter('Node'):
    if node.get('nodeId') == '650010010010170':
        print stringNode(node)[1]