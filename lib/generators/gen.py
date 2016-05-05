# -*- coding: utf-8 -*-
'''
Created on Jun 8, 2014

@author: Jake
'''
import random
s=''
# for k in [1,2,3,4,5,6]:
#     for j in [1,2]:
#         for i in [1,2,3]:
#             for h in [1,2,3]:
#                 for g in [1,2,3,4,5,6,7,8,9]:
#                     for f in [1,2,3]:
#                         for e in [1,2,3,4]:
#                             for d in ['','εἶπον']:
#                                 s+= 'verb[mood=' + str(k) + ',number=' + str(j) + ',person=' + str(i) + ',voice=' + str(h) + ',tense=' + str(g) + ',gender=' + str(f) + ',case=' + str(e) + ',verb=' + str(d) +'] --> {verb_=' + 'm=' + str(k) + ',n=' + str(j) + ',p=' + str(i) + ',v=' + str(h) + ',t=' + str(g) + ',g=' + str(f) + ',c=' + str(e) + ',vb=' + str(d) + '}\n'
# for k in [1,2,3,4,5,6]:
#     for j in [1,2]:
#         for i in [1,2,3]:
#             for h in [random.choice([1,2,3])]:
#                 for g in [random.choice([1,2,3,4,5,6,7,8,9])]:
#                     for f in [1,2,3]:
#                         for e in [random.choice([1,2,3,4])]:
#                             for d in [0,1]:
#                                 s+= 'verb[mood=' + str(k) + ',number=' + str(j) + ',person=' + str(i) + ',voice=' + str(h) + ',tense=' + str(g) + ',gender=' + str(f) + ',case=' + str(e) + ',verb=' + str(d) +'] --> {verb_=' + 'm=' + str(k) + ',n=' + str(j) + ',p=' + str(i) + ',v=' + str(h) + ',t=' + str(g) + ',g=' + str(f) + ',c=' + str(e) + ',vb=' + str(d) + '}\n'
# for l in range(1000):
#     k = random.choice([1,2,3,4,5,6])
#     j = random.choice([1,2])
#     i = random.choice([1,2,3])
#     h = random.choice([1,2,3])
#     g = random.choice([1,2,3,4,5,6,7,8,9])
#     f = random.choice([1,2,3])
#     e = random.choice([1,2,3,4])
#     s+= 'verb[mood=' + str(k) + ',number=' + str(j) + ',person=' + str(i) + ',voice=' + str(h) + ',tense=' + str(g) + ',gender=' + str(f) + ',case=' + str(e) + '] --> {verb_=' + 'm=' + str(k) + ',n=' + str(j) + ',p=' + str(i) + ',v=' + str(h) + ',t=' + str(g) + ',g=' + str(f) + ',c=' + str(e) + '}\n'
# f = open('test','r+')
# f.write(s)
# f.close() 

s = set()
lines = open('../Lexicons/verbs').readlines()
for line in lines:
    if line.startswith('\t\t'):
        s.add(line[line.rfind('\t')+1:-1])
t = ''
for item in s:
    t += str(item) + '\n'
f = open('test','r+')
f.write(t)
f.close()