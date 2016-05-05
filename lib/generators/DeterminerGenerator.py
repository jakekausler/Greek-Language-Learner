# -*- coding: utf-8 -*-
'''
Created on Jun 6, 2014

@author: Jake

Generate determiner forms based on an word.
'''

def generateDeterminerForms(word):
    '''Generate and return the forms of a determiner. A value of 0 in
    any position means the word cannot be found in that form. The
    forms are returned in the form of:
        [mns, mgs, mds, mcs, mvs,
         mnp, mgp, mdp, mcp,
         fns, fgs, fds, fcs, fvs,
         fnp, fgp, fdp, fcp,
         nns, ngs, nds, ncs, nvs,
         nnp, ngp, ndp, ncp]
    
    Keyword arguments:
    word -- Nominative masculine singular of the form to generate.
    '''
    if word=='ὁ':
        return ['ὁ',
                'τοῦ',
                'τῷ',
                'τόν',
                'ὁ',
                'οἱ',
                'τῶν',
                'τοῖς',
                'τούς',
                'ἡ',
                'τῆς',
                'τῇ',
                'τήν',
                'ἡ',
                'αἱ',
                'τῶν',
                'ταῖς',
                'τάς',
                'τό',
                'τοῦ',
                'τῷ',
                'τό',
                'τό',
                'τά',
                'τῶν',
                'τοῖς',
                'τά']
    elif word=='ὅς':
        return ['ὅς',
                'οὗ',
                'ᾧ',
                'ὃν',
                'ὅς',
                'οἳ',
                'ὧν',
                'οἷς',
                'οὓς',
                'ἥ',
                'ἧ',
                'ᾑ',
                'ἥν',
                'ἥ',
                'αἳ',
                'ὧν',
                'αἷς',
                'ἃς',
                'ὅ',
                'οὗ',
                'ᾧ',
                'ὅ',
                'ὅ',
                'ἃ',
                'ὧν',
                'οἷς',
                'ἃ']
    return 0