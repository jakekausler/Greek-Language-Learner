'''
Created on Jun 30, 2014

@author: Jake
'''


def combineLayouts(layoutStrings):
    s = set()
    for layout in layoutStrings:
        if layout[layout.find(',')+2:] in s:
            newS = set()
            for i in s:
                if i[1] == layout[layout.find(',')+2:]:
                    set.add((i[0] + '|' + layout[:layout.find(',')],i[1]))
                else:
                    newS.add(i)
                s = newS
        else:
            s.add((layout[:layout.find(',')],layout[layout.find(',')+2:]))
    return s
            
def getLayouts(input):
    f = open(input)
    lines = f.readlines()
    f.close()
    layoutStrings = []
    for line in lines:
        if line != '' and line != '\n':
            layoutStrings.append(line[:-1])
    return layoutStrings

def writeLayouts(layouts,output):
    f = open(output,'w')
    s = ''
    for layout in layouts:
        s += layout[0] + '---' + layout[1] + '\n'
    f.write(s)
    f.close()
    
def readAndWriteLayouts(input,output):
    writeLayouts(combineLayouts(getLayouts(input)),output)