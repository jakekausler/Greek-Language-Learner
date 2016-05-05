# -*- coding: utf-8 -*-
'''
Created on May 3, 2014

@author: Jake

Generate adjective forms based on a given morphological code and root.
'''

def generateAdjectiveForms(adjective, style):
    '''Generates the forms of an adjective based on a certain
    morphological code. A value of 0 in any position means the word
    cannot be found in that form. The forms are returned as:
        [mns, mgs, mds, mcs, mvs,
         mnp, mgp, mdp, mcp,
         fns, fgs, fds, fcs, fvs,
         fnp, fgp, fdp, fcp,
         nns, ngs, nds, ncs, nvs,
         nnp, ngp, ndp, ncp]
    
    Keyword arguments:
    adjective -- Root of the adjective to generate (nominative
                 masculine singular).
    style -- Style code of the adjective. Different codes form
             differently. Drawn from Mounce's "Morphology of
             Biblical Greek"
    '''
    # Match the style and call the correct function
    styles = {'a1a':a1a,
              'a1b':a1b,
              'a2a':a2a,
              'a2b':a2b,
              'a3a':a3a,
              'a3b':a3b,
              'a4a':a4a,
              'a4b':a4b,
              'a4c':a4c,
              'a5a':a5a,
              'a5b':a5b}
    return styles[style](adjective)

def a1a(adjective):
    '''a1a - Uncontracted Stems (2-1-2).
    
    Keyword arguments:
    adjective -- Nominative, masculine, singular root of the adjective
    '''
    if adjective in ['ἅγιος','ἄγριος','Ἀθηναῖος','αἴγειος','Αἰγύπτιος','αἰσχρός','αἴτιος','ἀκρογωνιαῖος','ἀλλότριος','ἀμφότεροι','ἀναγκαῖος','ἄξιος','ἀργύρεος','ἄρειος','ἀριστερός','ἄρτιος','ἀρχαῖος','ἀστεῖος','αὐστηρός','αὐχμηρός','βέβαιος','Βεροιαῖος','βίαιος','βλαβερός','βλητέος','Γαλιλαῖος','γνήσιος','γυναικεῖος','Δερβαῖος','δεξιός','δευτεραῖος','δεύτερος','δημόσιος','διακόσιοι','δίκαιος','δισχίλιοι','δόλιος','ἑκούσιος','ἐλαφρός','ἐλεύθερος','ἐναντίος','ἐνεός','ἐννεός','ἐντόπιος','ἑξακόσιοι','ἐπιτήδειος','ἐπτακισχίλιοι','ἐρυθρός','ἕτερος','Ἐφεσῖνος','Ἐφέσιος','ἐχθρός','ἡμέτερος','ἤπιος','θαυμάσιος','θεῖος','ἴδιος','ἱερός','ἱλαρός','Ἰουδαῖος','ἰσχυρός','καθαρός','κραταιός','κρυφαῖος','κρύφιος','λαμπρός','λεῖος','λεπρός','λιπαρός','λόγιος','μακάριος','μακρός','μάταιος','μεγαλεῖος','μικρός','μύριοι','μυρίος','μωρός','νεκρός','νέος','νήπιος','νηφαλέος','νηφάλιος','νωθρός','ξηρός','οἷος','ὀκνηρός','ὅμοιος','ὁποῖος','ὄρθριος','ὅσιος','ὄψιος','παλαιός','παραθαλάσσιος','παραπλήσιος','πατρῷος','πενιχρός','πεντακισχίλιοι','πεντακόσιοι','περαιτέρος','πικρός','Πισίδιος','πλούσιος','ποῖος','πονηρός','πυρρός','ῥυπαρός','Ῥωμαῖος','σαπρός','Σιδώνιος','σκληρός','σκολιός','Σμυρναῖος','σπουδαῖος','στερεός','ταλαντιαῖος','τέλειος','τεταρταῖος','τετρακισχίλιοι','τίμιος','τριακόσιοι','τρισχίλιοι','ὑγρός','ὑμέτερος','ὑπεναντίος','ὕστερος','φανερός','φοβερός','χάλκεος','Χαναναῖος','χίλιοι','χλιαρός','χλωρός','χρύσεος','ψυχρός','ὡραῖος']:
        return [adjective,
         adjective[:-2]+'υ',
         adjective[:-4]+'ῳ',
         adjective[:-2]+'ν',
         adjective[:-4]+'ε',
         adjective[:-2]+'ι',
         adjective[:-4]+'ων',
         adjective[:-2]+'ις',
         adjective[:-2]+'υς',
         adjective[:-4]+'α',
         adjective[:-4]+'ας',
         adjective[:-4]+'ᾳ',
         adjective[:-4]+'αν',
         adjective[:-4]+'α',
         adjective[:-4]+'αι',
         adjective[:-4]+'ων',
         adjective[:-4]+'αις',
         adjective[:-4]+'ας',
         adjective[:-2]+'ν',
         adjective[:-2]+'υ',
         adjective[:-4]+'ῳ',
         adjective[:-2]+'ν',
         adjective[:-2]+'ν',
         adjective[:-4]+'α',
         adjective[:-4]+'ων',
         adjective[:-2]+'ις',
         adjective[:-4]+'α']
    elif adjective in ['ἀγαθός','ἀγαπητός','ἁγιώτατος','ἁγνός','Ἀδραμυττηνός','αἱρετικός','ἀκάνθινος','ἀκριβέστατος','Ἀλεξανδρῖνος','ἀληθινός','ἁλυκός','ἀμαράντινος','ἀνατολικός','ἀνθρώπινος','ἀνωτερικός','ἁπαλός','ἀργός','ἀρεστός','ἀρκετός','αὐτόματος','βασιλικός','βδελυκτός','βιωτικός','βύσσινος','Γαδαρηνός','Γαλατικός','γεννητός','Γερασηνός','Γεργεσηνός','γνωστός','γραπτός','γυμνός','Δαμασκηνός','δειλός','δεινός','δέκατος','δεκτός','δερμάτινος','δῆλος','διδακτικός','διδακτός','διπλόος','δυνατός','δωδέκατος','ἕβδομος','Ἑβραϊκός','ἐθνικός','εἰρηνικός','ἕκαστος','ἐκλεκτός','ἕκτος','ἐλάχιστος','ἐλεεινός','ἐλεφάντινος','Ἑλληνικός','ἐμός','ἔνατος','ἑνδέκατος','ἐξουσιαστικός','ἐπαρχικός','ἑσπερινός','ἔσχατος','εὐλογητός','ζεστός','ἡλίκος','θαυμαστός','θνητός','θύϊνος','ἱκανός','Ἰουδαϊκός','ἱππικός','ἴσος','Ἰταλικός','καθημερινός','καθολικός','καινός','κακός','καλός','Καλοί Λιμένες','καταμόνας','κενός','κεραμικός','κλητός','κοινός','κοινωνικός','κόκκινος','κοσμικός','κράτιστος','κρίθινος','κριτικός','κρυπτός','κυλλός','κυριακός','κωφός','λαξευτός','λειτουργικός','λεπτός','Λευιτικός','λευκοβύσσινος','λευκός','λίθινος','λογικός','λοιπός','μαλακός','μέγας','μέγιστος','μέσος','μεστός','μόνος','μουσικός','μυλικός','μύλινος','μυλωνικός','Ναζαρηνός','νεωτερικός','νόθος','νομικός','ξένος','ξύλινος','ὄγδοος','ὀλίγος','ὅλος','ὀνικός','ὀπτός','ὁρατός','ὀργίλος','ὀρεινός','ὀρθός','ὀρθρινός','ὀρφανός','ὅσος','ὀστράκινος','παθητός','Πακατιανός','πάμπολυς','παραλυτικός','πατρικός','πεδινός','πεζός','πειθός','πέμπτος','πεντεκαιδέκατος','περισσός','πηλίκος','πιθός','πιστικός','πιστός','πλαστός','πλεῖστος','πνευματικός','πνικτός','ποδαπός','ποικίλος','πολύς','Ποντικός','πόσος','ποταπός','πρᾶος','προβατικός','προφητικός','πρωϊνός','πρῶτος','πτωχός','πυκνός','πύρινος','Ῥωμαϊκός','σαρκικός','σάρκινος','σεβαστός','σεμνός','σηρικός','σιδήρεος','σιρικός','σιτευτός','σιτιστός','σκοτεινός','σμαράγδινος','σός','σοφός','στενός','Στοϊκός','στυγητός','Στωϊκός','συνεκλεκτός','συνετός','συστατικός','σωματικός','τακτός','ταπεινός','ταχινός','τεσσαρεσκαιδέκατος','τέταρτος','τετρακόσιοι','τετραπλόος','τιμιώτατος','τομός','τρίτος','τρίχινος','τυφλός','τυφωνικός','ὑακίνθινος','ὑάλινος','ὑδρωπικός','ὑφαντός','ὑψηλός','φαῦλος','φθαρτός','φθινοπωρινός','φίλος','φυσικός','φωτεινός','χαλεπός','χοϊκός','χρήσιμος','χρηστός','χωλός','ψυχικός']:
        return [adjective,
         adjective[:-2]+'υ',
         adjective[:-4]+'ῳ',
         adjective[:-2]+'ν',
         adjective[:-4]+'ε',
         adjective[:-2]+'ι',
         adjective[:-4]+'ων',
         adjective[:-2]+'ις',
         adjective[:-2]+'υς',
         adjective[:-4]+'η',
         adjective[:-4]+'ης',
         adjective[:-4]+'ῃ',
         adjective[:-4]+'ην',
         adjective[:-4]+'η',
         adjective[:-4]+'αι',
         adjective[:-4]+'ων',
         adjective[:-4]+'αις',
         adjective[:-4]+'ας',
         adjective[:-2]+'ν',
         adjective[:-2]+'υ',
         adjective[:-4]+'ῳ',
         adjective[:-2]+'ν',
         adjective[:-2]+'ν',
         adjective[:-4]+'α',
         adjective[:-4]+'ων',
         adjective[:-2]+'ις',
         adjective[:-4]+'α']
    elif adjective in ['Ἰτουραῖος']:
        return [adjective,
         adjective[:-2]+'υ',
         adjective[:-5]+'ῳ',
         adjective[:-2]+'ν',
         adjective[:-5]+'ε',
         adjective[:-2]+'ι',
         adjective[:-5]+'ων',
         adjective[:-2]+'ις',
         adjective[:-2]+'υς',
         adjective[:-5]+'α',
         adjective[:-5]+'ας',
         adjective[:-5]+'ᾳ',
         adjective[:-5]+'αν',
         adjective[:-5]+'α',
         adjective[:-5]+'αι',
         adjective[:-5]+'ων',
         adjective[:-5]+'αις',
         adjective[:-5]+'ας',
         adjective[:-2]+'ν',
         adjective[:-2]+'υ',
         adjective[:-5]+'ῳ',
         adjective[:-2]+'ν',
         adjective[:-2]+'ν',
         adjective[:-5]+'α',
         adjective[:-5]+'ων',
         adjective[:-2]+'ις',
         adjective[:-5]+'α']
    else:
        return [adjective,
         adjective[:-2]+'υ',
         adjective[:-4]+'ῳ',
         adjective[:-2]+'ν',
         adjective,
         adjective[:-2]+'ι',
         adjective[:-4]+'ων',
         adjective[:-2]+'ις',
         adjective[:-2]+'υς',
         adjective[:-4]+'η',
         adjective[:-4]+'ης',
         adjective[:-4]+'ῃ',
         adjective[:-4]+'ην',
         adjective[:-4]+'η',
         adjective[:-4]+'αι',
         adjective[:-4]+'ων',
         adjective[:-4]+'αις',
         adjective[:-4]+'ας',
         adjective[:-2],
         adjective[:-2]+'υ',
         adjective[:-4]+'ῳ',
         adjective[:-2]+'ν',
         adjective[:-2],
         adjective[:-4]+'α',
         adjective[:-4]+'ων',
         adjective[:-2]+'ις',
         adjective[:-4]+'α']

def a1b(adjective):
    '''a1b - Contracted Stems (3-1-3).
    
    Keyword arguments:
    adjective -- Nominative, masculine, singular root of the adjective
    '''
    if adjective.endswith('ῦς'):
        return [adjective,
             adjective[:-2],
             adjective[:-7]+'ῳ',
             adjective[:-2]+'ν',
             adjective,
             adjective[:-5]+'ι',
             adjective[:-7]+'ων',
             adjective[:-5]+'ις',
             adjective,
             adjective[:-7]+'η',
             adjective[:-7]+'ης',
             adjective[:-7]+'ῃ',
             adjective[:-7]+'ην',
             adjective[:-7]+'η',
             adjective[:-7]+'αι',
             adjective[:-7]+'ων',
             adjective[:-7]+'αις',
             adjective[:-7]+'ας',
             adjective[:-2]+'ν',
             adjective[:-2],
             adjective[:-7]+'ῳ',
             adjective[:-2]+'ν',
             adjective[:-2]+'ν',
             adjective[:-7]+'α',
             adjective[:-7]+'ων',
             adjective[:-5]+'ις',
             adjective[:-7]+'α']
    else:
        return [adjective,
             adjective[:-2],
             adjective[:-6]+'ῳ',
             adjective[:-2]+'ν',
             adjective,
             adjective[:-4]+'ι',
             adjective[:-6]+'ων',
             adjective[:-4]+'ις',
             adjective,
             adjective[:-6]+'η',
             adjective[:-6]+'ης',
             adjective[:-6]+'ῃ',
             adjective[:-6]+'ην',
             adjective[:-6]+'η',
             adjective[:-6]+'αι',
             adjective[:-6]+'ων',
             adjective[:-6]+'αις',
             adjective[:-6]+'ας',
             adjective[:-2]+'ν',
             adjective[:-2],
             adjective[:-6]+'ῳ',
             adjective[:-2]+'ν',
             adjective[:-2]+'ν',
             adjective[:-6]+'α',
             adjective[:-6]+'ων',
             adjective[:-4]+'ις',
             adjective[:-6]+'α']
    
def a2a(adjective):
    '''a2a - Stems ending in ντ (3-1-3).
    
    Keyword arguments:
    adjective -- Nominative, masculine, singular root of the adjective
    '''
    if adjective == 'εἷς':
        return [adjective,
         'ἑνός',
         'ἑνί',
         'ἑνά',
         adjective,
         adjective,
         adjective,
         adjective,
         adjective,
         'μία',
         'μιᾶς',
         'μιᾷ',
         'μίαν',
         adjective,
         adjective,
         adjective,
         adjective,
         adjective,
         'ἕν',
         'ἑνός',
         'ἑνί',
         'ἕν',
         adjective,
         adjective,
         adjective,
         adjective,
         adjective]
    elif adjective == 'μέλας':
        return [adjective,
         'μέλανος',
         'μέλανι',
         'μέλανα',
         adjective,
         'μέλανες',
         'μελάνων',
         'μέλασιν',
         'μέλανας',
         'μέλαινα',
         'μελαίνης',
         'μελαίνῃ',
         'μέλαιναν',
         'μέλαινα',
         'μέλαιναι',
         'μελαινῶν',
         'μελαίναις',
         'μελαίνας',
         'μέλαν',
         'μέλανος',
         'μέλανι',
         'μέλαν',
         'μέλαν',
         'μέλανα',
         'μελάνων',
         'μέλασιν',
         'μέλανα']
    else:
        return [adjective,
         adjective[:-2]+'ντος',
         adjective[:-2]+'ντι',
         adjective[:-2]+'ντα',
         adjective,
         adjective[:-2]+'ντες',
         adjective[:-2]+'ντων',
         adjective[:-2]+'σιν',
         adjective[:-2]+'ντας',
         adjective[:-2]+'σα',
         adjective[:-2]+'σης',
         adjective[:-2]+'σῃ',
         adjective[:-2]+'σαν',
         adjective[:-2]+'σα',
         adjective[:-2]+'σαι',
         adjective[:-2]+'σων',
         adjective[:-2]+'σαις',
         adjective[:-2]+'σας',
         adjective[:-2]+'ν',
         adjective[:-2]+'ντος',
         adjective[:-2]+'ντι',
         adjective[:-2]+'ν',
         adjective[:-2]+'ν',
         adjective[:-2]+'ντα',
         adjective[:-2]+'ντων',
         adjective[:-2]+'σιν',
         adjective[:-2]+'ντα']
    
def a2b(adjective):
    '''a2b - Stems ending in digamma (3-1-3).
    
    Keyword arguments:
    adjective -- Nominative, masculine, singular root of the adjective
    '''
    return [adjective,
     adjective[:-4]+'εως',
     adjective[:-4]+'ει',
     adjective[:-2]+'ν',
     adjective,
     adjective[:-4]+'εις',
     adjective[:-4]+'εων',
     adjective[:-4]+'εσιν',
     adjective[:-4]+'εις',
     adjective[:-4]+'εια',
     adjective[:-4]+'ειας',
     adjective[:-4]+'ειᾳ',
     adjective[:-4]+'ειαν',
     adjective[:-4]+'εια',
     adjective[:-4]+'ειαι',
     adjective[:-4]+'ειων',
     adjective[:-4]+'ειαις',
     adjective[:-4]+'ειας',
     adjective[:-2],
     adjective[:-4]+'εως',
     adjective[:-4]+'ει',
     adjective[:-2],
     adjective[:-2],
     adjective[:-4]+'εα',
     adjective[:-4]+'εων',
     adjective[:-4]+'εσιν',
     adjective[:-4]+'εα']
    
def a3a(adjective):
    '''a3a - Stems consistently using two endings (2-2).
    
    Keyword arguments:
    adjective -- Nominative, masculine, singular root of the adjective
    '''
    return [adjective,
     adjective[:-2]+'υ',
     adjective[:-4]+'ῷ',
     adjective[:-2]+'ν',
     adjective[:-2]+'ε',
     adjective[:-2]+'ι',
     adjective[:-4]+'ων',
     adjective[:-2]+'ις',
     adjective[:-2]+'ιυς',
     adjective,
     adjective[:-2]+'υ',
     adjective[:-4]+'ῷ',
     adjective[:-2]+'ν',
     adjective[:-2]+'ε',
     adjective[:-2]+'ι',
     adjective[:-4]+'ων',
     adjective[:-2]+'ις',
     adjective[:-2]+'ιυς',
     adjective[:-2]+'ν',
     adjective[:-2]+'υ',
     adjective[:-4]+'ῷ',
     adjective[:-2]+'ν',
     adjective[:-2]+'ν',
     adjective[:-4]+'α',
     adjective[:-4]+'ων',
     adjective[:-2]+'ις',
     adjective[:-4]+'α']
    
def a3b(adjective):
    '''a3b - Stems alternating between two (2-2) and three (2-1-2)
    endings.
    
    Keyword arguments:
    adjective -- Nominative, masculine, singular root of the adjective
    '''
    if adjective in ['αἰώνιος','ἑδραῖος','κόσμιος','οἰκεῖος','παρόμοιος']:
        return [adjective,
         adjective[:-2]+'υ',
         adjective[:-4]+'ῷ',
         adjective[:-2]+'ν',
         adjective[:-2]+'ε',
         adjective[:-2]+'ι',
         adjective[:-4]+'ων',
         adjective[:-2]+'ις',
         adjective[:-2]+'ιυς',
         adjective[:-4]+'α',
         adjective[:-4]+'ας',
         adjective[:-4]+'ᾳ',
         adjective[:-4]+'αν',
         adjective[:-4]+'α',
         adjective[:-4]+'αι',
         adjective[:-4]+'ων',
         adjective[:-4]+'αις',
         adjective[:-4]+'ας',
         adjective[:-2]+'ν',
         adjective[:-2]+'υ',
         adjective[:-4]+'ῷ',
         adjective[:-2]+'ν',
         adjective[:-2]+'ν',
         adjective[:-4]+'α',
         adjective[:-4]+'ων',
         adjective[:-2]+'ις',
         adjective[:-4]+'α']
    else:
        return [adjective,
         adjective[:-2]+'υ',
         adjective[:-4]+'ῷ',
         adjective[:-2]+'ν',
         adjective[:-2]+'ε',
         adjective[:-2]+'ι',
         adjective[:-4]+'ων',
         adjective[:-2]+'ις',
         adjective[:-2]+'ιυς',
         adjective[:-4]+'η',
         adjective[:-4]+'ης',
         adjective[:-4]+'ῃ',
         adjective[:-4]+'ην',
         adjective[:-4]+'η',
         adjective[:-4]+'αι',
         adjective[:-4]+'ων',
         adjective[:-4]+'αις',
         adjective[:-4]+'ας',
         adjective[:-2]+'ν',
         adjective[:-2]+'υ',
         adjective[:-4]+'ῷ',
         adjective[:-2]+'ν',
         adjective[:-2]+'ν',
         adjective[:-4]+'α',
         adjective[:-4]+'ων',
         adjective[:-2]+'ις',
         adjective[:-4]+'α']
    
def a4a(adjective):
    '''a4a - Stems ending in ες (3-3).
    
    Keyword arguments:
    adjective -- Nominative, masculine, singular root of the adjective
    '''
    if adjective == 'τρεῖς':
        return [adjective,
         adjective,
         adjective,
         adjective,
         adjective,
         'τρεῖς',
         'τριῶν',
         'τρισίv',
         'τρεῖς',
         adjective,
         adjective,
         adjective,
         adjective,
         adjective,
         'τρεῖς',
         'τριῶν',
         'τρισίv',
         'τρεῖς',
         adjective,
         adjective,
         adjective,
         adjective,
         adjective,
         'τρία',
         'τριῶν',
         'τρισίv',
         'τρία']
    else:
        return [adjective,
         adjective[:-4]+'ους',
         adjective[:-4]+'ει',
         adjective[:-2],
         adjective,
         adjective[:-4]+'εις',
         adjective[:-4]+'ων',
         adjective[:-4]+'εσιν',
         adjective[:-4]+'εις',
         adjective,
         adjective[:-4]+'ους',
         adjective[:-4]+'ει',
         adjective[:-2],
         adjective,
         adjective[:-4]+'εις',
         adjective[:-4]+'ων',
         adjective[:-4]+'εσιν',
         adjective[:-4]+'εις',
         adjective[:-4]+'ες',
         adjective[:-4]+'ους',
         adjective[:-4]+'ει',
         adjective[:-4]+'ες',
         adjective[:-4]+'ες',
         adjective[:-2],
         adjective[:-4]+'ων',
         adjective[:-4]+'εσιν',
         adjective[:-2]]
    
def a4b(adjective):
    '''a4b - Stems ending in ν (3-3).
    
    Keyword arguments:
    adjective -- Nominative, masculine, singular root of the adjective
    '''
    if adjective in ['ἀνελεήμων','ἀσχήμων','ἄφρων','βελτίων','δεισιδαίμων','ἑκατον','ταπλασίων','ἐλάσσων','ἐλάττων','ἐλεήμων','ἐπιστήμων','ἑπταπλασίων','εὐσχήμων','ἥσσων','ἥττων','κρείσσων','κρείττων','μείζων','οἰκτίρμων','ὁμόφρων','πλείων','πολλαπλασίων','σώφρων','ταπεινόφρων','φιλόφρων','χείρων']:
        return [adjective,
         adjective[:-4]+'ονος',
         adjective[:-4]+'ονι',
         adjective[:-4]+'ονα',
         adjective,
         adjective[:-4]+'ονες',
         adjective,
         adjective[:-4]+'οσιν',
         adjective[:-4]+'ονας',
         adjective,
         adjective[:-4]+'ονος',
         adjective[:-4]+'ονι',
         adjective[:-4]+'ονα',
         adjective,
         adjective[:-4]+'ονες',
         adjective,
         adjective[:-4]+'οσιν',
         adjective[:-4]+'ονας',
         adjective[:-4]+'ον',
         adjective[:-4]+'ονος',
         adjective[:-4]+'ονι',
         adjective[:-4]+'ον',
         adjective,
         adjective[:-4]+'ονα',
         adjective,
         adjective[:-4]+'οσιν',
         adjective[:-4]+'ονα']
    else:
        return [adjective,
         adjective[:-2]+'νος',
         adjective[:-2]+'νι',
         adjective[:-2]+'να',
         adjective,
         adjective[:-2]+'νες',
         adjective[:-2]+'νων',
         adjective[:-2]+'σιν',
         adjective[:-2]+'νας',
         adjective,
         adjective[:-2]+'νος',
         adjective[:-2]+'νι',
         adjective[:-2]+'να',
         adjective,
         adjective[:-2]+'νες',
         adjective[:-2]+'νων',
         adjective[:-2]+'σιν',
         adjective[:-2]+'νας',
         adjective[:-2],
         adjective[:-2]+'νος',
         adjective[:-2]+'νι',
         adjective[:-2],
         adjective[:-2],
         adjective[:-2]+'να',
         adjective[:-2]+'νων',
         adjective[:-2]+'σιν',
         adjective[:-2]+'να']
    
def a4c(adjective):
    '''a4c - Miscellaneous stems (3-3).
    
    Keyword arguments:
    adjective -- Nominative, masculine, singular root of the adjective
    '''
    return [adjective,
     adjective[:-4]+'ενος',
     adjective[:-4]+'ενι',
     adjective[:-4]+'ενα',
     adjective,
     adjective[:-4]+'ες',
     adjective[:-4]+'ων',
     adjective[:-4]+'σιν',
     adjective[:-4]+'ας',
     adjective,
     adjective[:-4]+'ενος',
     adjective[:-4]+'ενι',
     adjective[:-4]+'ενα',
     adjective,
     adjective[:-4]+'ες',
     adjective[:-4]+'ων',
     adjective[:-4]+'σιν',
     adjective[:-4]+'ας',
     adjective[:-4]+'εν',
     adjective[:-4]+'ενος',
     adjective[:-4]+'ενι',
     adjective[:-4]+'εν',
     adjective[:-4],
     adjective[:-4]+'α',
     adjective[:-4]+'ων',
     adjective[:-4]+'σιν',
     adjective[:-4]+'α']
    
def a5a(adjective):
    '''a5a - Irregular stems.
    
    Keyword arguments:
    adjective -- Nominative, masculine, singular root of the adjective
    '''
    return [adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective]
    
def a5b(adjective):
    '''a5b - Indeclinable stems.
    
    Keyword arguments:
    adjective -- Nominative, masculine, singular root of the adjective
    '''
    return [adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective,
     adjective]
