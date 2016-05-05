from SemanticGenerator import makeSentences as makeSentencesSemantic
from SentenceGenerator import autogenerateSentencesFromModelFile as makeSentencesModelled
import calendar,time,sys

start = calendar.timegm(time.gmtime())
reload(sys)
sys.setdefaultencoding('utf-8')
i=0
while i < 20:
	print i
	t = ''
	sentences = makeSentencesModelled(10,False)
	for sentence in sentences:
		sentence = sentence[0]
		try:
			s = ''
			for word in sentence:
				s += word + ' '
			t += s[:-1] + '\n'
		except TypeError:
			s = ''
	i+=1
	f = open('sentences','a')
	f.write(t)
	f.close()
	end = calendar.timegm(time.gmtime())
	print i*10,'of',200,'after',end-start,'seconds'