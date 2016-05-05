# -*- coding: utf-8 -*-
import worker

def labelAll():
	# NumToRead - Number of books labeled
	words,labels = worker.makeWordAndLabelDicts()
	for i in range(40,67):
		f = open(str(i)+'Sem.txt')
		lines = f.readlines()
		f.close()
		j = 0
		while j < len(lines):
			if len(lines[j+1]) == 2:
				lines[j+1] = labelLine(lines[j],words,labels)
			j+=2
		s = ''
		for line in lines:
			s += line
		f = open(str(i)+'Sem.txt','w')
		f.write(s)
		f.close()

def labelLine(line,words,labels):
	s = '\t'
	word = line[line.rfind(' ')+1:-1]
	if word in words and len(words[word]) == 1:
		s += words[word][0]
	return s+'\n'

labelAll()