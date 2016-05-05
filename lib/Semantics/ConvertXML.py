# -*- coding: utf-8 -*-
'''
Created on Jul 2, 2014

@author: Jake
'''
import xml.etree.ElementTree as ET

for i in range(40,67):
    f = str(i)+'.xml'
    tree = ET.parse('../sentenceLayouts/'+f)
    root = tree.getroot()
    for node in root.iter('Node'):
        t = []
        for key in node.attrib:
            if key not in ['Head','Cat','Rule']:
                t.append(key)
        for key in t:
            del node.attrib[key]
    tree.write(f,'utf-8')
    print 'Finished',i,'of',66