f = open('lexicon')
lines = f.readlines()
f.close()

d = {}

for line in lines:
	if not line.startswith('\t'):
		d[line[:-1]] = set()
		curr = line[:-1]
	if line.startswith('\t') and not line.startswith('\t\t'):
		d[curr].add(line[1:-1])

t = ''
for key in d:
	t += key + '\n'
	for i in d[key]:
		t += '\t' + i + '\n'
f = open('domains2','w')
f.write(t)
f.close()