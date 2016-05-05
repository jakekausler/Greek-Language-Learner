# -*- coding: utf-8 -*-
'''
Created on Jun 23, 2014

@author: Jake
'''
import xml.etree.ElementTree as ET
from Tkinter import Tk, Frame, BOTH, Button, Canvas, LAST, VERTICAL, HORIZONTAL, Scrollbar,LEFT,RIGHT,BOTTOM,X,Y,CENTER
import ImageFont

def countNodeWidth(node):
    if len(node.getchildren()) == 0:
        return 1
    else:
        width = 0
        for child in node.getchildren():
            width += countNodeWidth(child)
        return width
    
def countNodeDepth(node,parent_map):
    depth = 0
    while parent_map[node].tag != 'Tree':
        depth += 1
        node = parent_map[node]
    return depth

def printTree(node,totalwidth,d={}):
    if int(node.get("Depth")) in d.keys():
        d[int(node.get("Depth"))] = list(d[int(node.get("Depth"))])
        d[int(node.get("Depth"))][int(node.get('Start')) if node.get('Start') != None else int(node.getchildren()[0].get('Start'))] = '+'
        d[int(node.get("Depth"))] = "".join(d[int(node.get("Depth"))])
    else:
        d[int(node.get("Depth"))] = ''
        for i in range(totalwidth):
            d[int(node.get("Depth"))] += '-'
        d[int(node.get("Depth"))] = list(d[int(node.get("Depth"))])
        d[int(node.get("Depth"))][int(node.get('Start')) if node.get('Start') != None else int(node.getchildren()[0].get('Start'))] = '+'
        d[int(node.get("Depth"))] = "".join(d[int(node.get("Depth"))])
    for child in node.getchildren():
        d = printTree(child,totalwidth,d)
    return d

def createDictionary(node,totalwidth,d={}):
    if int(node.get("Depth")) in d.keys():
        d[int(node.get("Depth"))][int(node.get('Start')) if node.get('Start') != None else int(node.getchildren()[0].get('Start'))] = node.get('nodeId')
    else:
        d[int(node.get("Depth"))] = []
        for i in range(totalwidth):
            d[int(node.get("Depth"))].append('')
        d[int(node.get("Depth"))][int(node.get('Start')) if node.get('Start') != None else int(node.getchildren()[0].get('Start'))] = node.get('nodeId')
    for child in node.getchildren():
        d = createDictionary(child,totalwidth,d)
    return d

class NodeImage(Button):
    def __init__(self, master=None, x=0, y=0, t='', width=100, height=100, paddingX=20, paddingY=20, cnf={}, **kw):
        Button.__init__(self, master=master, text=t, cnf=cnf, **kw)
        self.x = x*width+x*paddingX
        self.y = y*height+y*paddingY
        self.width = width
        self.height = height
        self.padX = paddingX
        self.padY = paddingY
        self.place(x=self.x,y=self.y,width=self.width,height=self.height)

class CanvasWindow(Canvas):
    def __init__(self,parent,dictionary,rootNode,buttonWidth,buttonHeight,buttonPadX,buttonPadY,font,fontSize):
        sr = self.calculateDimensions(dictionary,buttonWidth,buttonHeight,buttonPadX,buttonPadY)
        Canvas.__init__(self, parent,scrollregion=sr)
        self.addButtons(dictionary,rootNode,buttonWidth,buttonHeight,buttonPadX,buttonPadY,font,fontSize)
        
    def addButtons(self,dictionary,rootNode,buttonWidth,buttonHeight,buttonPadX,buttonPadY,font,fontSize):
        buttons = []
        lines = []
        for key in dictionary.keys():
            for node in dictionary[key]:
                if node != '':
                    l = list(rootNode.iter("Node"))
                    selected = None
                    i = 0
                    while selected == None and i < len(l):
                        if l[i].get("nodeId") == node:
                            selected = l[i]
                        i+=1
                    buttons.append((int(selected.get("Start")) if selected.get("Start")!=None else int(selected.getchildren()[0].get("Start")),key,formText(selected)))
                    for child in selected.getchildren():
                        lines.append((int(selected.get("Start") if selected.get("Start") != None else selected.getchildren()[0].get('Start')),key,int(child.get("Start")),key+1))
        self.addButtonsToScreen(buttons,buttonWidth,buttonHeight,buttonPadX,buttonPadY,font,fontSize)
        self.addLines(lines,buttonWidth,buttonHeight,buttonPadX,buttonPadY)
    def addLines(self,lines,bwidth,bheight,padX,padY,width=1):
        for line in lines:
            x1 = line[0]*bwidth+line[0]*padX+bwidth/2+padX
            y1 = line[1]*bheight+line[1]*padY+bheight+padY
            x2 = x1
            y2 = line[1]*bheight+line[1]*padY+bheight+padY/2+padY
            x3 = line[2]*bwidth+line[2]*padX+bwidth/2+padX
            y3 = y2
            x4 = x3
            y4 = line[3]*bheight+line[3]*padY+padY
            self.create_line(x1,y1,x2,y2,x3,y3,x4,y4,width=str(width)+'p')
    def calculateDimensions(self,dictionary,bw,bh,bpx,bpy):
        height = max(dictionary.keys())
        width = len(dictionary[dictionary.keys()[0]])
        return (0,0,width*bw+width*bpx+bw+bpx-bw,height*bh+height*bpy+bh+bpy*2)
    def addButtonsToScreen(self,buttons,bw,bh,bpx,bpy,font,fontSize):
        for button in buttons:
            self.create_rectangle(button[0]*bw+button[0]*bpx+bpx,button[1]*bh+button[1]*bpy+bpx,button[0]*bw+button[0]*bpx+bw+bpx,button[1]*bh+button[1]*bpy+bh+bpy)
            self.create_text(button[0]*bw+button[0]*bpx+bw/2+bpx,button[1]*bh+button[1]*bpy+bh/2+bpy,text=button[2],font=(font,fontSize),justify=CENTER)
class Window(Frame):
    def __init__(self,parent,dictionary,rootNode,font='ARIAL.TTF',fontSize=12):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI(dictionary,rootNode,font,fontSize)
    def initUI(self,dictionary,rootNode,font,fontSize):
        self.parent.title("Sentence Tree")
        self.pack(fill=BOTH, expand=1)
        
        canvas = CanvasWindow(self,dictionary,rootNode,self.getButtonWidth(dictionary,rootNode,font,fontSize),self.getButtonHeight(dictionary,rootNode,font,fontSize),20,20,font,fontSize)
        
        vbar = Scrollbar(self,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=canvas.yview)
        hbar = Scrollbar(self,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=canvas.xview)
        
        canvas.config(width=300,height=300)
        canvas.config(xscrollcommand=hbar.set,yscrollcommand=vbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)
    def getButtonWidth(self,dictionary,root,font,fontSize):
        maxWidth = 0
        font = ImageFont.truetype(font,fontSize)
        for key in dictionary:
            for node in dictionary[key]:
                if node != '':
                    l = list(root.iter("Node"))
                    selected = None
                    i = 0
                    while selected == None and i < len(l):
                        if l[i].get("nodeId") == node:
                            selected = l[i]
                        i+=1
                    for line in formText(selected).split('\n'):
                        if font.getsize(line)[0]+fontSize*3 > maxWidth:
                            maxWidth = font.getsize(line)[0]+fontSize*3
        return maxWidth/2
    def getButtonHeight(self,dictionary,root,font,fontSize):
        maxHeight = 0
        font = ImageFont.truetype(font,fontSize)
        for key in dictionary:
            for node in dictionary[key]:
                if node != '':
                    l = list(root.iter("Node"))
                    selected = None
                    i = 0
                    while selected == None and i < len(l):
                        if l[i].get("nodeId") == node:
                            selected = l[i]
                        i+=1
                    selected = formText(selected).split('\n')
                    if font.getsize(selected[0])[1]*len(selected)+len(selected)*(fontSize/3*2) > maxHeight:
                        maxHeight = font.getsize(selected[0])[1]*len(selected)+len(selected)*(fontSize/3*2)
        return maxHeight

def formText(node):
    code = str(node.get('nodeId')) + '\n'
    name = str(node.get('Cat')) + ('_'+ str(node.get('Rule')) if node.get('Rule')!=None else '') + ('_' + str(node.get('ClType')) if node.get('ClType')!=None else '') + '\n'
    features = ''
#     for feature in ['Person','Tense','Voice','Mood','Case','Number','Gender','Degree']:
#         features += feature + '='
#         if node.get(feature) != None:
#             features += node.get(feature) + '\n'
#         else:
#             features += '\n'
#     unicode = 'Unicode=' + (node.get('Unicode') if node.get('Unicode') != None else '')
    unicode = node.get('Unicode') if node.get('Unicode') != None else ''
    return name + features + unicode.encode('utf-8')

def runGUI(input,output):
    tree = ET.parse(input)
    root = tree.getroot()
    
    parent_map = dict((c, p) for p in tree.getiterator() for c in p)
    
    for node in root.iter("Node"):
        node.set('Depth',str(countNodeDepth(node,parent_map)))
    tree.write(output,'utf-8')

# tree = ET.parse('test2')
# root = tree.getroot()
#   
# d = createDictionary(list(root.iter("Node"))[0],int(list(root.iter("Node"))[0].get('End'))+1 if list(root.iter("Node"))[0].get('End') != None else int(list(root.iter("Node"))[0].getchildren()[0].get('End'))+1)
# 
# main = Tk()
# w, h = 300,300
# main.geometry("%dx%d+0+0" % (w, h))
# main.update()
# app = Window(main,d,root,'ARIAL.TTF',9)
# main.mainloop()

# d = printTree(list(root.iter("Node"))[0],int(list(root.iter("Node"))[0].get('End'))+1 if list(root.iter("Node"))[0].get('End') != None else int(list(root.iter("Node"))[0].getchildren()[0].get('End'))+1)

# s = ' '
# for i in range(17):
#     s += " " + str(i) if i >= 10 else "  " + str(i)
# print s
# for i in range(len(d.keys())):
#     d[i] = list(d[i])
#     d[i] = "  ".join(d[i])
#     print i if i >= 10 else " " + str(i),d[i]