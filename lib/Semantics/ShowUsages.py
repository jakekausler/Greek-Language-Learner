'''
Created on Jul 3, 2014

@author: Jake
'''
import xml.etree.ElementTree as ET

# s = set()
# for i in range(40,41):
#     tree = ET.parse(str(i)+'.xml')
#     root = tree.getroot()
#     for node in root.iter('Node'):
#         if node.get('Rule') != None:
#             s.add(node.get('Rule'))
#           
# t = ''
# for i in s:
#     t += i + '\n'
#      
# f = open('test','w')
# f.write(t)
# f.close()

def getChildren(node):
    if node.get('Rule') != None:
        if len(node.getchildren()) >= 1:
            children = []
            for i in range(len(node.getchildren())):
                # children.append(node.getchildren()[i].get('Rule')+'('+getHead(node.getchildren()[i])+')')
                children.append(node.getchildren()[i])
            return children
    return None
            
def getHead(node):
    if len(node.getchildren()) == 0:
        return node.get('Domain')
    else:
        head = int(node.get('Head'))
        return getHead(node.getchildren()[head])

def findInCommon(nodes):
    attribs = set()
    for node in nodes:
        for attr in ['Case','Gender','Number','Person','Voice','Tense','Mood']:
            if node.get(attr) != None:
                attribs.add(attr)
    addDict = {}
    for attr in attribs:
        i = 0
        adding = True
        value = None
        while i < len(nodes) and adding:
            if value == None:
                value = nodes[i].get(attr)
            elif nodes[i].get(attr) != None and nodes[i].get(attr) != value:
                adding = False
            i+=1
        if adding and value != None: #add value and make sure the value is listed as nonspecific (?c,?n,etc.)
            if attr == 'Case':
                value = '\'?c\''
            elif attr == 'Gender':
                value = '\'?g\''
            elif attr == 'Number':
                value = '\'?n\''
            elif attr == 'Person':
                value = '\'?p\''
            elif attr == 'Voice':
                value = '\'?v\''
            elif attr == 'Tense':
                value = '\'?t\''
            elif attr == 'Mood':
                value = '\'?m\''
            addDict[attr] = value
    return addDict

def makeTerminalStatement(node):
    feat = ''
    attribs = ['Case','Gender','Number','Person','Voice','Tense','Mood']
    for attr in attribs:
        if node.get(attr) != None:
            feat += attr + '=\'' + node.get(attr) + '\','
    if feat != '':
        feat = ',' + feat[:-1]
    s = child.get('Cat') + '[Domain=\'' + child.get('Domain') + '\'' + feat + '] --> {' + child.get('Cat') + '_' + 'Domain=\'' + child.get('Domain') + '\'' + feat + '}\n'
    return s

def makeFieldString(commonFields):
    fs = ',' if len(commonFields.keys())>0 else ''
    for key in commonFields:
        fs += key + '=' + commonFields[key] + ','
    fs = fs[:-1]
    return fs

s = ''
rules = set()
for i in range(40,43):
    tree = ET.parse(str(i)+'.xml')
    root = tree.getroot()
    for sent in root.iter('Sentence'):
        # s += '\n' + sent.get('ID') + '\n\n'
        for node in sent.iter('Node'):
            children = getChildren(node)
            if children != None:
                commonFields = findInCommon(children)
                fieldString = makeFieldString(commonFields)
                t = ''
                t += node.get('Rule') + '[' + 'Domain=\'' + getHead(node) + '\'' + fieldString + '] --> '
#                 t += node.get('Rule') + ' --> '
                j=0
                for child in children:
#                     t += child.get('Rule') + ', '
                    if str(j) == node.get('Head'):
                        t += child.get('Rule')+'-Head['+'Domain=\''+getHead(child)+'\''+fieldString+']' + ', '
                    else:
                        t += child.get('Rule')+'['+'Domain=\''+getHead(child)+'\''+fieldString+']' + ', '
                    j += 1
                t = t[:-2] + '\n'
                for child in children:
                    if len(child.getchildren()) == 0:
#                         k = child.get('Cat') + ' --> {' + child.get('Cat') + '}\n' 
                        k = makeTerminalStatement(child)
                        rules.add(k)
                rules.add(t)
    print 'finished ' + str(i)
for r in rules:
    s += r

f = open('grammar.fcfg','w')
f.write(s)
f.close()