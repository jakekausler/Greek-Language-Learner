# -*- coding: utf-8 -*-

def reverseFindNth(needle,haystack,n):
	for i in range(n):
		haystack = haystack[0:haystack.rfind(needle)]
	return len(haystack)

def makeWordAndLabelDicts():
	# NumToRead - Number of books labeled
	words = {}
	labels = {}
	for i in range(40,67):
		f = open(str(i)+'Sem.txt')
		lines = f.readlines()
		f.close()
		end = len(lines)
		j = 0
		while j < end:
			# word = (lines[j][lines[j].rfind(' ')+1:-1],lines[j][reverseFindNth(' ',lines[j],4)+1:reverseFindNth(' ',lines[j],3)])
			word = lines[j][lines[j].rfind(' ')+1:-1]
			if len(lines[j+1]) > 2:
				label = lines[j+1][1:-1] if lines[j+1].find(',') == -1 else lines[j+1][1:lines[j+1].find(',')]
			else:
				label = -1
			# if word in words:
				# if label not in words[word]:
				# 	words[word][label] = 1
				# else:
				# 	words[word][label] += 1
			# else:
			# 	words[word] = {}
			# 	words[word][label] = 1
			if word in words:
				if label != -1 and label not in words[word]:
					words[word].append(label)
			else:
				words[word] = [label] if label != -1 else []
			if label in labels:
				if word not in labels[label]:
					labels[label].append(word)
			else:
				labels[label] = [word]
			j+=2
	return (words,labels)

# words = makeWordAndLabelDicts(2)[0]
# s = ''
# for word in sorted(words.items(),key=lambda x: x[0]):
# 	if len(words[word[0]]) > 1:
# 		s += word[0] + ':' + '\n'
# 		for label in words[word[0]]:
# 			s += '\t' + label  + ' : ' + str(words[word[0]][label]) + '\n'

# f = open('test','w')
# f.write(s)
# f.close()