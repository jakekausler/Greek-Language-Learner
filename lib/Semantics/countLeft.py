import sys

def countLeft(start,finish):
	left = 0
	total = 0
	for i in range(start,finish+1):
		f = open(str(i)+'Sem.txt')
		lines = f.readlines()
		f.close()
		j = 0
		while j < len(lines):
			total += 1
			if len(lines[j+1]) == 2:
				left += 1
			j+=2
	return ('left: '+str(left),'labeled: '+str(total-left),'total: '+str(total),'percent-left: '+str((float(left)/float(total))*100),'percent-done: '+str(100-(float(left)/float(total))*100))

start = 40 if len(sys.argv) != 3 else int(sys.argv[1])
end = 66 if len(sys.argv) != 3 else int(sys.argv[2])
for thing in countLeft(start,end):
	print thing