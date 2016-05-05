# -*- coding: utf-8 -*-
def makeSemanticLexicon(start,stop):
	lexicon = {}
	for i in range(start,stop+1):
		f = open(str(i)+'Sem.txt')
		lines = f.readlines()
		f.close()
		j = 0
		while j < len(lines):
			pos = lines[j][lines[j].find(' ')+1:lines[j].find(' ')+2]
			word = lines[j][lines[j].rfind(' ')+1:-1]
			domain = lines[j+1][1:-1]
			if pos not in lexicon.keys():
				lexicon[pos] = {}
			if domain not in lexicon[pos].keys():
				lexicon[pos][domain] = {}
			if word not in lexicon[pos][domain]:
				lexicon[pos][domain][word] = 0
			lexicon[pos][domain][word] += 1
			j+=2
	return lexicon

def reverseFindNth(needle,haystack,n):
	for i in range(n):
		haystack = haystack[0:haystack.rfind(needle)]
	return len(haystack)

def stringLexicon(lexicon):
	s = ''
	for pos in lexicon.keys():
		s += pos + '\n'
		for domain in lexicon[pos].keys():
			s += '\t' + domain + '\n'
			for word in lexicon[pos][domain].keys():
				s += '\t\t' + word + ':' + str(lexicon[pos][domain][word]) + '\n'
		s += '\n'
	return s

def writeSemanticLexicon(start,stop,output):
	f = open(output,'w')
	f.write(stringLexicon(makeSemanticLexicon(start,stop)))
	f.close()

writeSemanticLexicon(40,42,'lexicon')