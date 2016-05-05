def mergefiles(newfile,oldfile,output):
	f = open(newfile)
	l1 = f.readlines()
	f.close()
	f = open(oldfile)
	l2 = f.readlines()
	f.close()
	s = ''
	i = 0
	j = 1
	while i < len(l1):
		s += l1[i] + l2[j]
		i+=1
		j+=2
	f = open(output,'w')
	f.write(s)
	f.close()

mergefiles('test','42Sem.txt','test2')