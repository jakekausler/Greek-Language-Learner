'''
Created on Jun 20, 2014

@author: Jake
'''
import xml.etree.ElementTree as ET
from nltk.featstruct import FeatStruct

# class Terminal:
#     def __init__(self,name,features):
#         self.name = name
#         self.features = features
#     def toString(self):
#         s = ''
#         s += self.name + ' --> {' + self.name + '_'
#         for key in self.features.keys():
#             s += key + '=' + self.features[key] + ','
#         return s[:-1]+'}.\n'
#         
# class NonTerminal:
#     def __init__(self,name):
#         self.name = name
#         self.childPaths = []
#     def addPath(self,listOfChildrenNames,allNodes):
#         i=0
#         inPaths=False
#         while i < len(self.childPaths) and not inPaths:
# #             print str(i) + self.name + ' ' + str(self.childPaths[i].toString())
#             inPaths = self.childPaths[i].inPath(listOfChildrenNames)
#             i+=1
#         if not inPaths:
#             self.childPaths.append(ChildPath())
#             self.childPaths[len(self.childPaths)-1].addChildren(listOfChildrenNames,allNodes)
#     def toString(self):
#         s = ''
#         for i in range(len(self.childPaths)):
#             s += self.name + ' --> ' + self.childPaths[i].toString() + '.\n'
#         return s
#         
# class ChildPath:
#     def __init__(self):
#         self.children = []
#     def addChildren(self,listOfChildrenNames,allNodes):
#         i=0
#         inNodes = False
#         for name in listOfChildrenNames:
#             while i < len(allNodes) and not inNodes:
#                 if allNodes[i].name == name:
#                     inNodes = True
#                 i+=1
#             if inNodes:
#                 self.children.append(allNodes[i-1])
#             else:
#                 if name.startswith('{'):
#                     allNodes.append(Terminal(name))
#                 else:
#                     allNodes.append(NonTerminal(name))
#                 self.children.append(allNodes[len(allNodes)-1])
#     def inPath(self,listOfChildrenNames):
#         i=0
#         inThis= (len(listOfChildrenNames)==len(self.children))
#         while i < len(self.children) and inThis:
#             if self.children[i].name != listOfChildrenNames[i]:
#                 inThis = False
#             i+=1
#         return inThis
#     def toString(self):
#         s = ''
#         for i in range(len(self.children)):
#             s += self.children[i].name + ', '
#         return s[:-2]
# 
# def addTerminalToNodes(node,allNodes):
#     i=0
#     inNodes=False
#     name = node.get('Cat')
#     while i<len(allNodes) and not inNodes:
#         if allNodes[i].name == name:
#             inNodes = True
#         i+=1
#     if not inNodes:
#         features = FeatStruct()
#         for key in node.keys():
#             if key in ['Person','Tense','Voice','Mood','Case','Number','Gender','Degree']:
#                 features = features.unify(FeatStruct('['+str(key)+'=\''+str(node.get(key))+'\']'))
#         allNodes.append(Terminal(name,features))
#     return allNodes
# 
# def addNonTerminalToNodes(node,allNodes):
#     i=0
#     inNodes=False
#     name=str(node.get('Cat')) + ('_'+ str(node.get('Rule')) if node.get('Rule')!=None else '') + ('_' + str(node.get('ClType')) if node.get('ClType')!=None else '')
#     while i < len(allNodes) and not inNodes:
#         if allNodes[i].name == name:
#             inNodes = True
#         i+=1
#     if inNodes:
#         children = []
#         for child in node.getchildren():
#             children.append(child.get('Cat') + ('_'+ str(child.get('Rule')) if child.get('Rule')!=None else '') + ('_' + str(child.get('ClType')) if child.get('ClType')!=None else ''))
#         allNodes[i-1].addPath(children,allNodes)
#     else:
#         allNodes.append(NonTerminal(name))
#         children = []
#         for child in node.getchildren():
#             children.append(child.get('Cat') + ('_'+ str(child.get('Rule')) if child.get('Rule')!=None else '') + ('_' + str(child.get('ClType')) if child.get('ClType')!=None else ''))
#         allNodes[len(allNodes)-1].addPath(children,allNodes)
#     return allNodes
# 
# def readXMLToNodes(xmlFile):
#     allNodes = []
#     tree = ET.parse(xmlFile)
#     root = tree.getroot()
#     for node in tree.iter('Node'):
#         if 'Unicode' in node.keys():
#             allNodes = addTerminalToNodes(node,allNodes)
#         else:
#             allNodes = addNonTerminalToNodes(node,allNodes)
#     return allNodes

class Terminal:
    def __init__(self,name,features):
        self.name = name
        self.features = features
    def toString(self):
        s = ''
        s += self.name + '[' + stringFeatures(self.features) + ']' + ' --> {' + self.name + '_' + stringFeatures(self.features) + '}.\n'
        if s.endswith('_}.\n'):
            s = s[:-4] + '}.\n'
        return s
    
class NonTerminal:
    def __init__(self,name):
        self.name = name
        self.childPaths = []
        self.features = FeatStruct()
    def addPath(self,children,nodes):
        i=0
        inPaths = False
        while i < len(self.childPaths) and not inPaths:
            if self.childPaths[i].inPath(children):
                inPaths = True
            i+=1
        if not inPaths:
            self.childPaths.append(ChildPath())
            self.childPaths[len(self.childPaths)-1].addChildren(children,nodes)
    def toString(self):
        s = ''
        for path in self.childPaths:
            s += self.name + '[' + stringFeatures(self.features) + ']' + ' --> ' + path.toString() + '.\n'
        return s
    
class ChildPath:
    def __init__(self):
        self.children = []
    def addChildren(self,children,nodes):
        for child in children:
            nodeNumber = whichNode(child,nodes)
            if nodeNumber == -1:
                if child.startswith('{'):
                    nodes.append(Terminal(child[1:child.find('_')],FeatStruct('['+child[child.find('_')+1:-1]+']')))
                else:
                    nodes.append(NonTerminal(child))
                self.children.append(nodes[len(nodes)-1])
            else:
                self.children.append(nodes[nodeNumber])
    def inPath(self,children):
        if len(children) == len(self.children):
            i = 0
            inThis = True
            while i < len(children) and inThis:
                tempName = children[i][1:children[i].find('_')] if children[i].startswith('{') else children[i]
                if tempName != self.children[i].name:
                    inThis = False
                i+=1
            return inThis
        else:
            return False
    def toString(self):
        s = ''
        for child in self.children:
            s += child.name + '[' + stringFeatures(child.features) + ']' + ', '
        return s[:-2]
        
def stringFeatures(featureStructure):
    s = ''
    for feature in featureStructure.keys():
        s += str(feature) + '=' + str(featureStructure[feature]) + ','
    s = s[:-1]
    return s

def whichNode(name,nodes):
    if name.startswith('{'):
        name = name[1:name.find('_')]
    i = 0
    while i < len(nodes) and nodes[i].name != name:
        i+=1
    if i >= len(nodes):
        return -1
    else:
        return i
    
def addTerminal(nodes,node):
    features = FeatStruct()
    for key in node.keys():
        if key in ['Person','Tense','Voice','Mood','Case','Number','Gender','Degree']:
            features = features.unify(FeatStruct('['+str(key)+'=\''+str(node.get(key))+'\']'))
    name = '{' + str(node.get('Cat')) + '_' + stringFeatures(features) + '}'
    nodeNumber = whichNode(name,nodes)
    if nodeNumber == -1:
        nodes.append(Terminal(name[1:name.find('_')],features))
        
def addNonTerminal(nodes,node):
    name=str(node.get('Cat')) + ('_'+ str(node.get('Rule')) if node.get('Rule')!=None else '') + ('_' + str(node.get('ClType')) if node.get('ClType')!=None else '')
    nodeNumber = whichNode(name,nodes)
    if nodeNumber == -1:
        nodes.append(NonTerminal(name))
        children = []
        for child in node.getchildren():
            if 'Unicode' in child.keys():
                features = FeatStruct()
                for key in child.keys():
                    if key in ['Person','Tense','Voice','Mood','Case','Number','Gender','Degree']:
                        features = features.unify(FeatStruct('['+str(key)+'=\''+str(child.get(key))+'\']'))
                children.append('{' + str(child.get('Cat')) + '_' + stringFeatures(features) + '}')
            else:
                children.append(str(child.get('Cat')) + ('_'+ str(child.get('Rule')) if child.get('Rule')!=None else '') + ('_' + str(child.get('ClType')) if child.get('ClType')!=None else ''))
        nodes[len(nodes)-1].addPath(children,nodes)
    else:
        children = []
        for child in node.getchildren():
            if 'Unicode' in child.keys():
                features = FeatStruct()
                for key in child.keys():
                    if key in ['Person','Tense','Voice','Mood','Case','Number','Gender','Degree']:
                        features = features.unify(FeatStruct('['+str(key)+'=\''+str(child.get(key))+'\']'))
                children.append('{' + str(child.get('Cat')) + '_' + stringFeatures(features) + '}')
            else:
                children.append(str(child.get('Cat')) + ('_'+ str(child.get('Rule')) if child.get('Rule')!=None else '') + ('_' + str(child.get('ClType')) if child.get('ClType')!=None else ''))
        nodes[nodeNumber].addPath(children,nodes)
        
def xmlToNodes(xmlFile):
    allNodes = []
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    for node in root.iter('Node'):
        if 'Unicode' in node.keys():
            addTerminal(allNodes,node)
        else:
            addNonTerminal(allNodes,node)
    return allNodes

def printCFG(allNodes,file=None):
    s = ''
    for node in allNodes:
#         print node.name + ' ' + str(len(node.childPaths) if isinstance(node,NonTerminal) else ' terminal')
        s += node.toString()
    if file == None:
        print s
    else:
        f = open(file,'w')
        f.write(s)
        f.close()

def runBuilder():
    nodes = xmlToNodes('65.xml')
    printCFG(nodes,'test2.xml')