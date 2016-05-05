'''
Created on Oct 22, 2014

@author: Jake
'''
f = open('grammar.fcfg')
lines = f.readlines()
f.close()
s = set()
for line in lines:
    if line.find('{') != -1:
        line = line[line.find('{')+1:]
        s.add(line[:line.find('_')])
print s