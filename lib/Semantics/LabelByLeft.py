def labelByLeft(input='test'):
	d = {}
	f = open(input)
	lines = f.readlines()
	f.close()
	for line in lines:
		if line.find(',') != -1:
			d[line[:line.find(':')]] = line[line.find(',')+1:-1]
	for i in range(40,67):
		f = open(str(i)+'Sem.txt')
		lines = f.readlines()
		f.close()
		total = len(lines)
		j = 0
		while j < total:
			if len(lines[j+1]) == 2 and lines[j][lines[j].rfind(' ')+1:-1] in d:
				lines[j+1] = '\t' + d[lines[j][lines[j].rfind(' ')+1:-1]] + '\n'
			j+=2
		s = ''
		for line in lines:
			s += line
		f = open(str(i)+'Sem.txt','w')
		f.write(s)
		f.close()

labelByLeft()