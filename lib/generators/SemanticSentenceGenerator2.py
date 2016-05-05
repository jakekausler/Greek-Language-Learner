'''
Created on Oct 11, 2014

@author: Jake
Adapted from Eli Benersky's blog on generating sentences from a CFG
http://eli.thegreenplace.net/2010/01/28/generating-random-sentences-from-a-context-free-grammar/
'''
# -*- coding: utf-8 -*-
from collections import defaultdict
import random, copy

class CFG:
    '''
    A CFG object that has the various productions recorded
    
    Attributes:
    prod -- Every production in the grammar, as a dictionary
            The form is prod[lhs] : (rhs),(rhs),(rhs),...
            The lhs (left hand side) is simply the name of the lhs node and the domain
            The rhs (right hand side) is a tuple of child names (allowing multiple lines)
    '''
    def __init__(self):
        # Default the productions to an empty default dictionary
        self.prod = defaultdict(list)
    
    def addProd(self,lhs,rhs,fs,head):
        '''
        Add a line to the grammar. rhs (right hand side) symbols are
        separated by a ', '
        For example:
            grammar.addProd('S','NP, VP')
            
        Keyword Arguments:
        lhs -- Left hand side of the production ('S')
        rhs -- Right hand side of the production ('NP, VP')
        fs -- Feature Structure of this production. None if there is
              not one
        head -- the head node of this production. Terminal nodes will
                not have one. This determines which path features need
                to be passed down.
        '''
        self.prod[lhs].append((rhs,fs,head))
    
    def constructGrammar(self,cfg='test'):
        f = open(cfg)
        lines = f.readlines()
        f.close()
        for line in lines:
            if not line.startswith('#') and len(line) > 1:
                l = line[:line.find(' -->')]
                lhs = (l[:l.find('[')],l[l.find('Domain=')+8:-2 if l.find(',') == -1 else l.find(',')-1])
                if l.find(',') != -1:
                    fs = self.makeFeatureStructure(l[l.find(',')+1:-1])
                else:
                    fs = None
                r = line[line.find('-->')+4:-1]
                rhs = []
                head = None
                i = 0
                for item in r.split(', '):
                    if item.find('-Head')!=-1:
                        head = i
                        item = item[:item.find('-Head')] + item[item.find('-Head')+5:]
                    if item.find('[') != -1:
                        rhs.append((item[:item.find('[')],item[item.find('Domain=')+8:-2 if item.find(',') == -1 else item.find(',')-1]))
                    else:
                        rhs.append((item,None))
                    i += 1
                self.addProd(lhs, tuple(rhs),fs,head)

    def makeFeatureStructure(self,fsString):
        '''
        Make a feature structure in the form
            {feat1:feat1Val,feat2:feat2Val,...}
        from a given string in the form:
            "Feat1='f1v',Feat2='f2v'..."
        '''
        fs = {}
        for i in fsString.split(','):
            fs[i[:i.find('=')]] = i[i.find('\'')+1:-1]
        return fs
    
    def genRandomSentence(self, symbol, domain=None):
        '''
        Generate a random sentence from the grammar, starting with the
        given start symbol.
        
        Keyword Arguments:
        
        symbol -- Start symbol for the sentence (or the node in
                  recursion)
        '''
        sentence = []
        
        # Select a domain if none is given
        if domain == None:
            domain = self.chooseRandomDomain(symbol)
        randProd = random.choice(self.prod[(symbol,domain)])
        
        for sym in randProd[0]:
            # for non-terminals, recurse
            if sym in self.prod:
                sentence += self.genRandomSentence(sym[0],sym[1])
            else:
                sentence.append(sym[0])
        return sentence
    
    def genRandomSentenceFS(self,symbol,domain=None,fs=None):
        '''
        Generate a random sentence from the grammar, starting with the
        given start symbol. A domain is optional, as a random domain
        will be chosen if none is supplied.
        
        Keyword Arguments:
        
        symbol -- Start symbol for the sentence (or the node in
                  recursion)
        domain -- The domain of the start symbol. If none is supplied,
                  a random one (possible for the symbol) will be
                  chosen.
        fs -- The feature structure needed to unify with the symbol.
              Should start as None. Only passes down if the child is
              the head child of the production.
        '''
        sentence = []
        
        # Select a domain if none is given
        if domain == None:
            domain = self.chooseRandomDomain(symbol)
            
        # Select a random production of the symbol which can unify with
        # the passed down feature structure. If none are found, fail
        prods = copy.copy(self.prod[(symbol,domain)])
        r = random.randint(0,len(prods)-1)
        randProd = prods[r]
        del prods[r]
        newfs = self.unify(fs,randProd[1])
        while newfs == None and randProd[1] != None and len(prods) > 0:
            r = random.randint(0,len(prods)-1)
            randProd = prods[r]
            del prods[r]
            newfs = self.unify(fs,randProd[1])
        if newfs == None and randProd[1] != None:
            return None
        
        # Recurse through the child symbols. If a failed route is found
        # fail out
        i = 0
        for sym in randProd[0]:
            # For non-terminals, recurse
            if sym in self.prod:
                topassfs = None
                if randProd[2] == i:
                    topassfs = newfs
                s = self.genRandomSentenceFS(sym[0], sym[1], topassfs)
                if s == None:
                    return None
                sentence += s[0]
                old = newfs
                newfs = self.unify(newfs,s[1])
                if old != None and newfs == None:
                    return None
            # Otherwise simply add the symbol to the sentence
            else:
                sentence.append(sym[0])
            i += 1
        return [sentence,newfs]
    
    def chooseRandomDomain(self,symbol):
        '''
        A helper method for generation. Chooses a random domain
        from the possible domains for a symbol.
        '''
        s = set()
        for i in self.prod:
            if i[0] == symbol and len(i) > 1:
                s.add(i[1])
        return random.choice(list(s))
    
    def unify(self,fs1,fs2):
        # Make an new fs that includes the features of both given
        newfs = {}
        if fs1 != None:
            for key in fs1:
                newfs[key] = fs1[key]
        if fs2 != None:
            for key in fs2:
                if key in newfs:
                    if newfs[key] != fs2[key]:
                        if newfs[key].find('?') != -1: # The first feature had one that needs filled in
                            newfs[key] = fs2[key]
                        elif fs2[key].find('?') != -1: # The second had one that needs filled in (so keep the first)
                            break
                        else: # The two were not equal. Fail
                            return None
                else:
                    newfs[key] = fs2[key]
        if len(newfs.keys()) == 0:
            return None
        else:
            return newfs
    
    def genRandomSentenceConvergent(self,symbol,cfactor=0.25,pcount=defaultdict(int),depth=30):
        '''
        Generate a random sentence from the grammar, starting at the
        given start symbol.
        Uses a convergent algorithm - productions that have already
        appeared in the derivation on each branch have a smaller
        chance to be selected.
        
        Keyword Arguments:
        
        symbol -- Start symbol for the sentence (or the node in
                  recursion)
        cfactor -- Controls how tight the convergence is.
                   0.0 < cfactor < 1.0
        pcount -- Internally used by recursive calls to pass on the
                  recursive calls to pass on the productions that have
                  been used in the branch.
        depth -- Maximum depth to recurse. If this dips below 0, fail.
        '''
        if depth > 0:
            sentence = []
            
            # The possible productions of this symbol are weighted by their
            # appearance in the branch that has led to this symbol in the
            # derivation
            weights = []
            for prod in self.prod[symbol]:
                if prod in pcount:
                    weights.append(cfactor ** (pcount[prod]))
                else:
                    weights.append(1.0)
                    
            randProd = self.prod[symbol][self.weightedChoice(weights)]
            
            # pcount is a single object (created in the first call to this
            # method) that is being passed around into recursive calls to
            # count how many times productions have been used.
            # Before recursive calls, the count is updated; after the
            # sentence for the this call is ready, it is rolled back to
            # avoid modifying the parent's pcount.
            pcount[randProd] += 1
            for sym in randProd:
                # for non-terminals, recurse
                if sym in self.prod:
                    s = self.genRandomSentenceConvergent(sym, cfactor=cfactor, pcount=pcount,depth=depth-1)
                    if s != None:
                        sentence += s
                    else:
                        return s
                else:
                    sentence.append(sym)
            
            # backtracking: clear the modification to pcount
            pcount[randProd] -= 1
            return sentence
        
    def genRandomSentenceConvergentFS(self,symbol,domain=None,fs=None,cfactor=0.25,pcount=defaultdict(int),depth=30):
        '''
        Generate a random sentence from the grammar, starting at the
        given start symbol and optional domain.
        Uses a convergent algorithm - productions that have already
        appeared in the derivation on each branch have a smaller
        chance to be selected.
        
        Keyword Arguments:
        
        symbol -- Start symbol for the sentence (or the node in
                  recursion)
        domain -- The domain of the start symbol. If none is supplied,
                  a random one (possible for the symbol) will be
                  chosen.
        fs -- The feature structure needed to unify with the symbol.
              Should start as None. Only passes down if the child is
              the head child of the production.
        cfactor -- Controls how tight the convergence is.
                   0.0 < cfactor < 1.0
        pcount -- Internally used by recursive calls to pass on the
                  recursive calls to pass on the productions that have
                  been used in the branch.
        depth -- Maximum depth to recurse. If this dips below 0, fail.
        '''
        if depth > 0:
            sentence = []
            
            # Select a domain if none is given
            if domain == None:
                domain = self.chooseRandomDomain(symbol)
                
#             # The possible productions of this symbol are weighted by their
#             # appearance in the branch that has led to this symbol in the
#             # derivation
#             weights = []
#             for prod in self.prod[symbol]:
#                 if prod in pcount:
#                     weights.append(cfactor ** (pcount[prod]))
#                 else:
#                     weights.append(1.0)
                    
            # Select a random production of the symbol which can unify with
            # the passed down feature structure. If none are found, fail
            prods = copy.copy(self.prod[(symbol,domain)])
            r = random.randint(0,len(prods)-1)
            randProd = prods[r]
            del prods[r]
            newfs = self.unify(fs,randProd[1])
            if depth > 99:
                print fs, randProd[1], len(prods), newfs, depth, newfs == None and randProd[1] != None and len(prods) > 0
            while newfs == None and randProd[1] != None and len(prods) > 0:
                if depth > 99:
                    print fs, randProd[1], depth
                r = random.randint(0,len(prods)-1)
                randProd = prods[r]
                del prods[r]
                newfs = self.unify(fs,randProd[1])
            if newfs == None and randProd[1] != None:
                return None

            # pcount is a single object (created in the first call to this
            # method) that is being passed around into recursive calls to
            # count how many times productions have been used.
            # Before recursive calls, the count is updated; after the
            # sentence for the this call is ready, it is rolled back to
            # avoid modifying the parent's pcount.
            pcount[randProd[0]] += 1
            print randProd[0]

            # Recurse through the child symbols. If a failed route is found
            # fail out
            i = 0
            for sym in randProd[0]:
                # For non-terminals, recurse
                if sym in self.prod:
                    topassfs = None
                    if randProd[2] == i:
                        topassfs = newfs
                    s = self.genRandomSentenceConvergentFS(sym[0], sym[1], topassfs, cfactor=cfactor, pcount=pcount,depth=depth-1)
                    if s == None:
                        return None
                    sentence += s[0]
                    old = newfs
                    newfs = self.unify(newfs,s[1])
                    if old != None and newfs == None:
                        return None
                # Otherwise simply add the symbol to the sentence
                else:
                    sentence.append(sym[0])
                i += 1
            return [sentence,newfs]
        
        
    def weightedChoice(self,weights):
        '''
        Helper method used in making a weighted path choice in the
        genRandomSentenceConvergence method.
        '''
        rnd = random.random()*sum(weights)
        for i,w in enumerate(weights):
            rnd -= w
            if rnd < 0:
                return i
    
    def toString(self):
        s = ''
        for key in self.prod:
            for p in self.prod[key]:
                s += key[0] + '[Domain=\'' + key[1] + '\']' + ' --> '
                for i in p:
                    if i[1] != None:
                        s += i[0] + '[Domain=\'' + i[1] + '\']' + ', '
                    else:
                        s += i[0] + ', '
                s = s[:-2] + '\n'
        return s

# grammar = CFG()
# grammar.constructGrammar('../Semantics/grammar.fcfg')
# for i in range(10):
# #     s = grammar.genRandomSentence('S')
# #     s = grammar.genRandomSentenceConvergent('S',cfactor=0.05,depth=20)
#     s = grammar.genRandomSentenceConvergentFS('S')
#     while s == None:
#         s = grammar.genRandomSentenceConvergentFS('S')
# #         s = grammar.genRandomSentenceConvergent('S',cfactor=0.05,depth=20)
#     print s[0]
# f = open('test2','w')
# f.write(grammar.toString())
# f.close()