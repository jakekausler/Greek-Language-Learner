# -*- coding: utf-8 -*-
'''
Created on Apr 28, 2014

@author: Jake
Generate verb forms based on morphological features, a morphological
code, and the root.
'''
import sys

def formTense(verb,form,tense):
    '''Generates the forms of an verb based on a certain
    morphological code, as well as the mood, voice, and tense. A value
    of 0 in any position means the word cannot be found in that form.
    The forms are returned as:
        Indicative, subjunctive, and optative:
            [1s,2s,3s,
             1p,2p,3p]
        Imperative:
            [2s,3s,
             2p,3p]
        Infinitive:
            Just the form itself
        Participle:
            [mns, mgs, mds, mcs, mvs,
             mnp, mgp, mdp, mcp,
             fns, fgs, fds, fcs, fvs,
             fnp, fgp, fdp, fcp,
             nns, ngs, nds, ncs, nvs,
             nnp, ngp, ndp, ncp]
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    tense -- The mood,tense, and voice of the verb. The first letter
             is the mood (one of i=indicative, s=subjunctive,
             o=optative, m=imperative, n=infinitive, or
             p=participle). The second letter is the tense (one of
             p=present, m=imperfect, f=future, f1=first future,
             f2=second future, a1=first aorist, a2=second aorist,
             e=perfect, e1=first perfect, e2=second perfect, or
             l=pluperfect). The third letter is the voice (one of
             a=active, m=middle, or p=passive).
    '''
    #Match Tenses
    styles = {'ipa':ipa,
                'ipm':ipm,
                'ipp':ipp,
                'ima':ima,
                'imm':imm,
                'imp':imp,
                'ifa':ifa,
                'ifm':ifm,
                'if1p':if1p,
                'if2p':if2p,
                'ia1a':ia1a,
                'ia1m':ia1m,
                'ia1p':ia1p,
                'ia2a':ia2a,
                'ia2m':ia2m,
                'ia2p':ia2p,
                'ie1a':ie1a,
                'ie2a':ie2a,
                'iem':iem,
                'iep':iep,
                'ila':ila,
                'ilm':ilm,
                'ilp':ilp,
                'spa':spa,
                'spm':spm,
                'spp':spp,
                'sa1a':sa1a,
                'sa1m':sa1m,
                'sa1p':sa1p,
                'sa2a':sa2a,
                'sa2m':sa2m,
                'sa2p':sa2p,
                'sea':sea,
                'sem':sem,
                'sep':sep,
                'opa':opa,
                'opm':opm,
                'oa1a':oa1a,
                'oa1m':oa1m,
                'oa1p':oa1p,
                'oa2a':oa2a,
                'oa2m':oa2m,
                'oa2p':oa2p,
                'mpa':mpa,
                'mpm':mpm,
                'mpp':mpp,
                'ma1a':ma1a,
                'ma1m':ma1m,
                'ma1p':ma1p,
                'ma2a':ma2a,
                'ma2m':ma2m,
                'ma2p':ma2p,
                'mea':mea,
                'mem':mem,
                'mep':mep,
                'npa':npa,
                'npm':npm,
                'npp':npp,
                'nfa':nfa,
                'nfm':nfm,
                'na1a':na1a,
                'na1m':na1m,
                'na1p':na1p,
                'na2a':na2a,
                'na2m':na2m,
                'na2p':na2p,
                'nea':nea,
                'nem':nem,
                'nep':nep,
                'ppa':ppa,
                'ppm':ppm,
                'ppp':ppp,
                'pfa':pfa,
                'pfm':pfm,
                'pfp':pfp,
                'pa1a':pa1a,
                'pa1m':pa1m,
                'pa1p':pa1p,
                'pa2a':pa2a,
                'pa2m':pa2m,
                'pa2p':pa2p,
                'pea':pea,
                'pem':pem,
                'pep':pep}
    return styles[tense](verb,form)

def getPrincipleParts(verb,form):
    '''Return the principle parts of the verb as a list in the form:
        [1-Present/Imperfect,2-Future Active/Middle,
         3-Aorist Active/Middle,4-Perfect/Pluperfect/Future Perfect Active,
         5-Perfect/Pluperfect/Future Perfect Middle,
         6-Aorist/Future Passive
    
    Keyword arguments:
    verb -- The present indicative, first person singular form of the
            verb
    form -- The morphological code of the verb, drawn from Mounce's
            "Morphology of Biblical Greek". Used to ensure the correct
            verb principle parts are chosen.
    '''
    f = open('verbprincipleparts')
    lines = f.readlines()
    for line in lines:
        if line.startswith(verb):
            if line.endswith(form+'\n'):
                l = line.split(',')[:-1]
                return l
            elif line.endswith(form):
                l = line.split(',')[:-1]
                return l
    return ['-','-','-','-','-','-']
            
def ipa(verb,form):
    '''Form the Present Active Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if verb == 'εἰμί':
            return ['εἰμί',
                    'εἶ',
                    'ἐστίν',
                    'ἐσμέν',
                    'ἐστέ',
                    'εἰσίν']
        elif verb == 'ἀφίημι':
            return ['ἀφίημι',
                    'ἀφιεῖς',
                    'ἀφίησιν',
                    'ἀφίομεν',
                    'ἀφίετε',
                    'ἀφίουσιν']
        if not parts[0].endswith('μι'):
            if parts[0][:-4].startswith('α') or verb[:-4].startswith('ά') or verb[:-4].startswith('ὰ'):
                return [parts[0][:-4]+'ῶ',
                 parts[0][:-4]+'ᾷς',
                 parts[0][:-4]+'ᾷ',
                 parts[0][:-4]+'ῶμεν',
                 parts[0][:-4]+'ᾶτε',
                 parts[0][:-4]+'ῶσι']
            elif parts[0][:-4].startswith('ε') or parts[0][:-4].startswith('ὲ') or parts[0][:-4].startswith('έ'):
                return [parts[0][:-4]+'ῶ',
                 parts[0][:-4]+'εῖς',
                 parts[0][:-4]+'εῖ',
                 parts[0][:-4]+'οῦμεν',
                 parts[0][:-4]+'εῖτε',
                 parts[0][:-4]+'οῦσι']
            elif parts[0][:-4].startswith('ο') or parts[0][:-4].startswith('ό') or parts[0][:-4].startswith('ὸ'):
                return [parts[0][:-4]+'ῶ',
                 parts[0][:-4]+'οῖς',
                 parts[0][:-4]+'οῖ',
                 parts[0][:-4]+'οῦμεν',
                 parts[0][:-4]+'οῦτε',
                 parts[0][:-4]+'οῦσι']
            else:
                return [parts[0],
                 parts[0][:-2]+'εις',
                 parts[0][:-2]+'ει',
                 parts[0][:-2]+'ομεν',
                 parts[0][:-2]+'ετε',
                 parts[0][:-2]+'ουσιν']
        else:
            if parts[0][:-8].startswith('θη') or parts[0][:-8].startswith('θὴ') or parts[0][:-8].startswith('θή'):
                return [parts[0],
                 parts[0][:-4]+'ς',
                 parts[0][:-4]+'σιν',
                 parts[0][:-6]+'εμεν',
                 parts[0][:-6]+'ετε',
                 parts[0][:-6]+'εῖσιν']
            elif parts[0][:-6].startswith('η') or parts[0][:-6].startswith('ὴ') or parts[0][:-6].startswith('ή'):
                return [parts[0],
                 parts[0][:-4]+'ς',
                 parts[0][:-4]+'σιν',
                 parts[0][:-6]+'αμεν',
                 parts[0][:-6]+'ατε',
                 parts[0][:-6]+'ᾶσιν']
            elif parts[0][:-6].startswith('ω') or parts[0][:-6].startswith('ὼ') or parts[0][:-6].startswith('ώ'):
                return [parts[0],
                 parts[0][:-4]+'ς',
                 parts[0][:-4]+'σιν',
                 parts[0][:-6]+'ομεν',
                 parts[0][:-6]+'οτε',
                 parts[0][:-6]+'οῦσιν']
            else:
                return [parts[0],
                 parts[0][:-4]+'ς',
                 parts[0][:-4]+'σιν',
                 parts[0][:-6]+'υμεν',
                 parts[0][:-6]+'υτε',
                 parts[0][:-6]+'υασιν']
    else:
        return 0

def ipm(verb,form):
    '''Form the Present Middle Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if verb == 'ἀφίημι':
            return ['ἀφίεμαι',
                    'ἀφίεσαι',
                    'ἀφίεται',
                    'ἀφιέμεθα',
                    'ἀφίεσθε',
                    'ἀφίενται']
        if not parts[0].endswith('μι'):
            if parts[0][:-4].startswith('α') or parts[0][:-4].startswith('ά') or parts[0][:-4].startswith('ὰ'):
                return [parts[0][:-4]+'ῶμαι',
                 parts[0][:-4]+'ᾷ',
                 parts[0][:-4]+'ᾶται',
                 parts[0][:-4]+'ωμεθα',
                 parts[0][:-4]+'ᾶσθα',
                 parts[0][:-4]+'ῶνται']
            elif parts[0][:-4].startswith('ε') or parts[0][:-4].startswith('ὲ') or parts[0][:-4].startswith('έ'):
                return [parts[0][:-4]+'οῦμαι',
                 parts[0][:-4]+'ῇ',
                 parts[0][:-4]+'εῖται',
                 parts[0][:-4]+'ουμεθα',
                 parts[0][:-4]+'εῖσθε',
                 parts[0][:-4]+'οῦνται']
            elif parts[0][:-4].startswith('ο') or parts[0][:-4].startswith('ό') or parts[0][:-4].startswith('ὸ'):
                return [parts[0][:-4]+'οῦμαι',
                 parts[0][:-4]+'οῖ',
                 parts[0][:-4]+'οῦται',
                 parts[0][:-4]+'ουμεθα',
                 parts[0][:-4]+'οῦσθα',
                 parts[0][:-4]+'οῦνται']
            else:
                return [parts[0][:-2]+'ομαι',
                 parts[0][:-2]+'ῃ',
                 parts[0][:-2]+'εται',
                 parts[0][:-2]+'ομεθα',
                 parts[0][:-2]+'εσθα',
                 parts[0][:-2]+'ονται']
        else:
            if parts[0][:-8].startswith('θη') or parts[0][:-8].startswith('θὴ') or parts[0][:-8].startswith('θή'):
                return [parts[0][:-6]+'εμαι',
                 parts[0][:-6]+'εσαι',
                 parts[0][:-6]+'εται',
                 parts[0][:-6]+'εμεθα',
                 parts[0][:-6]+'εσθα',
                 parts[0][:-6]+'ενται']
            elif parts[0][:-6].startswith('η') or parts[0][:-6].startswith('ὴ') or parts[0][:-6].startswith('ή'):
                return [parts[0][:-6]+'αμαι',
                 parts[0][:-6]+'ασαι',
                 parts[0][:-6]+'αται',
                 parts[0][:-6]+'αμεθα',
                 parts[0][:-6]+'ασθα',
                 parts[0][:-6]+'ανται']
            elif parts[0][:-6].startswith('ω') or parts[0][:-6].startswith('ὼ') or parts[0][:-6].startswith('ώ'):
                return [parts[0][:-6]+'ομαι',
                 parts[0][:-6]+'οσαι',
                 parts[0][:-6]+'οται',
                 parts[0][:-6]+'ομεθα',
                 parts[0][:-6]+'οσθα',
                 parts[0][:-6]+'ονται']
            else:
                return [parts[0][:-4]+'μαι',
                 parts[0][:-4]+'σαι',
                 parts[0][:-4]+'ται',
                 parts[0][:-4]+'μεθα',
                 parts[0][:-4]+'σθα',
                 parts[0][:-4]+'νται']
    else:
        return 0

def ipp(verb,form):
    '''Form the Present Passive Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return ipm(verb,form)

def ima(verb,form):
    '''Form the Imperfect Active Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if verb == 'εἰμί':
            return ['ἤμην',
                    'ἦς',
                    'ἦν',
                    'ἦμεν',
                    'ἦτε',
                    'ἦσαν']
        if not parts[0][:-4].startswith('μι'):
            if parts[0][:-4].startswith('α') or parts[0][:-4].startswith('ά') or parts[0][:-4].startswith('ὰ'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[1][:-2]+'ν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ας',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'α',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ῶμεν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ᾶτε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'ν']
            elif parts[0][:-4].startswith('ε') or parts[0][:-4].startswith('ὲ') or parts[0][:-4].startswith('έ'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ουν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'εις',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ει',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'οῦμεν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'εῖτε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ουν']
            elif parts[0][:-4].startswith('ο') or parts[0][:-4].startswith('ό') or parts[0][:-4].startswith('ὸ'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ουν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ους',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ου',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'οῦμεν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'οῦτε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ουν']
            else:
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'ον',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'ες',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'εν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'ομεν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'ετε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'ον']
        else:
            if parts[0][:-8].startswith('θη') or parts[0][:-8].startswith('θὴ') or parts[0][:-8].startswith('θή'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'εις',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ει',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'εμεν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ετε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'εσαν']
            elif parts[0][:-6].startswith('η') or parts[0][:-6].startswith('ὴ') or parts[0][:-6].startswith('ή'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ς',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4],
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'αμεν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ατε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ασαν']
            elif parts[0][:-6].startswith('ω') or parts[0][:-6].startswith('ὼ') or parts[0][:-6].startswith('ώ'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ουν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ους',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ου',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ομεν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'οτε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'οσαν']
            else:
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ς',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4],
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'μεν',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'τε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'σαν']
    else:
        return 0
    
def imm(verb,form):
    '''Form the Imperfect Middle Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if not parts[0][:-4].startswith('μι'):
            if parts[0][:-4].startswith('α') or parts[0][:-4].startswith('ά') or parts[0][:-4].startswith('ὰ'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[1][:-2]+'μην',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ῶ',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ᾶτο',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'μεθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ᾶσθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ῶντο']
            elif parts[0][:-4].startswith('ε') or parts[0][:-4].startswith('ὲ') or parts[0][:-4].startswith('έ'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ουμην',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'οῦ',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'εῖτο',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ουμεθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'εῖσθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'οῦντο']
            elif parts[0][:-4].startswith('ο') or parts[0][:-4].startswith('ό') or parts[0][:-4].startswith('ὸ'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ουμην',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'οῦ',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'οῦτο',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ουμεθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'οῦσθε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'οῦντο']
            else:
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'ομην',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'ου',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'ετο',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'ομεθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'εσθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-2]+'οντο']
        else:
            if parts[0][:-8].startswith('θη') or parts[0][:-8].startswith('θὴ') or parts[0][:-8].startswith('θή'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'εμην',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'εσο',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ετο',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'εμεθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'εσθε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'εντο']
            elif parts[0][:-6].startswith('η') or parts[0][:-6].startswith('ὴ') or parts[0][:-6].startswith('ή'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'αμην',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ασο',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ατο',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'αμεθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ασθε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'αντο']
            elif parts[0][:-6].startswith('ω') or parts[0][:-6].startswith('ὼ') or parts[0][:-6].startswith('ώ'):
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ομην',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'οσο',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'οτο',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'ομεθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'οσθε',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-6]+'οντο']
            else:
                return [(parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'μην',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'σο',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'το',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'μεθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'σθα',
                 (parts[2][:3] if parts[2]!='-' else 'ε')+parts[0][:-4]+'ντο']
    else:
        return 0

def imp(verb,form):
    '''Form the Imperfect Passive Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return imm(verb,form)

def ifa(verb,form):
    '''Form the Future Active Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[1] != '-':
        if verb == 'εἰμί':
            return ['ἔσομαι',
                    'ἔσῃ',
                    'ἔσται',
                    'ἐσόμεθα',
                    'ἔσεσθε',
                    'ἔσονται']
        elif verb == 'ἀφίημι':
            return ['ἀφιήσω',
                    'ἀφήσεις',
                    'ἀφήσει',
                    'ἀφήσομεν',
                    'ἀφήσετε',
                    'ἀφήσουσιν']
        if parts[1].endswith('ῶ'):
            return [parts[1],
             parts[1][:-3]+'εῖς',
             parts[1][:-3]+'εῖ',
             parts[1][:-3]+'οῦμεν',
             parts[1][:-3]+'εῖτε',
             parts[1][:-3]+'οῦσιν']
        else:
            return [parts[1],
             parts[1][:-2]+'εις',
             parts[1][:-2]+'ει',
             parts[1][:-2]+'ουμεν',
             parts[1][:-2]+'ετε',
             parts[1][:-2]+'ουσιν']
    else:
        return 0

def ifm(verb,form):
    '''Form the Future Middle Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[1] != '-':
        if parts[1].endswith('ῶ'):
            return [parts[1][:-3]+'οῦμαι',
             parts[1][:-3]+'ῇ',
             parts[1][:-3]+'εῖται',
             parts[1][:-3]+'ουμεθα',
             parts[1][:-3]+'εῖσθα',
             parts[1][:-3]+'οῦνται']
        else:
            return [parts[1][:-2]+'ομαι',
             parts[1][:-2]+'ῃ',
             parts[1][:-2]+'εται',
             parts[1][:-2]+'ομεθα',
             parts[1][:-2]+'εσθα',
             parts[1][:-2]+'ονται']
    else:
        return 0

def if1p(verb,form):
    '''Form the First Future Passive Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[5] != '-':
        return [parts[5][:-2]+'σομαι',
         parts[5][:-2]+'σῃ',
         parts[5][:-2]+'σεται',
         parts[5][:-2]+'σομεθα',
         parts[5][:-2]+'σεσθα',
         parts[5][:-2]+'σονται']
    else:
        return 0

def if2p(verb,form):
    '''Form the Second Future Passive Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[5] != '-':
        return [parts[5][:-2]+'ησομαι',
         parts[5][:-2]+'ησῃ',
         parts[5][:-2]+'ησεται',
         parts[5][:-2]+'ησομεθα',
         parts[5][:-2]+'ησεσθα',
         parts[5][:-2]+'ησονται']
    else:
        return 0

def ia1a(verb,form):
    '''Form the First Aorist Active Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) == 0:
            if verb == 'ἀφίημι':
                return ['ἀφῆκα',
                        'ἀφῆκας',
                        'ἀφῆκεν',
                        'ἀφήκαμεν',
                        'ἀφήκατε',
                        'ἀφῆκαν']
            else:
                return [parts[2],
                 parts[2]+'ς',
                 parts[2][:-2]+'εν',
                 parts[2]+'μεν',
                 parts[2]+'τε',
                 parts[2]+'ν']
        else:
            return 0
    else:
        return 0

def ia1m(verb,form):
    '''Form the First Aorist Middle Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) == 0:
            return [parts[2]+'μην',
             parts[2][:-2]+'ω',
             parts[2]+'το',
             parts[2]+'μεθα',
             parts[2]+'σθα',
             parts[2]+'ντο']
        else:
            return 0
    else:
        return 0

def ia1p(verb,form):
    '''Form the First Aorist Passive Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[5] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) == 0:
            return [parts[5]+'',
             parts[5][:-2]+'ς',
             parts[5][:-2]+'',
             parts[5][:-2]+'μην',
             parts[5][:-2]+'τε',
             parts[5][:-2]+'σαν']
        else:
            return 0
    else:
        return 0

def ia2a(verb,form):
    '''Form the Second Aorist Active Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) == 0:
            if verb == 'ἀφίημι':
                return ['ἀφῆκα',
                        'ἀφῆκας',
                        'ἀφῆκεν',
                        'ἀφήκαμεν',
                        'ἀφήκατε',
                        'ἀφῆκαν']
            elif verb == 'γινώσκω':
                return ['ἔγνων',
                        'ἔγνως',
                        'ἔγνω',
                        'ἔγνωμεν',
                        'ἔγνωτε',
                        'ἔγνωσαν']
            if parts[2].endswith('ον'):
                return [parts[2],
                 parts[2][:-4]+'ες',
                 parts[2][:-4]+'εν',
                 parts[2][:-2]+'μεν',
                 parts[2][:-4]+'ετε',
                 parts[2]]
            else:
                return [parts[2],
                 parts[2][:-2]+'ς',
                 parts[2][:-2],
                 parts[2][:-2]+'μεν',
                 parts[2][:-2]+'τε',
                 parts[2][:-2]+'σαν']
        else:
            return 0
    else:
        return 0

def ia2m(verb,form):
    '''Form the Second Aorist Middle Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) == 0:
            if parts[2].endswith('ον'):
                return [parts[2][:-2]+'μην',
                 parts[2][:-2]+'υ',
                 parts[2][:-4]+'ετο',
                 parts[2][:-2]+'μεθα',
                 parts[2][:-4]+'εσθε',
                 parts[2]+'το']
            else:
                if parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('α') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                    return [parts[2][:-4]+'αμην',
                     parts[2][:-4]+'ω',
                     parts[2][:-4]+'ατο',
                     parts[2][:-4]+'αμεθα',
                     parts[2][:-4]+'ασθε',
                     parts[2][:-4]+'αντο']
                elif parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ') or parts[0][:-4].endswith('ε'):
                    return [parts[2][:-4]+'εμην',
                     parts[2][:-4]+'ου',
                     parts[2][:-4]+'ετο',
                     parts[2][:-4]+'εμεθα',
                     parts[2][:-4]+'εσθε',
                     parts[2][:-4]+'εντο']
                else:
                    return [parts[2][:-4]+'ομην',
                     parts[2][:-4]+'ου',
                     parts[2][:-4]+'οτο',
                     parts[2][:-4]+'ομεθα',
                     parts[2][:-4]+'οσθε',
                     parts[2][:-4]+'οντο']
        else:
            return 0
    else:
        return 0

def ia2p(verb,form):
    '''Form the Second Aorist Passive Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[5] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) == 0:
            return [parts[5],
             parts[5][:-2]+'ς',
             parts[5][:-2],
             parts[5][:-2]+'μεν',
             parts[5][:-2]+'τε',
             parts[5][:-2]+'σαν']
        else:
            return 0
    else:
        return 0

def ie1a(verb,form):
    '''Form the First Perfect Active Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    if whichPerfect(verb) == 1:
        parts = getPrincipleParts(verb,form)
        if parts[3] != '-':
            if verb == 'οἶδα':
                return ['οἶδα',
                 'οἶδας',
                 'οἶδεν',
                 'οἴδαμεν',
                 'οἴδατε',
                 'οἴδασιν']
            else:
                return [parts[3],
                 parts[3]+'ς',
                 parts[3][:-2]+'εν',
                 parts[3]+'μεν',
                 parts[3]+'τε',
                 parts[3]+'σιν']
        else:
            return 0
    else:
        return 0

def ie2a(verb,form):
    '''Form the Second Perfect Active Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    if whichPerfect(verb) == 2:
        parts = getPrincipleParts(verb,form)
        if parts[3] != '-':
            return [parts[3],
             parts[3]+'ς',
             parts[3][:-2]+'εν',
             parts[3]+'μεν',
             parts[3]+'τε',
             parts[3]+'σιν']
        else:
            return 0
    else:
        return 0

def iem(verb,form):
    '''Form the Perfect Middle Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[4] != '-':
        if verb == 'ἀφίημι':
            return ['',
                    '',
                    '',
                    '',
                    '',
                    'ἀφέωνται']
        else:
            return [parts[4],
             parts[4][:-6]+'σαι',
             parts[4][:-6]+'ται',
             parts[4][:-6]+'μεθα',
             parts[4][:-6]+'σθε',
             parts[4][:-6]+'νται']
    else:
        return 0

def iep(verb,form):
    '''Form the Perfect Passive Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return iem(verb,form)

def ila(verb,form):
    '''Form the Pluperfect Active Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[3] != '-':
        if verb == 'οἶδα':
                return ['ᾔδειν',
                 'ᾔδεις',
                 'ᾔδει',
                 'ᾔδειμεν',
                 'ᾔδειτε',
                 'ᾔδεισαν']
        else:
            return [parts[3],
             parts[3][:-2]+'ς',
             parts[3][:-2]+'',
             parts[3][:-2]+'μεν',
             parts[3][:-2]+'τε',
             parts[3][:-2]+'σαν']
    else:
        return 0

def ilm(verb,form):
    '''Form the Pluperfect Middle Indicative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[4] != '-':
        if parts[4][:-6].endswith('μ'):
            return [parts[4],
             parts[4][:-8]+'ψο',
             parts[4][:-8]+'πτο',
             parts[4][:-8]+'μμεθα',
             parts[4][:-8]+'φθε',
             parts[4][:-8]+'μμενοι'] 
        elif parts[4][:-6].endswith('γ'):
            return [parts[4],
             parts[4][:-8]+'ξο',
             parts[4][:-8]+'κτο',
             parts[4][:-8]+'γμεθα',
             parts[4][:-8]+'χθε',
             parts[4][:-8]+'γμενοι']
        elif parts[4][:-6].endswith('σ'):
            return [parts[4],
             parts[4][:-6]+'ο',
             parts[4][:-6]+'το',
             parts[4][:-6]+'θα',
             parts[4][:-6]+'σθε',
             parts[4][:-6]+'μενοι']
        else:
            return [parts[4],
             parts[4][:-6]+'σο',
             parts[4][:-6]+'το',
             parts[4][:-6]+'μεθα',
             parts[4][:-6]+'σθε',
             parts[4][:-6]+'ντο']
    else:
        return 0

def ilp(verb,form):
    '''Form the Pluperfect Passive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return ilm(verb,form)

def spa(verb,form):
    '''Form the Present Active Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if verb == 'εἰμί':
            return ['ὦ',
                    'ᾖς',
                    'ᾖ',
                    'ὦμεν',
                    'ἦτε',
                    'ὦσιν']
        elif verb == 'ἀφίημι':
            return ['ἀφιῶ',
                    'ἀφιῇς',
                    'ἀφιῇ',
                    'ἀφιῶμεν',
                    'ἀφιῆτε',
                    'ἀφιῶσιν']
        if parts[0].endswith('μι'):
            if parts[0][:-2].endswith('ο') or parts[0][:-2].endswith('ὸ') or parts[0][:-2].endswith('ό') or parts[0][:-2].endswith('ω') or parts[0][:-2].endswith('ώ') or parts[0][:-2].endswith('ὼ'):
                return [parts[0][:-2]+'ῶ',
                 parts[0][:-2]+'ῷς',
                 parts[0][:-2]+'ῷ',
                 parts[0][:-2]+'ῶμεν',
                 parts[0][:-2]+'ῶτε',
                 parts[0][:-2]+'ῶσιν']
            else:
                return [parts[0][:-2]+'ῶ',
                 parts[0][:-2]+'ῇς',
                 parts[0][:-2]+'ῇ',
                 parts[0][:-2]+'ῶμεν',
                 parts[0][:-2]+'ῇτε',
                 parts[0][:-2]+'ῶσιν']
        else:
            if parts[0][:-2].endswith('α') or parts[0][:-2].endswith('ὰ') or parts[0][:-2].endswith('ά'):
                return [parts[0][:-2]+'ῶ',
                 parts[0][:-2]+'ᾷς',
                 parts[0][:-2]+'ᾷ',
                 parts[0][:-2]+'ῶμεν',
                 parts[0][:-2]+'ᾶτε',
                 parts[0][:-2]+'ῶσιν']
            elif parts[0][:-2].endswith('ε') or parts[0][:-2].endswith('έ') or parts[0][:-2].endswith('ὲ'):
                return [parts[0][:-2]+'ῶ',
                 parts[0][:-2]+'ῇς',
                 parts[0][:-2]+'ῇ',
                 parts[0][:-2]+'ῶμεν',
                 parts[0][:-2]+'ῆτε',
                 parts[0][:-2]+'ῶσιν']
            elif parts[0][:-2].endswith('ο') or parts[0][:-2].endswith('ὸ') or parts[0][:-2].endswith('ό'):
                return [parts[0][:-2]+'ῶ',
                 parts[0][:-2]+'οῖς',
                 parts[0][:-2]+'οῖ',
                 parts[0][:-2]+'ῶμεν',
                 parts[0][:-2]+'ῶτε',
                 parts[0][:-2]+'ῶσιν']
            else: 
                return [parts[0],
                 parts[0][:-2]+'ῃς',
                 parts[0][:-2]+'ῃ',
                 parts[0][:-2]+'ωμεν',
                 parts[0][:-2]+'ητε',
                 parts[0][:-2]+'ωσιν']
    else:
        return 0

def spm(verb,form):
    '''Form the Present Middle Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if parts[0].endswith('μι'):
            if parts[0][:-2].endswith('ο') or parts[0][:-2].endswith('ὸ') or parts[0][:-2].endswith('ό') or parts[0][:-2].endswith('ω') or parts[0][:-2].endswith('ώ') or parts[0][:-2].endswith('ὼ'):
                return [parts[0][:-2]+'ῶμαι',
                 parts[0][:-2]+'ῷ',
                 parts[0][:-2]+'ῶται',
                 parts[0][:-2]+'ωμεua',
                 parts[0][:-2]+'ῶσθε',
                 parts[0][:-2]+'ῶνται']
            else:
                return [parts[0][:-2]+'ῶμαι',
                 parts[0][:-2]+'ῇ',
                 parts[0][:-2]+'ῆται',
                 parts[0][:-2]+'ωμεua',
                 parts[0][:-2]+'ῆσθε',
                 parts[0][:-2]+'ῶνται']
        else:
            if parts[0][:-2].endswith('α') or parts[0][:-2].endswith('ὰ') or parts[0][:-2].endswith('ά'):
                return [parts[0][:-2]+'ῶμαι',
                 parts[0][:-2]+'ᾷ',
                 parts[0][:-2]+'ᾶται',
                 parts[0][:-2]+'ωμεθα',
                 parts[0][:-2]+'ᾶσθε',
                 parts[0][:-2]+'ῶνται']
            elif parts[0][:-2].endswith('ε') or parts[0][:-2].endswith('έ') or parts[0][:-2].endswith('ὲ'):
                return [parts[0][:-2]+'ῶ',
                 parts[0][:-2]+'ῇ',
                 parts[0][:-2]+'ῆται',
                 parts[0][:-2]+'ωμεθα',
                 parts[0][:-2]+'ῆσθε',
                 parts[0][:-2]+'ῶνται']
            elif parts[0][:-2].endswith('ο') or parts[0][:-2].endswith('ὸ') or parts[0][:-2].endswith('ό'):
                return [parts[0][:-2]+'ῶ',
                 parts[0][:-2]+'οῖ',
                 parts[0][:-2]+'ῶται',
                 parts[0][:-2]+'ωμεθα',
                 parts[0][:-2]+'ῶσθε',
                 parts[0][:-2]+'ῶνται']
            else: 
                return [parts[0][:-2]+'ωμαι',
                 parts[0][:-2]+'ῃ',
                 parts[0][:-2]+'ηται',
                 parts[0][:-2]+'ωμεθα',
                 parts[0][:-2]+'ησθε',
                 parts[0][:-2]+'ωνται']
    else:
        return 0

def spp(verb,form):
    '''Form the Present Passive Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return spm(verb,form)

def sa1a(verb,form):
    '''Form the First Aorist Active Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) == 0:
            if verb == 'ἀφίημι':
                return ['ἀφῶ',
                        'ἀφῇς',
                        'ἀφῇ',
                        'ἀφῶμεν',
                        'ἀφῆτε',
                        'ἀφῶσιν']
            elif verb == 'γινώσκω':
                return ['γνῶ',
                        'γνῷς',
                        'γνῷ',
                        'γνῶμεν',
                        'γνῶτε',
                        'γνῶσιν']
            else:
                front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
                return [parts[2][front:-2]+'ω',
                 parts[2][front:-2]+'ῃς',
                 parts[2][front:-2]+'ῃ',
                 parts[2][front:-2]+'ωμεν',
                 parts[2][front:-2]+'ητε',
                 parts[2][front:-2]+'ωσιν']
        else:
            return 0
    else:
        return 0

def sa1m(verb,form):
    '''Form the First Aorist Middle Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) == 0:
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            return [parts[2][front:-2]+'ωμαι',
             parts[2][front:-2]+'ῃ',
             parts[2][front:-2]+'ηται',
             parts[2][front:-2]+'ωμεθα',
             parts[2][front:-2]+'ησθα',
             parts[2][front:-2]+'ωνται']
        else:
            return 0
    else:
        return 0

def sa1p(verb,form):
    '''Form the First Aorist Passive Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) == 0:
            if verb == 'ἀφίημι':
                return ['ἀφεθῶ',
                        'ἀφεθῇς',
                        'ἀφεθῇ',
                        'ἀφεθῶμεν',
                        'ἀφεθῆτε',
                        'ἀφεθῶσιν']
            else:
                front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
                return [parts[2][front:-4]+'ῶ',
                 parts[2][front:-4]+'ῇς',
                 parts[2][front:-4]+'ῇ',
                 parts[2][front:-4]+'ῶμεν',
                 parts[2][front:-4]+'ῆτε',
                 parts[2][front:-4]+'ῶσιν']
        else:
            return 0
    else:
        return 0

def sa2a(verb,form):
    '''Form the Second Aorist Active Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) == 0:
            if verb == 'ἀφίημι':
                return ['ἀφῶ',
                        'ἀφῇς',
                        'ἀφῇ',
                        'ἀφῶμεν',
                        'ἀφῆτε',
                        'ἀφῶσιν']
            elif verb == 'γινώσκω':
                return ['γνῶ',
                        'γνῷς',
                        'γνῷ',
                        'γνῶμεν',
                        'γνῶτε',
                        'γνῶσιν']
            else:
                front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
                return [parts[2][front:-2]+'ω',
                 parts[2][front:-2]+'ῃς',
                 parts[2][front:-2]+'ῃ',
                 parts[2][front:-2]+'ωμεν',
                 parts[2][front:-2]+'ητε',
                 parts[2][front:-2]+'ωσιν']
        else:
            return 0
    else:
        return 0

def sa2m(verb,form):
    '''Form the Second Aorist Middle Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) == 0:
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            return [parts[2][front:-2]+'ωμαι',
             parts[2][front:-2]+'ῃ',
             parts[2][front:-2]+'ηται',
             parts[2][front:-2]+'ωμεθα',
             parts[2][front:-2]+'ησθα',
             parts[2][front:-2]+'ωνται']
        else:
            return 0
    else:
        return 0

def sa2p(verb,form):
    '''Form the Second Aorist Passive Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) == 0:
            if verb == 'ἀφίημι':
                return ['ἀφεθῶ',
                        'ἀφεθῇς',
                        'ἀφεθῇ',
                        'ἀφεθῶμεν',
                        'ἀφεθῆτε',
                        'ἀφεθῶσιν']
            else:
                front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
                return [parts[2][front:-4]+'ῶ',
                 parts[2][front:-4]+'ῇς',
                 parts[2][front:-4]+'ῇ',
                 parts[2][front:-4]+'ῶμεν',
                 parts[2][front:-4]+'ῆτε',
                 parts[2][front:-4]+'ῶσιν']
        else:
            return 0
    else:
        return 0

def sea(verb,form):
    '''Form the Perfect Active Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[3] != '-':
        if verb == 'οἶδα':
            return ['εἰδῶ',
             'εἰδῇς',
             'εἰδῇ',
             'εἰδῶμεν',
             'εἰδῆτε',
             'εἰδῶσιν']
        else:
            return 0
    else:
        return 0

def sem(verb,form):
    '''Form the Perfect Middle Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return 0

def sep(verb,form):
    '''Form the Perfect Passive Subjunctive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return 0

def opa(verb,form):
    '''Form the Present Active Optative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if verb == 'εἰμί':
            return ['εἴην',
             'εἴης',
             'εἴη',
             'εἶμεν',
             'εἶτε',
             'εἶεν']
        elif verb[:-4].endswith('a') or verb[:-4].endswith('ὰ') or verb[:-4].endswith('ά'):
            return [parts[0][:-4]+'ιην',
             parts[0][:-4]+'ιης',
             parts[0][:-4]+'ιη',
             parts[0][:-4]+'ῖμεν',
             parts[0][:-4]+'ῖτε',
             parts[0][:-4]+'ῖεν']
        elif verb[:-4].endswith('ε') or verb[:-4].endswith('έ') or verb[:-4].endswith('ὲ'):
            return [parts[0][:-4]+'ιην',
             parts[0][:-4]+'ιης',
             parts[0][:-4]+'ιη',
             parts[0][:-4]+'ῖμεν',
             parts[0][:-4]+'ῖτε',
             parts[0][:-4]+'ῖεν']
        elif verb[:-4].endswith('ο') or verb[:-4].endswith('ό') or verb[:-4].endswith('ὸ') or verb[:-4].endswith('ω') or verb[:-4].endswith('ὼ') or verb[:-4].endswith('ώ'):
            return [parts[0][:-6]+'οιην',
             parts[0][:-6]+'οιης',
             parts[0][:-6]+'οιη',
             parts[0][:-6]+'οῖμεν',
             parts[0][:-6]+'οῖτε',
             parts[0][:-6]+'οῖεν']
        else:
            return [parts[0][:-2]+'οιμι',
             parts[0][:-2]+'οις',
             parts[0][:-2]+'οι',
             parts[0][:-2]+'οιμεν',
             parts[0][:-2]+'οιτε',
             parts[0][:-2]+'οιεν']
    else:
        return 0

def opm(verb,form):
    '''Form the Present Middle Optative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if verb[:-4].endswith('a') or verb[:-4].endswith('ὰ') or verb[:-4].endswith('ά'):
            return [parts[0][:-4]+'ιμην',
             parts[0][:-4]+'ῖο',
             parts[0][:-4]+'ῖτο',
             parts[0][:-4]+'ιμεθα',
             parts[0][:-4]+'ῖσθε',
             parts[0][:-4]+'ῖντο']
        elif verb[:-4].endswith('ε') or verb[:-4].endswith('έ') or verb[:-4].endswith('ὲ'):
            return [parts[0][:-4]+'ιμην',
             parts[0][:-4]+'ῖο',
             parts[0][:-4]+'ῖτο',
             parts[0][:-4]+'ιμεθα',
             parts[0][:-4]+'ῖσθε',
             parts[0][:-4]+'ῖντο']
        elif verb[:-4].endswith('ο') or verb[:-4].endswith('ό') or verb[:-4].endswith('ὸ') or verb[:-4].endswith('ω') or verb[:-4].endswith('ὼ') or verb[:-4].endswith('ώ'):
            return [parts[0][:-6]+'οιμην',
             parts[0][:-6]+'οῖο',
             parts[0][:-6]+'οῖτο',
             parts[0][:-6]+'οιμεθα',
             parts[0][:-6]+'οῖσθε',
             parts[0][:-6]+'οῖντο']
        else:
            return [parts[0][:-2]+'οιμην',
             parts[0][:-2]+'οιο',
             parts[0][:-2]+'οιτο',
             parts[0][:-2]+'οιμεθα',
             parts[0][:-2]+'οισθα',
             parts[0][:-2]+'οιντο']
    else:
        return 0

def oa1a(verb,form):
    '''Form the First Aorist Active Optative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) == 0:
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            return [parts[2][front:]+'ιμι',
             parts[2][front:]+'ις',
             parts[2][front:]+'ι',
             parts[2][front:]+'ιμεν',
             parts[2][front:]+'ιτε',
             parts[2][front:]+'ιεν']
        else:
            return 0
    else:
        return 0

def oa1m(verb,form):
    '''Form the First Aorist Middle Optative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) == 0:
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            return [parts[2][front:]+'ιμην',
             parts[2][front:]+'ιο',
             parts[2][front:]+'ιτο',
             parts[2][front:]+'ιμεθα',
             parts[2][front:]+'ισθε',
             parts[2][front:]+'ιντο']
        else:
            return 0
    else:
        return 0

def oa1p(verb,form):
    '''Form the First Aorist Passive Optative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
        return [parts[2][front:-4]+'ειην',
         parts[2][front:-4]+'ειης',
         parts[2][front:-4]+'ειη',
         parts[2][front:-4]+'εῖμεν',
         parts[2][front:-4]+'εῖτε',
         parts[2][front:-4]+'εῖεν']
    else:
        return 0

def oa2a(verb,form):
    '''Form the Second Aorist Active Optative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) == 0:
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            if verb[:-4].endswith('a') or verb[:-4].endswith('ὰ') or verb[:-4].endswith('ά'):
                return [parts[2][front:-4]+'ιμν',
                 parts[2][front:-4]+'ιης',
                 parts[2][front:-4]+'ιη',
                 parts[2][front:-4]+'ῖμεν',
                 parts[2][front:-4]+'ῖτε',
                 parts[2][front:-4]+'ῖεν']
            elif verb[:-4].endswith('ε') or verb[:-4].endswith('έ') or verb[:-4].endswith('ὲ'):
                return [parts[2][front:-4]+'ιμν',
                 parts[2][front:-4]+'ιης',
                 parts[2][front:-4]+'ιη',
                 parts[2][front:-4]+'ῖμεν',
                 parts[2][front:-4]+'ῖτε',
                 parts[2][front:-4]+'ῖεν']
            elif verb[:-4].endswith('ο') or verb[:-4].endswith('ό') or verb[:-4].endswith('ὸ') or verb[:-4].endswith('ω') or verb[:-4].endswith('ὼ') or verb[:-4].endswith('ώ'):
                return [parts[2][front:-4]+'οιμν',
                 parts[2][front:-6]+'οιης',
                 parts[2][front:-6]+'οιη',
                 parts[2][front:-6]+'οῖμεν',
                 parts[2][front:-6]+'οῖτε',
                 parts[2][front:-6]+'οῖεν']
            else:
                return [parts[2][front:]+'ιμι',
                 parts[2][front:]+'ις',
                 parts[2][front:]+'ι',
                 parts[2][front:]+'ιμεν',
                 parts[2][front:]+'ιτε',
                 parts[2][front:]+'ιεν']
        else:
            return 0
    else:
        return 0

def oa2m(verb,form):
    '''Form the Second Aorist Middle Optative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) == 0:
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            if verb[:-4].endswith('a') or verb[:-4].endswith('ὰ') or verb[:-4].endswith('ά'):
                return [parts[2][front:-4]+'ιμην',
                 parts[2][front:-4]+'ιο',
                 parts[2][front:-4]+'ιτο',
                 parts[2][front:-4]+'ιμεθα',
                 parts[2][front:-4]+'ισθε',
                 parts[2][front:-4]+'ιντο']
            elif verb[:-4].endswith('ε') or verb[:-4].endswith('έ') or verb[:-4].endswith('ὲ'):
                return [parts[2][front:-4]+'ιμην',
                 parts[2][front:-4]+'ῖο',
                 parts[2][front:-4]+'ῖτο',
                 parts[2][front:-4]+'ιμεθα',
                 parts[2][front:-4]+'ῖσθε',
                 parts[2][front:-4]+'ῖντο']
            elif verb[:-4].endswith('ο') or verb[:-4].endswith('ό') or verb[:-4].endswith('ὸ') or verb[:-4].endswith('ω') or verb[:-4].endswith('ὼ') or verb[:-4].endswith('ώ'):
                return [parts[2][front:-4]+'οιμην',
                 parts[2][front:-4]+'οῖο',
                 parts[2][front:-4]+'οῖτο',
                 parts[2][front:-4]+'οιμεθα',
                 parts[2][front:-4]+'οῖσθε',
                 parts[2][front:-4]+'οῖντο']
            else:
                return [parts[2][front:]+'ιμην',
                 parts[2][front:]+'ιο',
                 parts[2][front:]+'ιτο',
                 parts[2][front:]+'ιμεθα',
                 parts[2][front:]+'ισθε',
                 parts[2][front:]+'ιντο']
        else:
            return 0
    else:
        return 0

def oa2p(verb,form):
    '''Form the Second Aorist Passive Optative of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[5] != '-':
        front = 3 if not any(parts[5].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
        return [parts[5][front:-4]+'ειην',
         parts[5][front:-4]+'ειης',
         parts[5][front:-4]+'ειη',
         parts[5][front:-4]+'εῖμεν',
         parts[5][front:-4]+'εῖτε',
         parts[5][front:-4]+'εῖεν']
    else:
        return 0

def mpa(verb,form):
    '''Form the Present Active Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if verb == 'εἰμί':
            return ['ἴσθι',
             'ἔστω',
             'ἔστε',
             'ἔστωσαν']
        elif verb == 'ἀφίημι':
            return ['ἀφίει',
             'ἀφιέτω',
             'ἀφίετε',
             'ἀφιέντων']
        if verb.endswith('μι'):
            if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return [parts[0][:-6]+'η',
                 parts[0][:-6]+'aτω',
                 parts[0][:-6]+'ατε',
                 parts[0][:-6]+'aτωσαν']
            elif parts[0][:-6].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return [parts[0][:-6]+'ει',
                 parts[0][:-6]+'ετω',
                 parts[0][:-6]+'ετε',
                 parts[0][:-6]+'ετωσαν']
            elif parts[0][:-2][:-4].endswith('ο') or parts[0][:-4].endswith('ὸ') or parts[0][:-4].endswith('ό') or parts[0][:-4].endswith('ω') or parts[0][:-4].endswith('ὼ') or parts[0][:-4].endswith('ώ'):
                return [parts[0][:-6]+'ου',
                 parts[0][:-6]+'οτω',
                 parts[0][:-6]+'οτε',
                 parts[0][:-6]+'οτωσαν']
            else:
                return [parts[0][:-4]+'υ',
                 parts[0][:-4]+'υτω',
                 parts[0][:-4]+'υτε',
                 parts[0][:-4]+'υτωσαν'] 
        else:
            if parts[0].endswith('α') or parts[0].endswith('ὰ') or parts[0].endswith('ά'):
                return [parts[0][:-4]+'α',
                 parts[0][:-4]+'aτω',
                 parts[0][:-4]+'ᾶτε',
                 parts[0][:-4]+'aτωσαν']
            elif parts[0].endswith('ε') or parts[0].endswith('έ') or parts[0].endswith('ὲ'):
                return [parts[0][:-4]+'ει',
                 parts[0][:-4]+'ειτω',
                 parts[0][:-4]+'εῖτε',
                 parts[0][:-4]+'ειτωσαν']
            elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return [parts[0][:-4]+'ου',
                 parts[0][:-4]+'ουτω',
                 parts[0][:-4]+'οῦτε',
                 parts[0][:-4]+'ουτωσαν']
            else:
                return [parts[0][:-2]+'ε',
                 parts[0][:-2]+'ετω',
                 parts[0][:-2]+'ετε',
                 parts[0][:-2]+'ετωσαν']
    else:
        return 0

def mpm(verb,form):
    '''Form the Present Middle Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if verb.endswith('μι'):
            if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return [parts[0][:-6]+'ασο',
                 parts[0][:-6]+'aσθω',
                 parts[0][:-6]+'ασθε',
                 parts[0][:-6]+'aσθωσαν']
            elif parts[0][:-6].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return [parts[0][:-6]+'εσο',
                 parts[0][:-6]+'εσθω',
                 parts[0][:-6]+'εσθε',
                 parts[0][:-6]+'εσθωσαν']
            elif parts[0][:-2][:-4].endswith('ο') or parts[0][:-4].endswith('ὸ') or parts[0][:-4].endswith('ό') or parts[0][:-4].endswith('ω') or parts[0][:-4].endswith('ὼ') or parts[0][:-4].endswith('ώ'):
                return [parts[0][:-6]+'οσο',
                 parts[0][:-6]+'οσθω',
                 parts[0][:-6]+'οσθε',
                 parts[0][:-6]+'οσθωσαν']
            else:
                return [parts[0][:-6]+'υσο',
                 parts[0][:-6]+'υσθω',
                 parts[0][:-6]+'υσθε',
                 parts[0][:-6]+'υσθωσαν']
        else:
            if parts[0].endswith('α') or parts[0].endswith('ὰ') or parts[0].endswith('ά'):
                return [parts[0][:-2]+'ῶ',
                 parts[0][:-2]+'ασθω',
                 parts[0][:-2]+'ασθε',
                 parts[0][:-2]+'ασθωσαν']
            elif parts[0].endswith('ε') or parts[0].endswith('έ') or parts[0].endswith('ὲ'):
                return [parts[0][:-2]+'οῦ',
                 parts[0][:-2]+'εισθω',
                 parts[0][:-2]+'εῖσθε',
                 parts[0][:-2]+'εισθωσαν']
            elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return [parts[0][:-2]+'οῦ',
                 parts[0][:-2]+'ουσθω',
                 parts[0][:-2]+'οῦσθε',
                 parts[0][:-2]+'ουσθωσαν']
            else:
                return [parts[0][:-2]+'ου',
                 parts[0][:-2]+'εσθω',
                 parts[0][:-2]+'εσθε',
                 parts[0][:-2]+'εσθωσαν']
    else:
        return 0

def mpp(verb,form):
    '''Form the Present Passive Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return mpm(verb,form)

def ma1a(verb,form):
    '''Form the First Aorist Active Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if whichAorist(verb) == 1 or whichAorist(verb) == 0:
        if parts[2] != '-':
            if verb == 'ἀφίημι':
                return ['ἀφές',
                 'ἀφέτω',
                 'ἄφετε',
                 'ἀφέτωσαν']
            elif verb == 'γινώσκω':
                return ['γνῶθι',
                 'γνώτω',
                 'γνῶτε',
                 'γνόντων']
            else:
                front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
                return [parts[2][front:-4]+'ον',
                 parts[2][front:-4]+'ατω',
                 parts[2][front:-4]+'ατε',
                 parts[2][front:-4]+'ατωσαν']
        else:
            return 0
    else:
        return 0

def ma1m(verb,form):
    '''Form the First Aorist Middle Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if whichAorist(verb) == 1 or whichAorist(verb) == 0:
        if parts[2] != '-':
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            return [parts[2][front:-2]+'ι',
             parts[2][front:-2]+'σθω',
             parts[2][front:-2]+'σθε',
             parts[2][front:-2]+'σθων']
        else:
            return 0
    else:
        return 0

def ma1p(verb,form):
    '''Form the First Aorist Passive Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if whichAorist(verb) == 1 or whichAorist(verb) == 0:
        if parts[2] != '-':
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            if parts[0].endswith('μι'):
                if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                    return [parts[2][front:-4]+'ητι',
                     parts[2][front:-4]+'ητω',
                     parts[2][front:-4]+'ῆτε',
                     parts[2][front:-4]+'ητωσαν']
                elif parts[0][:-6].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                    return [parts[2][front:-4]+'ητι',
                     parts[2][front:-4]+'ητω',
                     parts[2][front:-4]+'ητε',
                     parts[2][front:-4]+'ητωσαν']
                elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                    return [parts[2][front:-4]+'ητι',
                     parts[2][front:-4]+'ητω',
                     parts[2][front:-4]+'ητε',
                     parts[2][front:-4]+'ητωσαν']
            else:
                return [parts[2][front:-4]+'ητι',
                 parts[2][front:-4]+'ητω',
                 parts[2][front:-4]+'ητε',
                 parts[2][front:-4]+'ητωσαν']
        else:
            return 0
    else:
        return 0

def ma2a(verb,form):
    '''Form the Second Aorist Active Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if whichAorist(verb) == 2 or whichAorist(verb) == 0:
        if parts[2] != '-':
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            if parts[0].endswith('μι'):
                if verb == 'ἀφίημι':
                    return ['ἀφές',
                     'ἀφέτω',
                     'ἄφετε',
                     'ἀφέτωσαν']
                elif verb == 'γινώσκω':
                    return ['γνῶθι',
                     'γνώτω',
                     'γνῶτε',
                     'γνόντων']
                if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                    return [parts[2][front:-6]+'ε',
                     parts[2][front:-6]+'ητω',
                     parts[2][front:-6]+'ῆτε',
                     parts[2][front:-6]+'ητωσαν']
                elif parts[0][:-6].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                    return [parts[2][front:-6]+'ες',
                     parts[2][front:-6]+'ετω',
                     parts[2][front:-6]+'ετε',
                     parts[2][front:-6]+'ετωσαν']
                elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                    return [parts[2][front:-6]+'ος',
                     parts[2][front:-6]+'οτω',
                     parts[2][front:-6]+'οτε',
                     parts[2][front:-6]+'οτωσαν']
            else:
                return [parts[2][front:-2]+'ε',
                 parts[2][front:-2]+'ετω',
                 parts[2][front:-2]+'ετε',
                 parts[2][front:-2]+'ετωσαν']
        else:
            return 0
    else:
        return 0

def ma2m(verb,form):
    '''Form the Second Aorist Middle Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if whichAorist(verb) == 2 or whichAorist(verb) == 0:
        if parts[2] != '-':
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            if parts[0].endswith('μι'):
                if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                    return [parts[2][front:-2]+'ῶ',
                     parts[2][front:-2]+'ασθω',
                     parts[2][front:-2]+'ασθε',
                     parts[2][front:-2]+'ασθωσαν']
                elif parts[0][:-6].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                    return [parts[2][front:-2]+'οῦ',
                     parts[2][front:-2]+'εσθω',
                     parts[2][front:-2]+'εσθε',
                     parts[2][front:-2]+'εσθωσαν']
                elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                    return [parts[2][front:-2]+'οῦ',
                     parts[2][front:-2]+'οσθω',
                     parts[2][front:-2]+'οσθε',
                     parts[2][front:-2]+'οσθωσαν']
            else:
                return [parts[2][front:-2]+'οῦ',
                 parts[2][front:-2]+'εσθω',
                 parts[2][front:-2]+'εσθε',
                 parts[2][front:-2]+'εσθωσαν']
        else:
            return 0
    else:
        return 0

def ma2p(verb,form):
    '''Form the Second Aorist Passive Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if whichAorist(verb) == 1 or whichAorist(verb) == 0:
        front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
        if parts[2] != '-':
            return [parts[2][front:-4]+'ηθι',
             parts[2][front:-4]+'ητω',
             parts[2][front:-4]+'ητε',
             parts[2][front:-4]+'ητωσαν']
        else:
            return 0
    else:
        return 0

def mea(verb,form):
    '''Form the Perfect Active Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[3] != '-':
        if verb == 'οἶδα':
            return ['ἴσθι',
                    'ἴστω',
                    'ἴστε',
                    'ἴστωσαν']
        else:
            return [parts[3][:-2]+'ε',
             parts[3][:-2]+'ετω',
             parts[3][:-2]+'ετε',
             parts[3][:-2]+'ετωσαν']
    else:
        return 0

def mem(verb,form):
    '''Form the Perfect Middle Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[4] != '-':
        return [parts[4][:-2]+'ο',
         parts[4][:-2]+'θω',
         parts[4][:-2]+'θε',
         parts[4][:-2]+'θωσαν']
    else:
        return 0

def mep(verb,form):
    '''Form the Perfect Passive Imperfect of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return mem(verb,form)

def npa(verb,form):
    '''Form the Present Active Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if verb == 'εἰμί':
            return 'εἶναι'
        elif verb == 'ἀφίημι':
            return 'ἀφιέναι'
        if parts[0].endswith('μι'):
            if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[0][:-6]+'αναι'
            elif parts[0][:-4].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[0][:-6]+'εναι'
            elif parts[0][:-4].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return parts[0][:-6]+'οναι'
            else:
                return parts[0][:-6]+'υναι'
        else:
            if parts[0][:-2].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[0][:-4]+'ᾶν'
            elif parts[0][:-2].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[0][:-4]+'εῖν'
            elif parts[0][:-2].endswith('ο') or parts[0][:-2].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return parts[0][:-4]+'οῦν'
            else:
                return parts[0][:-2]+'ειν'
    else:
        return 0;

def npm(verb,form):
    '''Form the Present Middle Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if parts[0].endswith('μι'):
            if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[0][:-6]+'ασθαι'
            elif parts[0][:-4].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[0][:-6]+'εσθαι'
            elif parts[0][:-4].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return parts[0][:-6]+'οσθαι'
            else:
                return parts[0][:-6]+'υσθαι'
        else:
            if parts[0][:-2].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[0][:-4]+'ᾶσθαι'
            elif parts[0][:-2].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[0][:-4]+'εῖσθαι'
            elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return parts[0][:-4]+'οῦσθαι'
            else:
                return parts[0][:-2]+'εσθαι'
    else:
        return 0;

def npp(verb,form):
    '''Form the Present Passive Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return npm(verb,form)

def nfa(verb,form):
    '''Form the Future Active Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[1] != '-':
        if parts[0].endswith('μι'):
            if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[0][:-6]+'ησειν'
            elif parts[0][:-4].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[0][:-6]+'ησειν'
            else:
                return parts[0][:-6]+'ωσειν'
        else:
            if parts[0][:-2].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[0][:-4]+'ησειν'
            elif parts[0][:-2].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[0][:-4]+'ησειν'
            elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return parts[0][:-4]+'ωσειν'
            else:
                return parts[0][:-2]+'σειν'
    else:
        return 0;

def nfm(verb,form):
    '''Form the Future Middle Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[1] != '-':
        if verb == 'εἰμί':
            return 'ἔσεσθαι'
        if parts[0].endswith('μι'):
            if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[0][:-6]+'ησεσθαι'
            elif parts[0][:-4].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[0][:-6]+'ησεσθαι'
            else:
                return parts[0][:-6]+'ωσεσθαι'
        else:
            if parts[0][:-2].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[0][:-4]+'ησεσθαι'
            elif parts[0][:-2].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[0][:-4]+'ησεσθαι'
            elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return parts[0][:-4]+'ωσεσθαι'
            else:
                return parts[0][:-2]+'σεσθαι'
    else:
        return 0;

def na1a(verb,form):
    '''Form the First Aorist Active Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) == 0:
            if verb == 'ἀφίημι':
                return 'ἀφεῖναι'
            elif verb == 'γινώσκω':
                return 'γνῶναι'
            if parts[0].endswith('μι'):
                return parts[0][:-6]+'ησαι'
            else:
                if parts[0][:-2].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                    return parts[0][:-4]+'ησαι'
                elif parts[0][:-2].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                    return parts[0][:-4]+'ησαι'
                elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                    return parts[0][:-4]+'ωσαι'
                else:
                    return parts[0][:-2]+'σαι'
        else:
            return 0
    else:
        return 0;

def na1m(verb,form):
    '''Form the First Aorist Middle Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) == 0:
            if parts[0].endswith('μι'):
                return parts[0][:-6]+'ησασθαι'
            else:
                if parts[0][:-2].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                    return parts[0][:-4]+'ησασθαι'
                elif parts[0][:-2].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                    return parts[0][:-4]+'ησασθαι'
                elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                    return parts[0][:-4]+'ωσασθαι'
                else:
                    return parts[0][:-2]+'σασθαι'
        else:
            return 0
    else:
        return 0;

def na1p(verb,form):
    '''Form the First Aorist Passive Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) == 0:
            if parts[0].endswith('μι'):
                if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                    return parts[0][:-6]+'αθῆναι'
                elif parts[0][:-4].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                    return parts[0][:-6]+'εθῆναι'
                else:
                    return parts[0][:-6]+'οθῆναι'
            else:
                if parts[0][:-2].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                    return parts[0][:-4]+'ηθῆναι'
                elif parts[0][:-2].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                    return parts[0][:-4]+'ηθῆναι'
                elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                    return parts[0][:-4]+'ωθῆναι'
                else:
                    return parts[0][:-2]+'θῆναι'
        else:
            return 0
    else:
        return 0;

def na2a(verb,form):
    '''Form the Second Aorist Active Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) == 0:
            if verb == 'ἀφίημι':
                return 'ἀφεῖναι'
            elif verb == 'γινώσκω':
                return 'γνῶναι'
            if parts[0].endswith('μι'):
                if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                    return parts[0][:-6]+'ῆναι'
                elif parts[0][:-4].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                    return parts[0][:-6]+'ῖναι'
                else:
                    return parts[0][:-6]+'οῦναι'
            else:
                front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
                return parts[2][front:-4]+'εῖν'
        else:
            return 0
    else:
        return 0;

def na2m(verb,form):
    '''Form the Second Aorist Middle Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) == 0:
            if parts[0].endswith('μι'):
                if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                    return parts[0][:-6]+'ασθαι'
                elif parts[0][:-4].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                    return parts[0][:-6]+'εσθαι'
                else:
                    return parts[0][:-6]+'οσθαι'
            else:
                front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
                return parts[2][front:-4]+'εσθαι'
        else:
            return 0
    else:
        return 0;

def na2p(verb,form):
    '''Form the Second Aorist Passive Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) == 0:
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            return parts[2][front:-4]+'ῆναι'
        else:
            return 0
    else:
        return 0

def nea(verb,form):
    '''Form the Perfect Active Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[3] != '-':
        if verb == 'οἶδα':
            return 'εἰδέναι'
        if parts[0].endswith('μι'):
            if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[3][:-2]+'εναι'
            elif parts[0][:-4].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[3][:-2]+'εναι'
            else:
                return parts[3][:-2]+'εναι'
        else:
            if parts[0][:-2].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[3][:-2]+'εναι'
            elif parts[0][:-2].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[3][:-2]+'εναι'
            elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return parts[3][:-2]+'εναι'
            else:
                return parts[3][:-2]+'εναι'
    else:
        return 0;

def nem(verb,form):
    '''Form the Perfect Middle Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[3] != '-':
        if parts[0].endswith('μι'):
            if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[4][:-8]+'ασθαι'
            elif parts[0][:-4].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[4][:-8]+'εῖσθαι'
            else:
                return parts[4][:-8]+'οσθαι'
        else:
            if parts[0][:-2].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return parts[4][:-8]+'ῆσθαι'
            elif parts[0][:-2].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return parts[4][:-8]+'ῆσθαι'
            elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return parts[4][:-8]+'ῶσθαι'
            else:
                return parts[3][:-6]+'σθαι'
    else:
        return 0;

def nep(verb,form):
    '''Form the Perfect Passive Infinitive of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return nem(verb,form)

def ppa(verb,form):
    '''Form the Present Active Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if parts[0].endswith('μι'):
            if verb == 'εἰμί':
                return ['ὤν',
                        'ὄντος',
                        'ὄντι',
                        'ὄντα',
                        'ὤν',
                        'ὄντες',
                        'ὄντων',
                        'οὖσιν',
                        'ὄντας',
                        'οὖσα',
                        'οὔσης',
                        'οὔσῃ',
                        'οὖσαν',
                        'οὖσα',
                        'οὖσαι',
                        'οὐσῶν',
                        'οὔσαις',
                        'οὔσας',
                        'ὄν',
                        'ὄντος',
                        'ὄντι',
                        'ὄν',
                        'ὄν',
                        'ὄντα',
                        'ὄντων',
                        'οὖσιν',
                        'ὄντα']
            if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return [parts[0][:-6]+'ας',
                 parts[0][:-6]+'αντος',
                 parts[0][:-6]+'αντι',
                 parts[0][:-6]+'αντα',
                 parts[0][:-6]+'ας',
                 parts[0][:-6]+'αντες',
                 parts[0][:-6]+'αντων',
                 parts[0][:-6]+'ᾶσιν',
                 parts[0][:-6]+'αντας',
                 parts[0][:-6]+'ᾶσα',
                 parts[0][:-6]+'ασης',
                 parts[0][:-6]+'ασῃ',
                 parts[0][:-6]+'ᾶσαν',
                 parts[0][:-6]+'ᾶσα',
                 parts[0][:-6]+'ᾶσαι',
                 parts[0][:-6]+'ασῶν',
                 parts[0][:-6]+'ασαις',
                 parts[0][:-6]+'ασας',
                 parts[0][:-6]+'αν',
                 parts[0][:-6]+'αντος',
                 parts[0][:-6]+'αντι',
                 parts[0][:-6]+'αν',
                 parts[0][:-6]+'αν',
                 parts[0][:-6]+'αντα',
                 parts[0][:-6]+'αντων',
                 parts[0][:-6]+'ᾶσιν',
                 parts[0][:-6]+'ᾶντα']
            elif parts[0][:-4].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return [parts[0][:-6]+'εις',
                 parts[0][:-6]+'εντος',
                 parts[0][:-6]+'εντι',
                 parts[0][:-6]+'εντα',
                 parts[0][:-6]+'εις',
                 parts[0][:-6]+'εντες',
                 parts[0][:-6]+'εντων',
                 parts[0][:-6]+'εῖσιν',
                 parts[0][:-6]+'εντας',
                 parts[0][:-6]+'εῖσα',
                 parts[0][:-6]+'εισης',
                 parts[0][:-6]+'εισῃ',
                 parts[0][:-6]+'εῖσαν',
                 parts[0][:-6]+'εῖσα',
                 parts[0][:-6]+'εῖσαι',
                 parts[0][:-6]+'εισῶν',
                 parts[0][:-6]+'εισαις',
                 parts[0][:-6]+'εισας',
                 parts[0][:-6]+'εν',
                 parts[0][:-6]+'εντος',
                 parts[0][:-6]+'εντι',
                 parts[0][:-6]+'εν',
                 parts[0][:-6]+'εν',
                 parts[0][:-6]+'εντα',
                 parts[0][:-6]+'εισων',
                 parts[0][:-6]+'εῖσιν',
                 parts[0][:-6]+'εντα']
            elif parts[0][:-4].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return [parts[0][:-6]+'ους',
                 parts[0][:-6]+'οντος',
                 parts[0][:-6]+'οντι',
                 parts[0][:-6]+'οντα',
                 parts[0][:-6]+'ους',
                 parts[0][:-6]+'οντες',
                 parts[0][:-6]+'οντων',
                 parts[0][:-6]+'οῦσιν',
                 parts[0][:-6]+'οντας',
                 parts[0][:-6]+'οῦσα',
                 parts[0][:-6]+'ουσης',
                 parts[0][:-6]+'ουσῃ',
                 parts[0][:-6]+'οῦσαν',
                 parts[0][:-6]+'οῦσα',
                 parts[0][:-6]+'οῦσαι',
                 parts[0][:-6]+'ουσῶν',
                 parts[0][:-6]+'ουσαις',
                 parts[0][:-6]+'ουσας',
                 parts[0][:-6]+'ον',
                 parts[0][:-6]+'οντος',
                 parts[0][:-6]+'οντι',
                 parts[0][:-6]+'ον',
                 parts[0][:-6]+'ον',
                 parts[0][:-6]+'οντα',
                 parts[0][:-6]+'οντων',
                 parts[0][:-6]+'οῦσιν',
                 parts[0][:-6]+'οντα']
            else:
                return [parts[0][:-6]+'υς',
                 parts[0][:-6]+'υντος',
                 parts[0][:-6]+'υντι',
                 parts[0][:-6]+'υντα',
                 parts[0][:-6]+'υς',
                 parts[0][:-6]+'υντες',
                 parts[0][:-6]+'υντων',
                 parts[0][:-6]+'ῦσιν',
                 parts[0][:-6]+'υντας',
                 parts[0][:-6]+'ῦσα',
                 parts[0][:-6]+'υσης',
                 parts[0][:-6]+'υσῃ',
                 parts[0][:-6]+'ῦσαν',
                 parts[0][:-6]+'ῦσα',
                 parts[0][:-6]+'ῦσαι',
                 parts[0][:-6]+'υσῶν',
                 parts[0][:-6]+'υσαις',
                 parts[0][:-6]+'υσας',
                 parts[0][:-6]+'υν',
                 parts[0][:-6]+'υντος',
                 parts[0][:-6]+'υντι',
                 parts[0][:-6]+'υν',
                 parts[0][:-6]+'υν',
                 parts[0][:-6]+'υντα',
                 parts[0][:-6]+'υντων',
                 parts[0][:-6]+'ῦσιν',
                 parts[0][:-6]+'υντα']
        else:
            if parts[0][:-2].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return [parts[0][:-4]+'ῶν',
                 parts[0][:-4]+'ῶντος',
                 parts[0][:-4]+'ῶντι',
                 parts[0][:-4]+'ῶντα',
                 parts[0][:-4]+'ῶν',
                 parts[0][:-4]+'ῶντες',
                 parts[0][:-4]+'ωντων',
                 parts[0][:-4]+'ῶσιν',
                 parts[0][:-4]+'ῶντας',
                 parts[0][:-4]+'ῶσα',
                 parts[0][:-4]+'ωσης',
                 parts[0][:-4]+'ωσῃ',
                 parts[0][:-4]+'ῶσαν',
                 parts[0][:-4]+'ῶσα',
                 parts[0][:-4]+'ῶσαι',
                 parts[0][:-4]+'ωσῶν',
                 parts[0][:-4]+'ωσαις',
                 parts[0][:-4]+'ωσας',
                 parts[0][:-4]+'ῶν',
                 parts[0][:-4]+'ῶντος',
                 parts[0][:-4]+'ῶντι',
                 parts[0][:-4]+'ῶν',
                 parts[0][:-4]+'ῶν',
                 parts[0][:-4]+'ῶντα',
                 parts[0][:-4]+'ωντων',
                 parts[0][:-4]+'ῶσιν',
                 parts[0][:-4]+'ῶντα']
            elif parts[0][:-2].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return [parts[0][:-4]+'ῶν',
                 parts[0][:-4]+'οῦντος',
                 parts[0][:-4]+'οῦντι',
                 parts[0][:-4]+'οῦντα',
                 parts[0][:-4]+'ῶν',
                 parts[0][:-4]+'οῦντες',
                 parts[0][:-4]+'ουντων',
                 parts[0][:-4]+'οῦσιν',
                 parts[0][:-4]+'οῦντας',
                 parts[0][:-4]+'οῦσα',
                 parts[0][:-4]+'ουσης',
                 parts[0][:-4]+'ουσῃ',
                 parts[0][:-4]+'οῦσαν',
                 parts[0][:-4]+'οῦσα',
                 parts[0][:-4]+'οῦσαι',
                 parts[0][:-4]+'ουσῶν',
                 parts[0][:-4]+'ουσαις',
                 parts[0][:-4]+'ουσας',
                 parts[0][:-4]+'οῦν',
                 parts[0][:-4]+'οῦντος',
                 parts[0][:-4]+'οῦντι',
                 parts[0][:-4]+'οῦν',
                 parts[0][:-4]+'οῦν',
                 parts[0][:-4]+'οῦντα',
                 parts[0][:-4]+'ουντων',
                 parts[0][:-4]+'οῦσιν',
                 parts[0][:-4]+'οῦντα']
            elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return [parts[0][:-4]+'ῶν',
                 parts[0][:-4]+'οῦντος',
                 parts[0][:-4]+'οῦντι',
                 parts[0][:-4]+'οῦντα',
                 parts[0][:-4]+'ῶν',
                 parts[0][:-4]+'οῦντες',
                 parts[0][:-4]+'ουντων',
                 parts[0][:-4]+'οῦσιν',
                 parts[0][:-4]+'οῦντας',
                 parts[0][:-4]+'οῦσα',
                 parts[0][:-4]+'ουσης',
                 parts[0][:-4]+'ουσῃ',
                 parts[0][:-4]+'οῦσαν',
                 parts[0][:-4]+'οῦσα',
                 parts[0][:-4]+'οῦσαι',
                 parts[0][:-4]+'ουσῶν',
                 parts[0][:-4]+'ουσαις',
                 parts[0][:-4]+'ουσας',
                 parts[0][:-4]+'οῦν',
                 parts[0][:-4]+'οῦντος',
                 parts[0][:-4]+'οῦντι',
                 parts[0][:-4]+'οῦν',
                 parts[0][:-4]+'οῦν',
                 parts[0][:-4]+'οῦντα',
                 parts[0][:-4]+'ουντων',
                 parts[0][:-4]+'οῦσιν',
                 parts[0][:-4]+'οῦντα']
            else:
                return [parts[0][:-2]+'ων',
                 parts[0][:-2]+'οντος',
                 parts[0][:-2]+'οντι',
                 parts[0][:-2]+'οντα',
                 parts[0][:-2]+'ων',
                 parts[0][:-2]+'οντες',
                 parts[0][:-2]+'οντων',
                 parts[0][:-2]+'ουσιν',
                 parts[0][:-2]+'οντας',
                 parts[0][:-2]+'ουσα',
                 parts[0][:-2]+'ουσης',
                 parts[0][:-2]+'ουσῃ',
                 parts[0][:-2]+'ουσαν',
                 parts[0][:-2]+'ουσα',
                 parts[0][:-2]+'ουσαι',
                 parts[0][:-2]+'ουσῶν',
                 parts[0][:-2]+'ουσαις',
                 parts[0][:-2]+'ουσας',
                 parts[0][:-2]+'ον',
                 parts[0][:-2]+'οντος',
                 parts[0][:-2]+'οντι',
                 parts[0][:-2]+'ον',
                 parts[0][:-2]+'ον',
                 parts[0][:-2]+'οντα',
                 parts[0][:-2]+'οντων',
                 parts[0][:-2]+'ουσιν',
                 parts[0][:-2]+'οντα']
    else:
        return 0

def ppm(verb,form):
    '''Form the Present Middle Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[0] != '-':
        if parts[0].endswith('μι'):
            if parts[0][:-4].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return [parts[0][:-6]+'αμενος',
                 parts[0][:-6]+'αμενου',
                 parts[0][:-6]+'αμενῳ',
                 parts[0][:-6]+'αμενον',
                 parts[0][:-6]+'αμενε',
                 parts[0][:-6]+'αμενοι',
                 parts[0][:-6]+'αμενων',
                 parts[0][:-6]+'αμενοις',
                 parts[0][:-6]+'αμενους',
                 parts[0][:-6]+'αμενη',
                 parts[0][:-6]+'αμενης',
                 parts[0][:-6]+'αμενῃ',
                 parts[0][:-6]+'αμενην',
                 parts[0][:-6]+'αμενη',
                 parts[0][:-6]+'αμεναι',
                 parts[0][:-6]+'αμενων',
                 parts[0][:-6]+'αμεναις',
                 parts[0][:-6]+'αμενας',
                 parts[0][:-6]+'αμενον',
                 parts[0][:-6]+'αμενου',
                 parts[0][:-6]+'αμενῳ',
                 parts[0][:-6]+'αμενον',
                 parts[0][:-6]+'αμενον',
                 parts[0][:-6]+'αμενα',
                 parts[0][:-6]+'αμενων',
                 parts[0][:-6]+'αμενοις',
                 parts[0][:-6]+'αμενα']
            elif parts[0][:-4].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return [parts[0][:-6]+'εμενος',
                 parts[0][:-6]+'εμενου',
                 parts[0][:-6]+'εμενῳ',
                 parts[0][:-6]+'εμενον',
                 parts[0][:-6]+'εμενε',
                 parts[0][:-6]+'εμενοι',
                 parts[0][:-6]+'εμενων',
                 parts[0][:-6]+'εμενοις',
                 parts[0][:-6]+'εμενους',
                 parts[0][:-6]+'εμενη',
                 parts[0][:-6]+'εμενης',
                 parts[0][:-6]+'εμενῃ',
                 parts[0][:-6]+'εμενην',
                 parts[0][:-6]+'εμενη',
                 parts[0][:-6]+'εμεναι',
                 parts[0][:-6]+'εμενων',
                 parts[0][:-6]+'εμεναις',
                 parts[0][:-6]+'εμενας',
                 parts[0][:-6]+'εμενον',
                 parts[0][:-6]+'εμενου',
                 parts[0][:-6]+'εμενῳ',
                 parts[0][:-6]+'εμενον',
                 parts[0][:-6]+'εμενον',
                 parts[0][:-6]+'εμενα',
                 parts[0][:-6]+'εμενων',
                 parts[0][:-6]+'εμενοις',
                 parts[0][:-6]+'εμενα']
            elif parts[0][:-4].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return [parts[0][:-6]+'ομενος',
                 parts[0][:-6]+'ομενου',
                 parts[0][:-6]+'ομενῳ',
                 parts[0][:-6]+'ομενον',
                 parts[0][:-6]+'ομενε',
                 parts[0][:-6]+'ομενοι',
                 parts[0][:-6]+'ομενων',
                 parts[0][:-6]+'ομενοις',
                 parts[0][:-6]+'ομενους',
                 parts[0][:-6]+'ομενη',
                 parts[0][:-6]+'ομενης',
                 parts[0][:-6]+'ομενῃ',
                 parts[0][:-6]+'ομενην',
                 parts[0][:-6]+'ομενη',
                 parts[0][:-6]+'ομεναι',
                 parts[0][:-6]+'ομενων',
                 parts[0][:-6]+'ομεναις',
                 parts[0][:-6]+'ομενας',
                 parts[0][:-6]+'ομενον',
                 parts[0][:-6]+'ομενου',
                 parts[0][:-6]+'ομενῳ',
                 parts[0][:-6]+'ομενον',
                 parts[0][:-6]+'ομενον',
                 parts[0][:-6]+'ομενα',
                 parts[0][:-6]+'ομενων',
                 parts[0][:-6]+'ομενοις',
                 parts[0][:-6]+'ομενα']
            else:
                return [parts[0][:-6]+'υμενος',
                 parts[0][:-6]+'υμενου',
                 parts[0][:-6]+'υμενῳ',
                 parts[0][:-6]+'υμενον',
                 parts[0][:-6]+'υμενε',
                 parts[0][:-6]+'υμενοι',
                 parts[0][:-6]+'υμενων',
                 parts[0][:-6]+'υμενοις',
                 parts[0][:-6]+'υμενους',
                 parts[0][:-6]+'υμενη',
                 parts[0][:-6]+'υμενης',
                 parts[0][:-6]+'υμενῃ',
                 parts[0][:-6]+'υμενην',
                 parts[0][:-6]+'υμενη',
                 parts[0][:-6]+'υμεναι',
                 parts[0][:-6]+'υμενων',
                 parts[0][:-6]+'υμεναις',
                 parts[0][:-6]+'υμενας',
                 parts[0][:-6]+'υμενον',
                 parts[0][:-6]+'υμενου',
                 parts[0][:-6]+'υμενῳ',
                 parts[0][:-6]+'υμενον',
                 parts[0][:-6]+'υμενον',
                 parts[0][:-6]+'υμενα',
                 parts[0][:-6]+'υμενων',
                 parts[0][:-6]+'υμενοις',
                 parts[0][:-6]+'υμενα']
        else:
            if parts[0][:-2].endswith('α') or parts[0][:-4].endswith('ὰ') or parts[0][:-4].endswith('ά') or parts[0][:-4].endswith('η') or parts[0][:-4].endswith('ὴ') or parts[0][:-4].endswith('ή'):
                return [parts[0][:-4]+'ωμενος',
                 parts[0][:-4]+'ωμενου',
                 parts[0][:-4]+'ωμενῳ',
                 parts[0][:-4]+'ωμενον',
                 parts[0][:-4]+'ωμενε',
                 parts[0][:-4]+'ωμενοι',
                 parts[0][:-4]+'ωμενων',
                 parts[0][:-4]+'ωμενοις',
                 parts[0][:-4]+'ωμενους',
                 parts[0][:-4]+'ωμενη',
                 parts[0][:-4]+'ωμενης',
                 parts[0][:-4]+'ωμενῃ',
                 parts[0][:-4]+'ωμενην',
                 parts[0][:-4]+'ωμενη',
                 parts[0][:-4]+'ωμεναι',
                 parts[0][:-4]+'ωμενων',
                 parts[0][:-4]+'ωμεναις',
                 parts[0][:-4]+'ωμενας',
                 parts[0][:-4]+'ωμενον',
                 parts[0][:-4]+'ωμενου',
                 parts[0][:-4]+'ωμενῳ',
                 parts[0][:-4]+'ωμενον',
                 parts[0][:-4]+'ωμενον',
                 parts[0][:-4]+'ωμενα',
                 parts[0][:-4]+'ωμενων',
                 parts[0][:-4]+'ωμενοις',
                 parts[0][:-4]+'ωμενα']
            elif parts[0][:-2].endswith('ε') or parts[0][:-4].endswith('έ') or parts[0][:-4].endswith('ὲ'):
                return [parts[0][:-4]+'ουμενος',
                 parts[0][:-4]+'ουμενου',
                 parts[0][:-4]+'ουμενῳ',
                 parts[0][:-4]+'ουμενον',
                 parts[0][:-4]+'ουμενε',
                 parts[0][:-4]+'ουμενοι',
                 parts[0][:-4]+'ουμενων',
                 parts[0][:-4]+'ουμενοις',
                 parts[0][:-4]+'ουμενους',
                 parts[0][:-4]+'ουμενη',
                 parts[0][:-4]+'ουμενης',
                 parts[0][:-4]+'ουμενῃ',
                 parts[0][:-4]+'ουμενην',
                 parts[0][:-4]+'ουμενη',
                 parts[0][:-4]+'ουμεναι',
                 parts[0][:-4]+'ουμενων',
                 parts[0][:-4]+'ουμεναις',
                 parts[0][:-4]+'ουμενας',
                 parts[0][:-4]+'ουμενον',
                 parts[0][:-4]+'ουμενου',
                 parts[0][:-4]+'ουμενῳ',
                 parts[0][:-4]+'ουμενον',
                 parts[0][:-4]+'ουμενον',
                 parts[0][:-4]+'ουμενα',
                 parts[0][:-4]+'ουμενων',
                 parts[0][:-4]+'ουμενοις',
                 parts[0][:-4]+'ουμενα']
            elif parts[0][:-2].endswith('ο') or parts[0].endswith('ὸ') or parts[0].endswith('ό') or parts[0].endswith('ω') or parts[0].endswith('ὼ') or parts[0].endswith('ώ'):
                return [parts[0][:-4]+'ουμενος',
                 parts[0][:-4]+'ουμενου',
                 parts[0][:-4]+'ουμενῳ',
                 parts[0][:-4]+'ουμενον',
                 parts[0][:-4]+'ουμενε',
                 parts[0][:-4]+'ουμενοι',
                 parts[0][:-4]+'ουμενων',
                 parts[0][:-4]+'ουμενοις',
                 parts[0][:-4]+'ουμενους',
                 parts[0][:-4]+'ουμενη',
                 parts[0][:-4]+'ουμενης',
                 parts[0][:-4]+'ουμενῃ',
                 parts[0][:-4]+'ουμενην',
                 parts[0][:-4]+'ουμενη',
                 parts[0][:-4]+'ουμεναι',
                 parts[0][:-4]+'ουμενων',
                 parts[0][:-4]+'ουμεναις',
                 parts[0][:-4]+'ουμενας',
                 parts[0][:-4]+'ουμενον',
                 parts[0][:-4]+'ουμενου',
                 parts[0][:-4]+'ουμενῳ',
                 parts[0][:-4]+'ουμενον',
                 parts[0][:-4]+'ουμενον',
                 parts[0][:-4]+'ουμενα',
                 parts[0][:-4]+'ουμενων',
                 parts[0][:-4]+'ουμενοις',
                 parts[0][:-4]+'ουμενα']
            else:
                return [parts[0][:-2]+'ομενος',
                 parts[0][:-2]+'ομενου',
                 parts[0][:-2]+'ομενῳ',
                 parts[0][:-2]+'ομενον',
                 parts[0][:-2]+'ομενε',
                 parts[0][:-2]+'ομενοι',
                 parts[0][:-2]+'ομενων',
                 parts[0][:-2]+'ομενοις',
                 parts[0][:-2]+'ομενους',
                 parts[0][:-2]+'ομενη',
                 parts[0][:-2]+'ομενης',
                 parts[0][:-2]+'ομενῃ',
                 parts[0][:-2]+'ομενην',
                 parts[0][:-2]+'ομενη',
                 parts[0][:-2]+'ομεναι',
                 parts[0][:-2]+'ομενων',
                 parts[0][:-2]+'ομεναις',
                 parts[0][:-2]+'ομενας',
                 parts[0][:-2]+'ομενον',
                 parts[0][:-2]+'ομενου',
                 parts[0][:-2]+'ομενῳ',
                 parts[0][:-2]+'ομενον',
                 parts[0][:-2]+'ομενον',
                 parts[0][:-2]+'ομενα',
                 parts[0][:-2]+'ομενων',
                 parts[0][:-2]+'ομενοις',
                 parts[0][:-2]+'ομενα']
    else:
        return 0

def ppp(verb,form):
    '''Form the Present Passive Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return ppm(verb,form)

def pfa(verb,form):
    '''Form the Future Active Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[1] != '-':
        return [parts[0][:-2]+'ων',
         parts[0][:-2]+'οντος',
         parts[0][:-2]+'οντι',
         parts[0][:-2]+'οντα',
         parts[0][:-2]+'ων',
         parts[0][:-2]+'οντες',
         parts[0][:-2]+'οντων',
         parts[0][:-2]+'ουσιν',
         parts[0][:-2]+'οντας',
         parts[0][:-2]+'ουσα',
         parts[0][:-2]+'ουσης',
         parts[0][:-2]+'ουσῃ',
         parts[0][:-2]+'ουσαν',
         parts[0][:-2]+'ουσα',
         parts[0][:-2]+'ουσαι',
         parts[0][:-2]+'ουσῶν',
         parts[0][:-2]+'ουσαις',
         parts[0][:-2]+'ουσας',
         parts[0][:-2]+'ον',
         parts[0][:-2]+'οντος',
         parts[0][:-2]+'οντι',
         parts[0][:-2]+'ον',
         parts[0][:-2]+'ον',
         parts[0][:-2]+'οντα',
         parts[0][:-2]+'οντων',
         parts[0][:-2]+'ουσιν',
         parts[0][:-2]+'οντα']
    else:
        return 0

def pfm(verb,form):
    '''Form the Future Middle Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[1] != '-':
        return [parts[0][:-2]+'ομενος',
         parts[0][:-2]+'ομενου',
         parts[0][:-2]+'ομενῳ',
         parts[0][:-2]+'ομενον',
         parts[0][:-2]+'ομενε',
         parts[0][:-2]+'ομενοι',
         parts[0][:-2]+'ομενων',
         parts[0][:-2]+'ομενοις',
         parts[0][:-2]+'ομενους',
         parts[0][:-2]+'ομενη',
         parts[0][:-2]+'ομενης',
         parts[0][:-2]+'ομενῃ',
         parts[0][:-2]+'ομενην',
         parts[0][:-2]+'ομενη',
         parts[0][:-2]+'ομεναι',
         parts[0][:-2]+'ομενων',
         parts[0][:-2]+'ομεναις',
         parts[0][:-2]+'ομενας',
         parts[0][:-2]+'ομενον',
         parts[0][:-2]+'ομενου',
         parts[0][:-2]+'ομενῳ',
         parts[0][:-2]+'ομενον',
         parts[0][:-2]+'ομενον',
         parts[0][:-2]+'ομενα',
         parts[0][:-2]+'ομενων',
         parts[0][:-2]+'ομενοις',
         parts[0][:-2]+'ομενα']
    else:
        return 0

def pfp(verb,form):
    '''Form the Future Passive Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[5] != '-':
        front = 3 if not any(parts[5].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
        return [parts[5][front:-2]+'σομενος',
         parts[5][front:-2]+'σομενου',
         parts[5][front:-2]+'σομενῳ',
         parts[5][front:-2]+'σομενον',
         parts[5][front:-2]+'σομενε',
         parts[5][front:-2]+'σομενοι',
         parts[5][front:-2]+'σομενων',
         parts[5][front:-2]+'σομενοις',
         parts[5][front:-2]+'σομενους',
         parts[5][front:-2]+'σομενη',
         parts[5][front:-2]+'σομενης',
         parts[5][front:-2]+'σομενῃ',
         parts[5][front:-2]+'σομενην',
         parts[5][front:-2]+'σομενη',
         parts[5][front:-2]+'σομεναι',
         parts[5][front:-2]+'σομενων',
         parts[5][front:-2]+'σομεναις',
         parts[5][front:-2]+'σομενας',
         parts[5][front:-2]+'σομενον',
         parts[5][front:-2]+'σομενου',
         parts[5][front:-2]+'σομενῳ',
         parts[5][front:-2]+'σομενον',
         parts[5][front:-2]+'σομενον',
         parts[5][front:-2]+'σομενα',
         parts[5][front:-2]+'σομενων',
         parts[5][front:-2]+'σομενοις',
         parts[5][front:-2]+'σομενα']
    else:
        return 0

def pa1a(verb,form):
    '''Form the First Aorist Active Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) != 0:
            if verb == 'ἀφίημι':
                return ['ἀφεις',
                 'ἀφεντος',
                 'ἀφεντι',
                 'ἀφεντα',
                 'ἀφεις',
                 'ἀφεντες',
                 'ἀφεντων',
                 'ἀφεῖσιν',
                 'ἀφεντας',
                 'ἀφεῖσα',
                 'ἀφεισης',
                 'ἀφεισῃ',
                 'ἀφεῖσαν',
                 'ἀφεῖσα',
                 'ἀφεῖσαι',
                 'ἀφεισῶν',
                 'ἀφεισαις',
                 'ἀφεισας',
                 'ἀφεν',
                 'ἀφεντος',
                 'ἀφεντι',
                 'ἀφεν',
                 'ἀφεν',
                 'ἀφεντα',
                 'ἀφεισων',
                 'ἀφεῖσιν',
                 'ἀφεντα']
            elif verb == 'γινώσκω':
                return ['γνους',
                 'γνοντος',
                 'γνοντι',
                 'γνοντα',
                 'γνους',
                 'γνοντες',
                 'γνοντων',
                 'γνοῦσιν',
                 'γνοντας',
                 'γνοῦσα',
                 'γνουσης',
                 'γνουσῃ',
                 'γνοῦσαν',
                 'γνοῦσα',
                 'γνοῦσαι',
                 'γνουσῶν',
                 'γνουσαις',
                 'γνουσας',
                 'γνον',
                 'γνοντος',
                 'γνοντι',
                 'γνον',
                 'γνον',
                 'γνοντα',
                 'γνοντων',
                 'γνοῦσιν',
                 'γνοντα']
            else:
                front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
                return [parts[2][front:]+'ς',
                 parts[2][front:]+'ντος',
                 parts[2][front:]+'ντι',
                 parts[2][front:]+'ντα',
                 parts[2][front:]+'ς',
                 parts[2][front:]+'ντες',
                 parts[2][front:]+'ντων',
                 parts[2][front:]+'σιν',
                 parts[2][front:]+'ντας',
                 parts[2][front:]+'σα',
                 parts[2][front:]+'σης',
                 parts[2][front:]+'σῃ',
                 parts[2][front:]+'σαν',
                 parts[2][front:]+'σα',
                 parts[2][front:]+'σαι',
                 parts[2][front:]+'σῶν',
                 parts[2][front:]+'σαις',
                 parts[2][front:]+'σασ',
                 parts[2][front:]+'ν',
                 parts[2][front:]+'ντος',
                 parts[2][front:]+'ντι',
                 parts[2][front:]+'ν',
                 parts[2][front:]+'ν',
                 parts[2][front:]+'ντα',
                 parts[2][front:]+'ντων',
                 parts[2][front:]+'σιν',
                 parts[2][front:]+'ντα']
        else:
            return 0
    else:
        return 0

def pa1m(verb,form):
    '''Form the First Aorist Middle Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) != 0:
            front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            return [parts[2][front:-2]+'μενος',
             parts[2][front:-2]+'μενου',
             parts[2][front:-2]+'μενῳ',
             parts[2][front:-2]+'μενον',
             parts[2][front:-2]+'μενε',
             parts[2][front:-2]+'μενοι',
             parts[2][front:-2]+'μενων',
             parts[2][front:-2]+'μενοις',
             parts[2][front:-2]+'μενους',
             parts[2][front:-2]+'μενη',
             parts[2][front:-2]+'μενης',
             parts[2][front:-2]+'μενῃ',
             parts[2][front:-2]+'μενην',
             parts[2][front:-2]+'μενη',
             parts[2][front:-2]+'μεναι',
             parts[2][front:-2]+'μενων',
             parts[2][front:-2]+'μεναις',
             parts[2][front:-2]+'μενας',
             parts[2][front:-2]+'μενον',
             parts[2][front:-2]+'μενου',
             parts[2][front:-2]+'μενῳ',
             parts[2][front:-2]+'μενον',
             parts[2][front:-2]+'μενον',
             parts[2][front:-2]+'μενα',
             parts[2][front:-2]+'μενων',
             parts[2][front:-2]+'μενοις',
             parts[2][front:-2]+'μενα']
        else:
            return 0
    else:
        return 0

def pa1p(verb,form):
    '''Form the First Aorist Passive Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[5] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) != 0:
            front = 3 if not any(parts[5].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            return [parts[5][front:-4]+'εις',
             parts[5][front:-4]+'εντος',
             parts[5][front:-4]+'εντι',
             parts[5][front:-4]+'εντα',
             parts[5][front:-4]+'εις',
             parts[5][front:-4]+'εντες',
             parts[5][front:-4]+'εντων',
             parts[5][front:-4]+'εῖσιν',
             parts[5][front:-4]+'εντας',
             parts[5][front:-4]+'εῖσα',
             parts[5][front:-4]+'εισης',
             parts[5][front:-4]+'εισῃ',
             parts[5][front:-4]+'εῖσαν',
             parts[5][front:-4]+'εῖσα',
             parts[5][front:-4]+'εισαι',
             parts[5][front:-4]+'εισῶν',
             parts[5][front:-4]+'εισαις',
             parts[5][front:-4]+'εισας',
             parts[5][front:-4]+'εν',
             parts[5][front:-4]+'εντος',
             parts[5][front:-4]+'εντι',
             parts[5][front:-4]+'εν',
             parts[5][front:-4]+'εν',
             parts[5][front:-4]+'εντα',
             parts[5][front:-4]+'εντων',
             parts[5][front:-4]+'εῖσιν',
             parts[5][front:-4]+'εντα']
        else:
            return 0
    else:
        return 0

def pa2a(verb,form):
    '''Form the Second Aorist Active Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) != 0:
            if verb == 'ἀφίημι':
                return ['ἀφεις',
                 'ἀφεντος',
                 'ἀφεντι',
                 'ἀφεντα',
                 'ἀφεις',
                 'ἀφεντες',
                 'ἀφεντων',
                 'ἀφεῖσιν',
                 'ἀφεντας',
                 'ἀφεῖσα',
                 'ἀφεισης',
                 'ἀφεισῃ',
                 'ἀφεῖσαν',
                 'ἀφεῖσα',
                 'ἀφεῖσαι',
                 'ἀφεισῶν',
                 'ἀφεισαις',
                 'ἀφεισας',
                 'ἀφεν',
                 'ἀφεντος',
                 'ἀφεντι',
                 'ἀφεν',
                 'ἀφεν',
                 'ἀφεντα',
                 'ἀφεισων',
                 'ἀφεῖσιν',
                 'ἀφεντα']
            elif verb == 'γινώσκω':
                return ['γνους',
                 'γνοντος',
                 'γνοντι',
                 'γνοντα',
                 'γνους',
                 'γνοντες',
                 'γνοντων',
                 'γνοῦσιν',
                 'γνοντας',
                 'γνοῦσα',
                 'γνουσης',
                 'γνουσῃ',
                 'γνοῦσαν',
                 'γνοῦσα',
                 'γνοῦσαι',
                 'γνουσῶν',
                 'γνουσαις',
                 'γνουσας',
                 'γνον',
                 'γνοντος',
                 'γνοντι',
                 'γνον',
                 'γνον',
                 'γνοντα',
                 'γνοντων',
                 'γνοῦσιν',
                 'γνοντα']
            else:
                front = 3 if not any(parts[2].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
                return [parts[2][front:-4]+'ων',
                     parts[2][front:-4]+'οντος',
                     parts[2][front:-4]+'οντι',
                     parts[2][front:-4]+'οντα',
                     parts[2][front:-4]+'ων',
                     parts[2][front:-4]+'οντες',
                     parts[2][front:-4]+'οντων',
                     parts[2][front:-4]+'ουσιν',
                     parts[2][front:-4]+'οντας',
                     parts[2][front:-4]+'ουσα',
                     parts[2][front:-4]+'ουσης',
                     parts[2][front:-4]+'ουσῃ',
                     parts[2][front:-4]+'ουσαν',
                     parts[2][front:-4]+'ουσα',
                     parts[2][front:-4]+'ουσαι',
                     parts[2][front:-4]+'ουσῶν',
                     parts[2][front:-4]+'ουσαις',
                     parts[2][front:-4]+'ουσας',
                     parts[2][front:-4]+'ον',
                     parts[2][front:-4]+'οντος',
                     parts[2][front:-4]+'οντι',
                     parts[2][front:-4]+'ον',
                     parts[2][front:-4]+'ον',
                     parts[2][front:-4]+'οντα',
                     parts[2][front:-4]+'οντων',
                     parts[2][front:-4]+'ουσιν',
                     parts[2][front:-4]+'οντα']
        else:
            return 0
    else:
        return 0

def pa2m(verb,form):
    '''Form the Second Aorist Middle Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[2] != '-':
        if whichAorist(verb) == 2 or whichAorist(verb) != 0:
            return [parts[0][:-2]+'ομενος',
                 parts[0][:-2]+'ομενου',
                 parts[0][:-2]+'ομενῳ',
                 parts[0][:-2]+'ομενον',
                 parts[0][:-2]+'ομενε',
                 parts[0][:-2]+'ομενοι',
                 parts[0][:-2]+'ομενων',
                 parts[0][:-2]+'ομενοις',
                 parts[0][:-2]+'ομενους',
                 parts[0][:-2]+'ομενη',
                 parts[0][:-2]+'ομενης',
                 parts[0][:-2]+'ομενῃ',
                 parts[0][:-2]+'ομενην',
                 parts[0][:-2]+'ομενη',
                 parts[0][:-2]+'ομεναι',
                 parts[0][:-2]+'ομενων',
                 parts[0][:-2]+'ομεναις',
                 parts[0][:-2]+'ομενας',
                 parts[0][:-2]+'ομενον',
                 parts[0][:-2]+'ομενου',
                 parts[0][:-2]+'ομενῳ',
                 parts[0][:-2]+'ομενον',
                 parts[0][:-2]+'ομενον',
                 parts[0][:-2]+'ομενα',
                 parts[0][:-2]+'ομενων',
                 parts[0][:-2]+'ομενοις',
                 parts[0][:-2]+'ομενα']
        else:
            return 0
    else:
        return 0

def pa2p(verb,form):
    '''Form the Second Aorist Passive Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[5] != '-':
        if whichAorist(verb) == 1 or whichAorist(verb) != 0:
            front = 3 if not any(parts[5].startswith(l) for l in 'βδγζθκλμνξπρστφχψΒΔΓΖΘΚΛΜΝΞΠΡΣΤΦΧΨ') else 0
            return [parts[5][front:-4]+'εις',
             parts[5][front:-4]+'εντος',
             parts[5][front:-4]+'εντι',
             parts[5][front:-4]+'εντα',
             parts[5][front:-4]+'εις',
             parts[5][front:-4]+'εντες',
             parts[5][front:-4]+'εντων',
             parts[5][front:-4]+'εῖσιν',
             parts[5][front:-4]+'εντας',
             parts[5][front:-4]+'εῖσα',
             parts[5][front:-4]+'εισης',
             parts[5][front:-4]+'εισῃ',
             parts[5][front:-4]+'εῖσαν',
             parts[5][front:-4]+'εῖσα',
             parts[5][front:-4]+'εισαι',
             parts[5][front:-4]+'εισῶν',
             parts[5][front:-4]+'εισαις',
             parts[5][front:-4]+'εισας',
             parts[5][front:-4]+'εν',
             parts[5][front:-4]+'εντος',
             parts[5][front:-4]+'εντι',
             parts[5][front:-4]+'εν',
             parts[5][front:-4]+'εν',
             parts[5][front:-4]+'εντα',
             parts[5][front:-4]+'εντων',
             parts[5][front:-4]+'εῖσιν',
             parts[5][front:-4]+'εντα']
        else:
            return 0
    else:
        return 0

def pea(verb,form):
    '''Form the Perfect Active Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[3] != '-':
        if verb == 'οἶδα':
            return ['εἰδως',
             'εἰδοτος',
             'εἰδοτι',
             'εἰδοτα',
             'εἰδως',
             'εἰδοτες',
             'εἰδοτων',
             'εἰδοσιν',
             'εἰδοτας',
             'εἰδυῖα',
             'εἰδυιας',
             'εἰδυιᾳ',
             'εἰδυῖαν',
             'εἰδυῖα',
             'εἰδυῖαι',
             'εἰδυιῶν',
             'εἰδυιαις',
             'εἰδυιας',
             'εἰδος',
             'εἰδοτος',
             'εἰδοτι',
             'εἰδος',
             'εἰδος',
             'εἰδοτα',
             'εἰδοτων',
             'εἰδοσιν',
             'εἰδοτα']
        else:
            return [parts[3][:-2]+'ως',
             parts[3][:-2]+'οτος',
             parts[3][:-2]+'οτι',
             parts[3][:-2]+'οτα',
             parts[3][:-2]+'ως',
             parts[3][:-2]+'οτες',
             parts[3][:-2]+'οτων',
             parts[3][:-2]+'οσιν',
             parts[3][:-2]+'οτας',
             parts[3][:-2]+'υῖα',
             parts[3][:-2]+'υιας',
             parts[3][:-2]+'υιᾳ',
             parts[3][:-2]+'υῖαν',
             parts[3][:-2]+'υῖα',
             parts[3][:-2]+'υῖαι',
             parts[3][:-2]+'υιῶν',
             parts[3][:-2]+'υιαις',
             parts[3][:-2]+'υιας',
             parts[3][:-2]+'ος',
             parts[3][:-2]+'οτος',
             parts[3][:-2]+'οτι',
             parts[3][:-2]+'ος',
             parts[3][:-2]+'ος',
             parts[3][:-2]+'οτα',
             parts[3][:-2]+'οτων',
             parts[3][:-2]+'οσιν',
             parts[3][:-2]+'οτα']
    else:
        return 0
    
def pem(verb,form):
    '''Form the Perfect Passive Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    parts = getPrincipleParts(verb,form)
    if parts[4] != '-':
        return [parts[4][:-6]+'μενος',
         parts[4][:-6]+'μενου',
         parts[4][:-6]+'μενῳ',
         parts[4][:-6]+'μενον',
         parts[4][:-6]+'μενε',
         parts[4][:-6]+'μενοι',
         parts[4][:-6]+'μενων',
         parts[4][:-6]+'μενοις',
         parts[4][:-6]+'μενους',
         parts[4][:-6]+'μενη',
         parts[4][:-6]+'μενης',
         parts[4][:-6]+'μενῃ',
         parts[4][:-6]+'μενην',
         parts[4][:-6]+'μενη',
         parts[4][:-6]+'μεναι',
         parts[4][:-6]+'μενων',
         parts[4][:-6]+'μεναις',
         parts[4][:-6]+'μενας',
         parts[4][:-6]+'μενον',
         parts[4][:-6]+'μενου',
         parts[4][:-6]+'μενῳ',
         parts[4][:-6]+'μενον',
         parts[4][:-6]+'μενον',
         parts[4][:-6]+'μενα',
         parts[4][:-6]+'μενων',
         parts[4][:-6]+'μενοις',
         parts[4][:-6]+'μενα']
    else:
        return 0

def pep(verb,form):
    '''Form the Perfect Passive Participle of the verb.
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    form -- The morphological code of the verb. Simply used in getting
            the verb's principle parts. Drawn from Mounce's "Morphology
            of Biblical Greek".
    '''
    return pem(verb,form)
      
#1 is first, 2 if second, 0 if both
def whichAorist(verb):
    '''Determine if the verb is first or second aorist, or both.
    Return 0 for both, 1 for first, or 2 for second. 
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    '''
    
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if any(verb.endswith(w) for w in ['γω','σθάνομαι','ναθάλλω','νακράζω','ποθνῄσκω','πόλλυμι','βάλλω','γίνομαι','ρχομαι','σθίω','ρίσκω','χω','θιγγάνω','κνέομαι','κάμνω','λαγχάνω','λαμβάνω','λανθάνω','λέγω','λείπω','μανθάνω','ράω','φείλω','πάσχω','περιτέμνω','πέτομαι','πίνω','πίπτω','πυνθάνομαι','συναποθνῄσκω','τέμνω','τίκτω','τρέχω','τυγχάνω','φεύγω']):
        return 2
    elif any(verb.endswith(w) for w in ['ρέω','μαρτάνω','ἀφίημι','γινώσκω']):
        return 1
    elif verb == 'ἐφάλλομαι':
        return 2
    else:
        return 1
    
def whichPerfect(verb):
    '''Determine if the verb is first or second perfect (or future),
    or both. Return 0 for both, 1 for first, or 2 for second. 
    
    Keyword arguments:
    verb -- The present indicative, first person singular of the verb.
    '''
    
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if any(verb.endswith(w) for w in ['κούω','νοίγω','γίνομαι','γράφω','διατάσσω','κφεύγω','εἴκω','ρχομαι','κράζω','λαμβάνω','λλυμι','πάσχω','πείθω','πράσσω','προσφέρω','σήπω','τυγχάνω']):
        return 2
    else:
        return 1
