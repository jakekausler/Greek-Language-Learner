import xml.etree.ElementTree as ET

for i in range(40,67):
    f = open(str(i)+'Sem.txt')
    labels = f.readlines()
    f.close()
    labelDict = {}
    j=0
    previousVerse = 0
    k = 0
    # s = ''
    while j < len(labels):
        # print labels[j]
        if int(previousVerse) != int(labels[j][4:6]):
            k = 0
            previousVerse = labels[j][4:6]
        k += 1
        labelDict[labels[j][:labels[j].find(' ')]+(('0'+str(k)) if k<10 else str(k))] = labels[j+1][1:-1]
        # s += labels[j][:labels[j].find(' ')]+(('0'+str(k)) if k<10 else str(k)) + ' ' + labels[j][labels[j].find(' ')+1:] + '\n'
        j+=2
    # f = open('test','w')
    # f.write(s)
    # f.close()

    f = str(i)+'.xml'
    tree = ET.parse('../sentenceLayouts/'+f)
    root = tree.getroot()
    for node in root.iter('Node'):
        if node.get('morphId') != None:
            j = node.get('morphId')
            book = ('0'+str(int(i)-39)) if int(i)-39<10 else str(int(i)-39)
            chapter = j[3:5]
            verse = j[6:8]
            word = j[9:]
            code = book+chapter+verse+word
            # print code
            if code in labelDict:
                node.set('Domain',labelDict[code])
        if node.get('Rule') == None:
            node.set('Rule',node.get('Cat'))
        t = []
        for key in node.attrib:
            if key not in ['Head','Cat','Rule','Domain','Case','Gender','Number','Person','Voice','Tense','Mood']:
                t.append(key)
        for key in t:
            del node.attrib[key]
    tree.write(f,'utf-8')
    print 'Finished',i,'of',66