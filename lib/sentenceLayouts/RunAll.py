# -*- coding: utf-8 -*-
'''
Created on Jun 24, 2014

@author: Jake
'''
import Editor,GUI,CreateCFG,SentenceModelMaker,WordFrequencyCounter,LayoutCombiner
import time

def makeFullCFG(input,output):
    GUI.runGUI(input,'test.xml')
    Editor.runEditor('test.xml','test2.xml')
    CreateCFG.writeCFGs('test2.xml',output)
    
def makeSentenceModels(input,output):
    SentenceModelMaker.makeModels(input, output)
    
def makeWordFrequencies(listOfInputs,output):
    WordFrequencyCounter.allWrites(listOfInputs, output)
    
def makePOSWordFrequencies(listOfInputs):
    WordFrequencyCounter.allWritePOSFrequencies(listOfInputs)

def readAndWriteLayouts(input,output):
    LayoutCombiner.readAndWriteLayouts(input, output)
    
# start = time.time()
# for i in range(65,66):
#     makeFullCFG(str(i)+'.xml','cfgs')
#     print "Completed file " + str(i) + " of 66"
# end = time.time()
# print "finished in " + str(end-start) + " seconds"

# start = time.time()
# for i in range(40,67):
#     makeSentenceModels(str(i)+'.xml','test.xml')
#     print "Completed file " + str(i) + " of 66"
# end = time.time()
# print "finished in " + str(end-start) + " seconds"

# files = []
# for i in range(40,67):
#     files.append(str(i)+'.xml')
# makeWordFrequencies(files,'test.xml')

# files = []
# for i in range(40,67):
#     files.append(str(i)+'.xml')
# makePOSWordFrequencies(files)

# readAndWriteLayouts('../generators/models','test')