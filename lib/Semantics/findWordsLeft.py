def findWordsLeft(unlabeled=False):
	d = {}
	labeled = set()
	for i in range(40,67):
		f = open(str(i)+'SEM.txt')
		lines = f.readlines()
		f.close()
		total = len(lines)
		j = 0
		while j < total:
			word = lines[j][lines[j].rfind(' ')+1:-1]
			if len(lines[j+1]) != 2:
				labeled.add(word)
			if len(lines[j+1]) == 2:
				if (unlabeled and word not in labeled) or not unlabeled:
					if word in d:
						d[word] += 1
					else:
						d[word] = 1
			j+=2
	return d

d = sorted(findWordsLeft(True).items(),key=lambda x: x[1])
s = ''
for item in d:
	if item[1] > 1:
		s += item[0] + ': ' + str(item[1]) + '\n'
f = open('test','w')
f.write(s)
f.close()