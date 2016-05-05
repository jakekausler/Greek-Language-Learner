# -*- coding: utf-8 -*-
'''
Created on Jun 6, 2014

@author: Jake

Generate a pronoun based on a word and given morphological features.
'''
def generatePronounForms(pronoun,gender,number,case):
    '''Generate and return a pronoun based on a word and given
    morphological features. A value of 0 in any position means the
    word cannot be found in that form. Only returns one form (e.g. the
    nms).
    
    Keyword arguments:
    pronoun -- The masculine singular nominative form of the pronoun.
    gender -- The gender of the pronoun. 1 is masculine, 2 is feminine,
              3 is neuter.
    number -- The number of the pronoun. 1 is singular, 2 is plural.
    case -- The case of the pronoun. 1 is nominative, 2 is genitive,
            3 is dative, 4 is accusative.
    '''
    if pronoun in ['αὐτός','οὗτος','ὅς','τίς','τὶς','τὶς','ἴδιος','ἐμός','σός','ἡμέτερος','ὑμέτερος','ὅσος','ἐκεῖνος','πόσος','ποῖος','ἄλλος','ἕτερος','ἕκαστος','πολύς','ὅδε','τοσοῦτος','τοιοῦτος']:
        if number == 1:
            if gender == 1:
                if case == 1:
                    if pronoun in ['ἡμέτερος','ὅσος','ποῖος','ὅδε']:
                        return 0
                    return pronoun
                elif case == 2:
                    if pronoun in ['οὗτος']:
                        return 'τουτου'
                    elif pronoun in ['ὅς']:
                        return 'οὗ'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινος'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιου'
                    elif pronoun in ['ἐμός']:
                        return 0
                    elif pronoun in ['ἐμός']:
                        return 0
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['ἐκεῖνος']:
                        return pronoun[:-2]+'υ'
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return pronoun[:-2]+'υ'
                    elif pronoun in ['ἄλλος']:
                        return pronoun[:-2]+'υ'
                    elif pronoun in ['ἕτερος']:
                        return pronoun[:-2]+'υ'
                    elif pronoun in ['ἕκαστος']:
                        return pronoun[:-2]+'υ'
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λoῦ'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    elif pronoun in ['τοιοῦτος']:
                        return pronoun[:-2]+'υ'
                    else:
                        return pronoun[:-2]+'ῦ'
                elif case == 3:
                    if pronoun in ['οὗτος']:
                        return 'τουτῳ'
                    elif pronoun in ['ὅς']:
                        return 'ᾧ'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινι'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιῳ'
                    elif pronoun in ['ἐμός']:
                        return 'ἐμῳ'
                    elif pronoun in ['σός']:
                        return 'σῷ'
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λῷ'
                    elif pronoun in ['ὅδε']:
                        return 0
                    else:
                        return pronoun[:-4]+'ῳ'
                elif case ==4:
                    if pronoun in ['οὗτος']:
                        return 'τοῦτον'
                    elif pronoun in ['ὅς']:
                        return 'ὃν'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινα'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιον'
                    elif pronoun in ['ἐμός']:
                        return 'ἐμον'
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return pronoun[:-2]+'ν'
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ὅδε']:
                        return 0
                    else:
                        return pronoun[:-2]+'ν'
                else:
                    return 0
            elif gender == 2:
                if case == 1:
                    if pronoun in ['οὗτος']:
                        return 'αυτη'
                    elif pronoun in ['ὅς']:
                        return 'ἥ'
                    elif pronoun in ['τίς','τὶς']:
                        return pronoun
                    elif pronoun in ['ἴδιος']:
                        return 0
                    elif pronoun in ['ἐμός']:
                        return 'ἐμη'
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος','ὑμέτερος']:
                        return pronoun[:-4]+'α'
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return pronoun[:-4]+'α'
                    elif pronoun in ['ἕτερος']:
                        return pronoun[:-4]+'α'
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λη'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    else:
                        return pronoun[:-4]+'η'
                elif case == 2:
                    if pronoun in ['οὗτος']:
                        return 'ταυτης'
                    elif pronoun in ['ὅς']:
                        return 'ἧ'
                    elif pronoun in ['τίς','τὶς']:
                        return 0
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιας'
                    elif pronoun in ['ἐμός']:
                        return 'ἐμῆς'
                    elif pronoun in ['σός']:
                        return 'σῆς'
                    elif pronoun in ['ἡμέτερος','ὑμέτερος']:
                        return pronoun[:-4]+'ας'
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return pronoun[:-4]+'ας'
                    elif pronoun in ['ἕτερος']:
                        return pronoun[:-4]+'ας'
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λῆς'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    elif pronoun in ['τοιοῦτος']:
                        return 0
                    else:
                        return pronoun[:-4]+'ης'
                elif case == 3:
                    if pronoun in ['οὗτος']:
                        return 'ταυτῃ'
                    elif pronoun in ['ὅς']:
                        return 'ᾑ'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινι'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιᾳ'
                    elif pronoun in ['ἐμός']:
                        return 'ἐμῇ'
                    elif pronoun in ['σός']:
                        return 'σῇ'
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return pronoun[:-4]+'ᾳ'
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return pronoun[:-2]+'υ'
                    elif pronoun in ['ποῖος']:
                        return pronoun[:-4]+'ᾳ'
                    elif pronoun in ['ἄλλος']:
                        return 0
                    elif pronoun in ['ἕτερος']:
                        return pronoun[:-4]+'ᾳ'
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λῇ'
                    elif pronoun in ['ὅδε']:
                        return 'τῇδε'
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    elif pronoun in ['τοιοῦτος']:
                        return 0
                    else:
                        return pronoun[:-4]+'ῃ'
                elif case ==4:
                    if pronoun in ['οὗτος']:
                        return 'ταυτην'
                    elif pronoun in ['ὅς']:
                        return 'ἥν'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινα'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιαν'
                    elif pronoun in ['ἐμός']:
                        return 'ἐμην'
                    elif pronoun in ['σός']:
                        return 'σην'
                    elif pronoun in ['ἡμέτερος','ὑμέτερος']:
                        return pronoun[:-4]+'αν'
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return pronoun[:-4]+'αν'
                    elif pronoun in ['ἕτερος']:
                        return pronoun[:-4]+'αν'
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λην'
                    elif pronoun in ['ὅδε']:
                        return 'τηνδε'
                    else:
                        return pronoun[:-4]+'ην'
                else:
                    return 0
            elif gender == 3:
                if case == 1:
                    if pronoun in ['οὗτος']:
                        return 'τοῦτο'
                    elif pronoun in ['ὅς']:
                        return 'ὅ'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τι'
                    elif pronoun in ['ἴδιος']:
                        return 0
                    elif pronoun in ['ἐμός']:
                        return 'ἐμον'
                    elif pronoun in ['σός']:
                        return 'σον'
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return pronoun[:-2]+'ν'
                    elif pronoun in ['ἐκεῖνος']:
                        return pronoun[:-2]
                    elif pronoun in ['πόσος']:
                        return pronoun[:-2]+'ν'
                    elif pronoun in ['ἕκαστος']:
                        return pronoun[:-2]+'ν'
                    elif pronoun in ['πολύς']:
                        return 'πλεῖον'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    elif pronoun in ['τοιοῦτος']:
                        return 0
                    else:
                        return pronoun[:-2]
                elif case == 2:
                    if pronoun in ['οὗτος']:
                        return 'τουτου'
                    elif pronoun in ['ὅς']:
                        return 'οὗ'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινος'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιου'
                    elif pronoun in ['ἐμός']:
                        return 0
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['ἐκεῖνος']:
                        return pronoun[:-2]+'υ'
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return 0
                    elif pronoun in ['ἄλλος']:
                        return pronoun[:-2]+'υ'
                    elif pronoun in ['ἕτερος']:
                        return 0
                    elif pronoun in ['ἕκαστος']:
                        return pronoun[:-2]+'υ'
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λοῦ'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return pronoun[:-2]+'υ'
                    elif pronoun in ['τοιοῦτος']:
                        return 0
                    else:
                        return pronoun[:-2]+'ῦ'
                elif case == 3:
                    if pronoun in ['οὗτος']:
                        return 'τουτῳ'
                    elif pronoun in ['ὅς']:
                        return 'ᾧ'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινι'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιῳ'
                    elif pronoun in ['ἐμός']:
                        return 'ἐμῷ'
                    elif pronoun in ['σός']:
                        return 'σῷ'
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return pronoun[:-4]+'ῳ'
                    elif pronoun in ['ἐκεῖνος']:
                        return 0
                    elif pronoun in ['ἄλλος']:
                        return pronoun[:-4]+'ῳ'
                    elif pronoun in ['ἕκαστος']:
                        return pronoun[:-4]+'ῳ'
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λῷ'
                    
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return pronoun[:-4]+'ῳ'
                    elif pronoun in ['τοιοῦτος']:
                        return 0
                    else:
                        return pronoun[:-4]+'ῷ'
                elif case ==4:
                    if pronoun in ['οὗτος']:
                        return 'τοῦτο'
                    elif pronoun in ['ὅς']:
                        return 'ὅ'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τι'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιον'
                    elif pronoun in ['ἐμός']:
                        return 'ἐμον'
                    elif pronoun in ['σός']:
                        return 'σον'
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return pronoun[:-2]+'ν'
                    elif pronoun in ['ἐκεῖνος']:
                        return pronoun[:-2]
                    elif pronoun in ['πόσος']:
                        return pronoun[:-2]+'ν'
                    elif pronoun in ['ἕκαστος']:
                        return pronoun[:-2]+'ν'
                    elif pronoun in ['πολύς']:
                        return 'πλεῖον'
                    elif pronoun in ['ὅδε']:
                        return 0
                    else:
                        return pronoun[:-2]
                else:
                    return 0
        elif number == 2:
            if gender == 1:
                if case == 1:
                    if pronoun in ['ὅς']:
                        return 'οἳ'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινες'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιοι'
                    elif pronoun in ['ἐμός']:
                        return 0
                    elif pronoun in ['σός']:
                        return 'σοι'
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λοι'
                    elif pronoun in ['ὅδε']:
                        return 0
                    else:
                        return pronoun[:-2]+'ι'
                elif case == 2:
                    if pronoun in ['οὗτος']:
                        return 'τουτων'
                    elif pronoun in ['ὅς']:
                        return 'ὧν'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινων'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιων'
                    elif pronoun in ['ἐμός']:
                        return 0
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['ἐκεῖνος']:
                        return pronoun[:-4]+'ων'
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return 0
                    elif pronoun in ['ἄλλος']:
                        return pronoun[:-4]+'ων'
                    elif pronoun in ['ἕτερος']:
                        return pronoun[:-4]+'ων'
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λῶν'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return pronoun[:-4]+'ων'
                    elif pronoun in ['τοιοῦτος']:
                        return 0
                    else:
                        return pronoun[:-4]+'ῶν'
                elif case == 3:
                    if pronoun in ['οὗτος']:
                        return 'τουτοις'
                    elif pronoun in ['ὅς']:
                        return 'οἷς'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τισιν'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιοις'
                    elif pronoun in ['ἐμός']:
                        return 0
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος']:
                        return pronoun[:-2]+'ις'
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['ἐκεῖνος']:
                        return pronoun[:-2]+'ις'
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return 0
                    elif pronoun in ['ἄλλος']:
                        return pronoun[:-2]+'ις'
                    elif pronoun in ['ἕτερος']:
                        return pronoun[:-2]+'ις'
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λοῖς'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    elif pronoun in ['τοιοῦτος']:
                        return pronoun[:-2]+'ις'
                    else:
                        return pronoun[:-2]+'ῖς'
                elif case ==4:
                    if pronoun in ['οὗτος']:
                        return 'τουτους'
                    elif pronoun in ['ὅς']:
                        return 'οὓς'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινας'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιους'
                    elif pronoun in ['ἐμός']:
                        return 'εμους'
                    elif pronoun in ['σός']:
                        return 'σους'
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ἐκεῖνος']:
                        return pronoun[:-2]+'υς'
                    elif pronoun in ['ποῖος']:
                        return 0
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λους'
                    elif pronoun in ['ὅδε']:
                        return 0
                    else:
                        return pronoun[:-2]+'υς'
                else:
                    return 0
            elif gender == 2:
                if case == 1:
                    if pronoun in ['αὐτός']:
                        return 0
                    elif pronoun in ['οὗτος']:
                        return 'αυται'
                    elif pronoun in ['ὅς']:
                        return 'αἳ'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινες'
                    elif pronoun in ['ἴδιος']:
                        return 0
                    elif pronoun in ['ἐμός']:
                        return 0
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return 0
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λαι'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    else:
                        return pronoun[:-4]+'αι'
                elif case == 2:
                    if pronoun in ['οὗτος']:
                        return 'τουτων'
                    elif pronoun in ['ὅς']:
                        return 'ὧν'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινων'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιων'
                    elif pronoun in ['ἐμός']:
                        return 0
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος']:
                        return pronoun[:-4]+'ων'
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['ἐκεῖνος']:
                        return 0
                    elif pronoun in ['πόσος']:
                        return pronoun[:-4]+'ων'
                    elif pronoun in ['ποῖος']:
                        return 0
                    elif pronoun in ['ἄλλος']:
                        return 0
                    elif pronoun in ['ἕτερος']:
                        return 0
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λῶν'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    elif pronoun in ['τοιοῦτος']:
                        return 0
                    else:
                        return pronoun[:-4]+'ῶν'
                elif case == 3:
                    if pronoun in ['οὗτος']:
                        return 'ταυταις'
                    elif pronoun in ['ὅς']:
                        return 'αἷς'
                    elif pronoun in ['τίς','τὶς']:
                        return 0
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιαις'
                    elif pronoun in ['ἐμός']:
                        return 0
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος']:
                        return pronoun[:-4]+'αις'
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['ἐκεῖνος']:
                        return pronoun[:-4]+'αις'
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return 0
                    elif pronoun in ['ἄλλος']:
                        return 0
                    elif pronoun in ['ἕτερος']:
                        return pronoun[:-4]+'αις'
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λαῖς'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    elif pronoun in ['τοιοῦτος']:
                        return pronoun[:-4]+'αις'
                    else:
                        return pronoun[:-4]+'αῖς'
                elif case ==4:
                    if pronoun in ['οὗτος']:
                        return 'ταυτας'
                    elif pronoun in ['ὅς']:
                        return 'ἃς'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινας'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιας'
                    elif pronoun in ['ἐμός']:
                        return 'εμας'
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['ἕτερος']:
                        return 0
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λας'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    else:
                        return pronoun[:-4]+'ας'
                else:
                    return 0
            elif gender == 3:
                if case == 1:
                    if pronoun in ['οὗτος']:
                        return 'ταυτα'
                    elif pronoun in ['ὅς']:
                        return 'ἃ'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινα'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδια'
                    elif pronoun in ['ἐμός']:
                        return 'εμα'
                    elif pronoun in ['σός']:
                        return 'σα'
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ἐκεῖνος']:
                        return 0
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return 0
                    elif pronoun in ['ἕτερος']:
                        return 0
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λα'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοιοῦτος']:
                        return 0
                    else:
                        return pronoun[:-4]+'α'
                elif case == 2:
                    if pronoun in ['οὗτος']:
                        return 'τουτων'
                    elif pronoun in ['ὅς']:
                        return 'ὧν'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινων'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιων'
                    elif pronoun in ['ἐμός']:
                        return 'εμῶν'
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return pronoun[:-4]+'ων'
                    elif pronoun in ['ἐκεῖνος']:
                        return pronoun[:-4]+'ων'
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return 0
                    elif pronoun in ['ἄλλος']:
                        return 0
                    elif pronoun in ['ἕτερος']:
                        return 0
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λῶν'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    elif pronoun in ['τοιοῦτος']:
                        return pronoun[:-4]+'ων'
                    else:
                        return pronoun[:-4]+'ῶν'
                elif case == 3:
                    if pronoun in ['οὗτος']:
                        return 'τουτοις'
                    elif pronoun in ['ὅς']:
                        return 'οἷς'
                    elif pronoun in ['τίς','τὶς']:
                        return 0
                    elif pronoun in ['ἴδιος']:
                        return 'ιδιοις'
                    elif pronoun in ['ἐμός']:
                        return 'εμοῖς'
                    elif pronoun in ['σός']:
                        return 0
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ὅσος']:
                        return 0
                    elif pronoun in ['ἐκεῖνος']:
                        return 0
                    elif pronoun in ['πόσος']:
                        return 0
                    elif pronoun in ['ποῖος']:
                        return 0
                    elif pronoun in ['ἄλλος']:
                        return 0
                    elif pronoun in ['ἕτερος']:
                        return pronoun[:-2]+'ις'
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λοῖς'
                    elif pronoun in ['ὅδε']:
                        return 0
                    elif pronoun in ['τοσοῦτος']:
                        return 0
                    elif pronoun in ['τοιοῦτος']:
                        return pronoun[:-2]+'ις'
                    else:
                        return pronoun[:-2]+'ῖς'
                elif case ==4:
                    if pronoun in ['οὗτος']:
                        return 'ταυτα'
                    elif pronoun in ['ὅς']:
                        return 'ἃ'
                    elif pronoun in ['τίς','τὶς']:
                        return 'τινα'
                    elif pronoun in ['ἴδιος']:
                        return 'ιδια'
                    elif pronoun in ['ἐμός']:
                        return 'εμα'
                    elif pronoun in ['σός']:
                        return 'σα'
                    elif pronoun in ['ἡμέτερος']:
                        return 0
                    elif pronoun in ['ὑμέτερος']:
                        return 0
                    elif pronoun in ['ἕκαστος']:
                        return 0
                    elif pronoun in ['πολύς']:
                        return pronoun[:-4]+'λα'
                    elif pronoun in ['ὅδε']:
                        return 'ταδε'
                    else:
                        return pronoun[:-4]+'α'
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    elif pronoun in ['τοιόσδε']:
        if case == 3 and number == 1 and gender == 2:
            return 'τοιᾶσδε'
        else:
            return 0
    elif pronoun in ['ὅστις','τηλικοῦτος']:
        if case == 1:
            if gender == 1:
                if number == 1:
                    return pronoun
                elif number == 2:
                    if pronoun in ['ὅστις']:
                        return 'οἵτινες'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 2:
                if number == 1:
                    if pronoun in ['ὅστις']:
                        return 'ἥτις'
                    else:
                        return 0
                elif number == 2:
                    if pronoun in ['ὅστις']:
                        return 'αἵτινες'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 3:
                if number == 2:
                    if pronoun in ['ὅστις']:
                        return 'ἅτινα'
                    elif pronoun in ['τηλικοῦτος']:
                        return pronoun[:-4]+'α'
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        elif case == 2:
            if gender == 1:
                if number == 1:
                    if pronoun in ['τηλικοῦτος']:
                        return pronoun[:-2]+'υ'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 2:
                if number == 1:
                    if pronoun in ['τηλικοῦτος']:
                        return pronoun[:-4]+'ης'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 3:
                if number == 1:
                    if pronoun in ['ὅστις']:
                        return 'ὅτου'
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    elif pronoun in ['οἷος','ὁποῖος','ποταπός']:
        if number == 1:
            if gender == 1:
                if case == 1:
                    if pronoun in ['οἷος','ὁποῖος','ποταπός']:
                        return pronoun
                    else:
                        return 0
                elif case == 4:
                    if pronoun in ['οἷος']:
                        return pronoun[:-2]+'ν'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 2:
                if case == 1:
                    if pronoun in ['οἷος']:
                        return pronoun[:-4]+'α'
                    elif pronoun in ['ποταπός']:
                        return pronoun[:-4]+'η'
                    else:
                        return 0
                elif case == 4:
                    if pronoun in ['ὁποῖος']:
                        return pronoun[:-4]+'αν'
                    elif pronoun in ['ποταπός']:
                        return pronoun[:-4]+'ην'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 3:
                if case == 1:
                    if pronoun in ['οἷος','ὁποῖος']:
                        return pronoun[:-2]+'ν'
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        elif number == 2:
            if gender == 1:
                if case == 1:
                    if pronoun in ['οἷος','ὁποῖος','ποταπός']:
                        return pronoun[:-2]+'ι'
                elif case == 4:
                    if pronoun in ['οἷος','ποταπός']:
                        return pronoun[:-2]+'υς'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 2:
                if case == 1:
                    if pronoun in ['ποταπός']:
                        return pronoun[:-4]+'αι'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 3:
                if case == 1:
                    if pronoun in ['οἷος']:
                        return pronoun[:-4]+'α'
                    else:
                        return 0
                elif case == 4:
                    if pronoun in ['οἷος']:
                        return pronoun[:-4]+'α'
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    elif pronoun in ['ἡλίκος']:
        if number == 1:
            if case == 1:
                if gender == 3:
                    return pronoun[:-2]+'ν'
                else:
                    return 0
            elif case == 4:
                if gender == 1:
                    return pronoun[:-2]+'ν'
                elif gender == 2:
                    return pronoun[:-4]+'ην'
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    elif pronoun in ['πηλίκος']:
        if number == 1:
            if gender == 1:
                if case == 1:
                    return pronoun
                else:
                    return 0
            else:
                return 0
        elif number == 2:
            if gender == 3:
                if case == 3:
                    return pronoun[:-2]+'ις'
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    elif pronoun in ['ἀμφότεροι']:
        if number == 2:
            if gender == 1:
                if case == 1:
                    return pronoun
                elif case == 2:
                    return pronoun[:-4]+'ων'
                elif case == 3:
                    return pronoun[:-2]+'ις'
                elif case == 4:
                    return pronoun[:-2]+'υς'
                else:
                    return 0
            elif gender == 3:
                if case == 4:
                    return pronoun[:-4]+'α'
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    elif pronoun in ['ἐγώ','σύ']:
        if number == 1:
            if case == 1:
                if pronoun in ['ἐγώ']:
                    return pronoun
                elif pronoun in ['σύ']:
                    return pronoun
                else:
                    return 0
            elif case == 2:
                if pronoun in ['ἐγώ']:
                    return 'μου'
                elif pronoun in ['σύ']:
                    return 'σου'
                else:
                    return 0
            elif case == 3:
                if pronoun in ['ἐγώ']:
                    return 'μοι'
                elif pronoun in ['σύ']:
                    return 'σοι'
                else:
                    return 0
            elif case == 4:
                if pronoun in ['ἐγώ']:
                    return 'με'
                elif pronoun in ['σύ']:
                    return 'σε'
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    elif pronoun in ['ἡμεῖς','ὑμεῖς']:
        if number == 2:
            if case == 1:
                if pronoun in ['ἡμεῖς']:
                    return pronoun
                elif pronoun in ['ὑμεῖς']:
                    return pronoun
                else:
                    return 0
            elif case == 2:
                if pronoun in ['ἡμεῖς']:
                    return 'ἡμῶν'
                elif pronoun in ['ὑμεῖς']:
                    return 'ὑμῶν'
                else:
                    return 0
            elif case == 3:
                if pronoun in ['ἡμεῖς']:
                    return 'ἡμῖν'
                elif pronoun in ['ὑμεῖς']:
                    return 'ὑμῖν'
                else:
                    return 0
            elif case == 4:
                if pronoun in ['ἡμεῖς']:
                    return 'ἡμᾶς'
                elif pronoun in ['ὑμεῖς']:
                    return 'ὑμᾶς'
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    elif pronoun in ['ἀλλήλων']:
        if number == 2:
            if gender == 1:
                if case == 2:
                    return pronoun
                elif case == 3:
                    return pronoun[:-4]+'οις'
                elif case == 4:
                    return pronoun[:-4]+'ους'
                else:
                    return 0
            elif gender == 3:
                if case == 2:
                    return pronoun
                elif case == 3:
                    return pronoun[:-4]+'οις'
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    elif pronoun in ['ἑαυτοῦ','ἀλλότριος']:
        if number == 1:
            if gender == 1:
                if case == 2:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun
                    else:
                        return 0
                elif case == 3:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-5]+'ῷ'
                    elif pronoun in ['ἀλλότριος']:
                        return pronoun[:-4]+'ῳ'
                    else:
                        return 0
                elif case == 4:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-3]+'ν'
                    elif pronoun in ['ἀλλότριος']:
                        return pronoun[:-2]+'ν'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 2:
                if case == 2:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-5]+'ῆς'
                    else:
                        return 0
                elif case == 3:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-5]+'ῇ'
                    elif pronoun in ['ἀλλότριος']:
                        return pronoun[:-4]+'ᾳ'
                    else:
                        return 0
                elif case == 4:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-5]+'ην'
                    elif pronoun in ['ἀλλότριος']:
                        return pronoun[:-4]+'αν'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 3:
                if case == 2:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun
                    else:
                        return 0
                elif case == 3:
                    if pronoun in ['ἀλλότριος']:
                        return pronoun[:-4]+'ῳ'
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        elif number == 2:
            if gender == 1:
                if case == 2:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-5]+'ῶν'
                    elif pronoun in ['ἀλλότριος']:
                        return pronoun[:-4]+'ων'
                    else:
                        return 0
                elif case == 3:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-3]+'ῖς'
                    elif pronoun in ['ἀλλότριος']:
                        return pronoun[:-2]+'ις'
                    else:
                        return 0
                elif case == 4:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-3]+'υς'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 2:
                if case == 2:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-5]+'ῶν'
                    else:
                        return 0
                elif case == 3:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-5]+'αῖς'
                    elif pronoun in ['ἀλλότριος']:
                        return pronoun[:-4]+'αις'
                    else:
                        return 0
                elif case == 4:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-5]+'ας'
                    else:
                        return 0
                else:
                    return 0
            elif gender == 3:
                if case == 2:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-5]+'ῶν'
                    else:
                        return 0
                elif case == 4:
                    if pronoun in ['ἑαυτοῦ']:
                        return pronoun[:-5]+'α'
                    else:
                        return 0
                else:
                    return 0
        else:
            return 0
    elif pronoun in ['σεαυτοῦ','ἐμαυτοῦ']:
        if number == 1:
            if gender == 1:
                if case == 2:
                    return pronoun
                elif case == 3:
                    return pronoun[:-5]+'ῷ'
                elif case == 4:
                    return pronoun[:-3]+'v'
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0
