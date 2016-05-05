# -*- coding: utf-8 -*-
'''
Created on Jun 6, 2014

@author: Jake

Form sentence models from a feature-based CFG file.
'''
import random
from nltk.featstruct import FeatStruct

class Terminal:
    '''A terminal node, i.e. one without any children.
    
    Attributes:
    name -- Name of the node (e.g. verb_n=2,m=1...)
    '''
    
    def __init__(self,n):
        '''Initialize the node.
        
        Keyword arguments:
        n -- Name of the node
        '''
        self.name=n
        
    def toString(self):
        '''Return the name of the node.'''
        return self.name

class NonTerminal:
    '''A non-terminal node, i.e. one with children.
    
    Attributes:
    name -- Name of the node (e.g. verb_n=2,m=1...)
    children[] -- Child nodes of this node (i.e. the right hand side
                  of the grammar). Each element in the list contains a
                  seperate 'line' of the grammar. For example, in the
                  following
                      nounClause --> det, noun.
                      nounClause -- > noun.
                  the first line would be children[0] and the second
                  children[1]. Each element of the children elements
                  contains the nodes of the respective line, so
                  children[0][0] would be the 'det' node, and
                  children[0][1] and children[1][0] the 'noun' node.
    childFeatures[] -- Features of this node and the children. Each
                       element represents a 'line' of the grammar. For
                       example, in the following
                           nounClause[person=?p] --> det[] noun[person=?p].
                           nounClause[number=?n] --> noun[number=?n].
                       childFeatures[0] represents the first line and
                       childFeatures[1] represents the second. In each
                       line, the sub-elements are the feature
                       structures moving across from left-to-right.
                       So, childFeatures[0][0] would be the
                       FeatStruct('person=?p') for the nounClause
                       head, childFeatures[0][1] the empty
                       FeatStruct() for det, and so on. 
    '''
    
    def __init__(self,n):
        '''Initialize the node.
        
        Keyword arguments:
        n -- Name of the node.
        '''
        self.name=n
        self.children=[]
        self.childFeatures=[]
        
    def addChildren(self,s,nodes,headFeature):
        '''Add children to the node, based on a single line from the
        grammar.
        
        Keyword arguments:
        s -- List of children to be analyzed (each token after the
             '-->' in the grammar, separated by ', ').
        nodes -- The nodes from which child nodes will be drawn from.
        headFeature -- The feature of the head of the line (the
                       FeatStruct of the left-hand-side).
        '''
        
        # Add a new 'child' to the node, representing a line from the
        # grammar. Also, add a new set of child features,
        # corresponding to the new 'path' with a head of headFeature.
        self.children.append([])
        self.childFeatures.append([headFeature])
        
        # Add every token given.
        for k in s:
            i=0
            inNodes=0
            name = k[:k.find('[')] if k.find('[')!=-1 else k # The name of the token is everything up to the '[' if a '[' is found, otherwise it is just the token itself.
            # Go through the nodes and see if the token is in them. If
            # so, add the respective node as the child.
            while i<len(nodes) and inNodes==0:
                if nodes[i].name==name:
                    inNodes = 1;
                    self.children[len(self.children)-1].append(nodes[i])
                    newFeature = FeatStruct(k[k.find('['):]) if k.find('[')!=-1 else FeatStruct()
                    self.childFeatures[len(self.childFeatures)-1].append(newFeature)
                i+=1
            
            # If the token was not in the nodes, add it to the nodes
            # and match it to the child.
            if inNodes==0:
                if k.startswith('{') and k.endswith('}'): # If the token is a terminal
                    n = Terminal(name)
                    nodes.append(n)
                    self.children[len(self.children)-1].append(n)
                    newFeature = FeatStruct()
                    self.childFeatures[len(self.childFeatures)-1].append(newFeature)
                else: # If the token is not a terminal
                    n = NonTerminal(name)
                    nodes.append(n)
                    self.children[len(self.children)-1].append(n)
                    newFeature = FeatStruct(k[k.find('['):]) if k.find('[') else FeatStruct()
                    self.childFeatures[len(self.childFeatures)-1].append(newFeature)
                    
    def toString(self):
        '''Return a string representing each child, or 'line', of the
        node in feature-based CFG format.
        '''
        
        s = ''
        for i in range(len(self.children)):
            s += self.name + str(self.childFeatures[i][0]).replace('\n','') + ' --> '
            for j in range(len(self.children[i])):
                s += self.children[i][j].name + str(self.childFeatures[i][j+1]).replace('\n','') + ', '
            s = s[:-2]
            s += '\n'
        return s

def readCFG(string):
    '''Read a feature-based CFG to a list of nodes, returning the list of nodes.
    
    Keyword arguments:
    string -- String of the feature-based CFG to read
    '''
    
    # Array the string and add new lines to the end of each
#     lines = string.split('\n')
#     for l in lines:
#         l += '\n'

    f = open('Grammar.fcfg')
    lines = f.readlines()
    f.close()
        
    allNodes = []
    
    #For every line in the file, add it to the nodes
    for l in lines:
        if (len(l) > 1 and l[0] != '#'): #If the line is not blank and not a comment
            i=0
            inNodes=0
            p = l[l.find('>')+2:l.find('.')].split(', ') #The tokens of the right-hand-side of the line
            name = l[0:l.find('[')] if (l.find('[')!=-1) and (l.find('[') < l.find(' ')) else l[0:l.find(' ')] #The name of the left-hand token, which is up to the first '[' if there is one before the '-->', otherwise it is simply the token itself 
            
            # See if the left-hand token is in the list of nodes.
            while i<len(allNodes) and inNodes==0:
                # If the left-hand token is in the list of nodes
                if allNodes[i].name==name:
                    inNodes=1
                    j=0
                    inChildren=0
                    # See if the right-hand 'path' is listed in the
                    # head node's children
                    while j < len(allNodes[i].children) and inChildren==0:
                        if len(p) == len(allNodes[i].children[j]):
                            k = 0
                            inChildren = 1
                            while k < len(p) and inChildren==1:
                                pName = p[k][:p[k].find('[')] if (p[k].find('[')) else p[k]
                                if pName != allNodes[i].children[j][k].name:
                                    inChildren = 0
                                k+=1
                        j+=1
                    # If the 'path' is not in the head node's children, add it as a child
                    if inChildren==0:
                        head = FeatStruct() if name==l[0:l.find(' ')] else FeatStruct(l[l.find('['):l.find(' ')])
                        allNodes[i].addChildren(p,allNodes,head)
                i+=1
            # If the left-hand token is not in the nodes, add it
            if inNodes==0:
                n = NonTerminal(name)
                allNodes.append(n)
                head = FeatStruct() if name==l[0:l.find(' ')] else FeatStruct(l[l.find('['):l.find(' ')])
                allNodes[len(allNodes)-1].addChildren(p,allNodes,head)
    return allNodes

def printCFG(allNodes):
    '''Print the grammar represented by a list of nodes.
    
    Keyword arguments:
    allNodes -- The nodes representing the grammar.
    '''
    
    for n in allNodes:
        if isinstance(n,NonTerminal):
            print n.toString()

def generateFB(sent,node,fs,maxDepth=3,currentDepth=0,previousNode=None):
    '''.
    
    Keyword arguments:
    sent -- The sentence in its current state (words are filled in as
            it goes). It should start with [].
    node -- The node representing the starting state of the grammar
            (probably the sentence node).
    fs -- The feature structure of the previous call. It should start
          with the feature structure of the starting state of the
          grammar.
    maxDepth -- The maximum depth for traversal on recursive clauses
                (default is 3).
    currentDepth -- The current depth of traversal on a recursive
                    clause (default is 0, as it should be for starting)
    previousNode -- The node that the recursion is counting (default
                    is None). If the current node is different from
                    the previous node, the count can reset.
    '''
    
    # If the node is a terminal, add it to the sentence if the feature
    # structure is not None (if it were none, it would mean it didn't
    # work with the current choices.
    if isinstance(node,Terminal):
        if fs!=None:
            print 'Added ' + node.name + ' to the sentence with fs ' + str(fs).replace('\n','').replace(' ','')
            sent.append(node.name)
        print 'Failed to add ' + node.name + ' to the sentence because fs was null'
        return [sent,fs]
    # If the node is not a terminal, recursively build the sentence
    else:
        # Check the node to see if recursion applies
        if previousNode!=None and node.name==previousNode.name:
            print 'The current node ' + node.name + ' is the same as the previous node. Added one to the depth'
            currentDepth+=1
        else:
            if previousNode == None:
                print 'The previousNode is blank. Reset the depth.'
            else:
                print 'The current node ' + node.name + ' is not the same as the previous node ' + previousNode.name + '. Reset the depth.'
            currentDepth=0
        i=0
        paths = []
        print 'Starting to add paths.'
        # Add 'paths' from the node's children that can work with the
        # current feature structure to be used when recursively
        # looking for the path to take (randomly chosen)
        while i<len(node.children):
            j=0
            works=1
            while j<len(node.children[i]) and works!=0:
                if (node.childFeatures[i][j+1]!=None and fs!=None) and node.childFeatures[i][j+1].unify(fs) != None:
                    print 'The node ' + node.name + ' had child features ' + str(node.childFeatures[i][j+1]).replace('\n','').replace(' ','') + ' for child ' + node.children[i][j].name + ' that successfully merged with fs ' + str(fs).replace('\n','').replace(' ','')
                    if currentDepth >= maxDepth and previousNode !=None and node.children[i][j].name==previousNode.name:
                        print 'The maximum depth would be exceeded if this path were chosen.'
                        works=0
                    else:
                        print 'This child works in the path. Moving to the next child.'
                        j+=1
                else:
                    print 'The node ' + node.name + ' had child features ' + str(node.childFeatures[i][j+1]).replace('\n','').replace(' ','') + ' that did not merge with fs ' + str(fs).replace('\n','').replace(' ','')
                    works=0
            if works==1:
                print 'This path works. Adding it to the potential paths.'
                paths.append(i)
            i+=1
        # If no path works with the feature structure, go up a level
        # to try another
        if len(paths)==0:
            print 'There were no paths that work for this node ' + node.name + '. Backtracking now.'
            return None
        # Otherwise choose a random path until either it works or
        # there are no paths left to choose
        else:
            print 'There are potential paths to choose from for this node ' + node.name + '.'
            newFS = fs
            newSent = sent
            path=int(random.choice(paths))
            tried=[]
            while len(paths)>0:
                print 'Trying a path.'
                failed=0
                i=0
                while i<len(node.children[path]) and failed==0:
                    print 'Trying the child ' + node.children[path][i].name
                    if i > 0:
                        print 'The child ' + node.children[path][i].name + ' is not the first child, so the newFS should smartUnify with fs.'
                        if fs == FeatStruct():
                            print 'The fs was empty, so the newFS is simply the previous newFS:'
                            print 'previous newFS: ' + str(newFS).replace('\n','').replace(' ','') + ' unified with ' + 'fs: ' + str(fs).replace('\n','').replace(' ','') + ' = '
                            newFS = newFS.unify(fs)
                            print 'newFS: ' + str(newFS).replace('\n','').replace(' ','')
                        else:
                            print 'The fs was not empty, so the new FS is the previous newFS unified with the fs, smartUnified with the fs:'
                            print 'previous newFS: ' + str(newFS).replace('\n','').replace(' ','') + ' unified with ' + 'fs: ' + str(fs).replace('\n','').replace(' ','') + ' = '
                            print 'this: ' + str(newFS.unify(fs)).replace('\n','').replace(' ','') + ', which smart unified with fs: ' + str(fs).replace('\n','').replace(' ','') + ' = '
                            newFS = smartUnify(newFS.unify(fs),fs)
                            print 'newFS: ' + str(newFS).replace('\n','').replace(' ','')
                    toUnify = smartUnify2(newFS,node.childFeatures[path][i+1])
                    print 'Now the feature toUnify is the smartUnify2 of newFS: ' + str(newFS).replace('\n','').replace(' ','') + ' with the child feature: ' + str(node.childFeatures[path][i+1]).replace('\n','').replace(' ','') + ' which is '
                    print 'toUnify: ' + str(toUnify).replace('\n','').replace(' ','')
#                     toUnify = newFS.unify(node.childFeatures[path][i+1])
#                     print node.name
#                     print node.childFeatures[path]
#                     print newFS
#                     print node.childFeatures[path][i+1]
#                     print toUnify
                    # If the feature unification failed, this path
                    # fails
                    if toUnify == None:
                        print 'toUnify failed to be produced.'
                        failed=1
                    # Otherwise, send the unified feature structure
                    # down to the child node
                    else:
                        newFS = node.childFeatures[path][0].unify(toUnify)
                        print 'Now the newFS is the unity of the head feature: ' + str(node.childFeatures[path][0]).replace('\n','').replace(' ','') + ' with the feature toUnify: ' + str(toUnify).replace('\n','').replace(' ','') + ', which gives'
                        print 'newFS: ' + str(newFS).replace('\n','').replace(' ','')
#                         print node.name, str(node.childFeatures[path][0]).replace('\n','').replace(' ',''),'+', str(toUnify).replace('\n','').replace(' ',''),'=',str(newFS).replace('\n','').replace(' ','')
#                         print sent
                        print 'Now we will try to generate on the current child ' + node.children[path][i].name
                        fields = generateFB(newSent,node.children[path][i],newFS,maxDepth,currentDepth,node)
                        print 'We have returned to the node ' + node.name + '.'
#                         print fields
                        # If a sentence failed to be generated, this
                        # path fails
                        if fields == None or fields[0]==None:
                            print 'No fields were returned or no sentence was returned.'
                            failed=1
                        # If a feature structure failed to be returned
                        # this path fails and the feature structure is
                        # reset
                        elif fields[1]==None:
                            print 'No feature structure was returned. The newFS is now set back to the fs: ' + str(fs).replace('\n','').replace(' ','')
                            failed=1
                            newFS = fs
                        # Otherwise, the sentence and features are
                        # updated and the next item in the path is
                        # analyzed
                        else:
                            newSent = fields[0]
                            newFS = fields[1]
                            print 'The sentence ' + str(newSent).replace(' ','') + ' and feature set ' + str(newFS).replace('\n','').replace(' ','') + ' were returned. newFS is now set to this feature set.'
                            print 'Finished with this child ' + node.children[path][i].name
                        if newFS==None:
                            print 'The newFS is none. Reset the newFS to fs.'
                            failed=1
                            newFS=fs
                    i+=1
                # If the path failed, remove this path from the set
                # and choose another one. If all fail, go up a
                # level.
                if failed==1:
                    print 'This path failed. Adding it to the list of tried paths.'
                    tried.append(path)
                    paths.remove(path)
                    newSent = sent
                    if len(paths) > 0:
                        print 'There are paths left to try. Choosing a new path.'
                        path = random.choice(paths)
                # Otherwise, go up a level, updating the sentence and
                # feature set.
                else:
                    print 'This path worked for this node ' + node.name + '. Returning the sentence ' + str(newSent).replace(' ','') + ' and feature set ' + str(smartUnify(fs,newFS)).replace('\n','').replace(' ','')
                    return [newSent,smartUnify(fs,newFS)]
            print 'None of the paths worked for this node ' + node.name + '. Backtracking now.'
            return None
        
def generateNewFB(sent,node,fs):
    #If the node is a terminal, add it to the sentence
    if isinstance(node,Terminal):
        sent.append(node.name)
        print sent
        return (sent,True)
    #If not, do recursion
    else:
        #Add all possible paths to a list
        paths = []
        for i in range(len(node.children)):
            if node.childFeatures[i][0].unify(fs) != None:
                unifies = True
                j = 1
                while unifies and j < len(node.childFeatures[i]):
                    if node.childFeatures[i][0].unify(node.childFeatures[i][j]) == None:
                        unifies = False
                    j+=1
                if unifies:
                    paths.append(i)
        #If there are no possible paths, return false
        if len(paths) == 0:
            return (sent,False)
        #Otherwise, choose a random path until one works or all are exausted
        else:
            path = paths[random.randint(0,len(paths)-1)]
            while len(paths) > 0:
                newSent = sent
                i = 0
                works = True
                #For every child in the path, attempt to create more of the sentence
                while i < len(node.children[path]) and works:
                    fields = generateNewFB(newSent,node.children[path][i],node.childFeatures[path][i+1])
                    if fields[1]:
                        newSent = fields[0]
                    else:
                        works = False
                    i+=1
                if works:
                    return (newSent,True)
                else:
                    paths.remove(path)
                    if len(paths) == 0:
                        return (sent,False)
                    else:
                        path = paths[random.randint(0,len(paths)-1)]
                    
def generateSentence(nodes,maxDepth=3):
    '''Wrapper method for the generateFB method. Generate a sentence
    from the specified set of grammar nodes, returning only a list
    of sentence parts.
    
    Keyword arguments:
    nodes -- The set of nodes that represent the grammar.
    maxDepth -- The maximum depth with which to do recursion in the
                grammar (default is 3).
    '''
    
    sent = []
    for item in generateNewFB([],nodes[0],nodes[0].childFeatures[0][0])[0]:
        sent.append(item)
#     print sent
    return sent
#     for item in generateFB([],nodes[0],nodes[0].childFeatures[0][0],maxDepth)[0]:
#         sent.append(item[1:-1])
#     return sent
        
def smartUnify(*featstructs):
    '''Unifies two or more feature structures based on what they have
    in common. For example, [person=1,number=2] and [case=3,number=2]
    will return [number=2], not [person=1,number=2,case=3] as
    featStruct.unify() would do. Return None if unable to unify.
    
    Arguments:
    *featstructs -- Any number of feature structures to unify.
    '''
    
    # Create a list of lists of feature structures in each overall
    # structure. 
    lis = []
    for struct in featstructs:
        lis.append([])
        for item in struct:
            lis[len(lis)-1].append(item)
    # Create a set based on the first structure list, and then form
    # the intersection of the remaining lists, leaving only what is
    # left in common between all lists.
    s = set(lis[0])
    f = FeatStruct()
    for l in lis:
        s = s.intersection(l)
    # Unify the set together to form the resulting FeatStruct
    for struct in featstructs:
        for i in struct:
            if i in s:
                f = f.unify(FeatStruct('['+str(i)+'='+str(struct[i])+']'))
                if f == None:
                    return None
    return f

def smartUnify2(*featstructs):
    '''Unifies two or more feature structures based on what they have
    in common, and only that. For example, [person=1,number=2,case=4] and [case=3,number=2]
    will return [number=2], not None as
    featStruct.unify() would do. Return empty feature structure if unable to unify.
    
    Arguments:
    *featstructs -- Any number of feature structures to unify.
    '''
    
    # Create a list of lists of feature structures in each overall
    # structure. 
    lis = []
    for struct in featstructs:
        lis.append([])
        for item in struct:
            lis[len(lis)-1].append(item)
    # Create a set based on the first structure list, and then form
    # the intersection of the remaining lists, leaving only what is
    # left in common between all lists.
    s = set(lis[0])
    f = FeatStruct()
    for l in lis:
        s = s.intersection(l)
    # Unify the set together to form the resulting FeatStruct
    for struct in featstructs:
        for i in struct:
#             if i in s:
#                 f = f.unify(FeatStruct('['+str(i)+'='+str(struct[i])+']'))
#                 if f == None:
#                     return None
            if i in s and i not in f:
                f = f.unify(FeatStruct('['+str(i)+'='+str(struct[i])+']'))
            elif i in s and i in f and f[i] != struct[i]:
                del f[i]
    return f

def smartSubsumes(fs1,fs2):
    '''Return true if every item in the first structure is in the
    second, and false if not.
    
    Keyword Arguments:
    fs1 -- The 'child' feature structure, what is supposed to be
           contained in the second.
    fs2 -- The 'parent' feature structure, what is supposed to contain
           the first.
    '''
    l1 = []
    l2 = []
    for item in fs1:
        l1.append(item)
    for item in fs2:
        l2.append(item)
    if all(item in l2 for item in l1):
        return True
    else:
        return False

# for i in range(1,10):
#     print generateSentence(readCFG('Grammar.fcfg'))
# print generateSentence(readCFG('Grammar.fcfg'))

# allNodes = readCFG('Grammar.fcfg')
# printCFG(allNodes)
# for i in range(10):
# for j in range(1,20):
#     s = generateFB([],allNodes[0],allNodes[0].childFeatures[0][0],2)
#     m = ''
#     for i in s[0]:
#         m += i
#     print m
  
# fs1 = FeatStruct('[case=4,number=1]')

# print smartUnify2(FeatStruct('[case=2,gender=1,number=1]'),FeatStruct('[case=2,gender=2,number=1]'))
# fs2 = FeatStruct('[case=4,number=1,id=3]')
# smartUnify(fs1,fs2)
# print fs1.unify(fs2)