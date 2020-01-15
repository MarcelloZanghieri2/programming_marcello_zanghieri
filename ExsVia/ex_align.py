

MsubsVia = { # Little matrix of the exercise by Via
    'AA':  2, 'AT': -1, 'AC': -1, 'AG':  0, 'A-': -2, 
    'TA': -1, 'TT':  2, 'TC':  0, 'TG': -1, 'T-': -2, 
    'CA': -1, 'CT':  0, 'CC':  2, 'CG': -1, 'C-': -2, 
    'GA':  0, 'GT': -1, 'GC': -1, 'GG':  2, 'G-': -2,
    '-A': -2, '-T': -2, '-C': -2, '-G': -2, '--': -2,
    }


def prune(s1, s2):
    while s1[0] == '-' and s2[0] == '-' :
        s1, s2 = s1[1:], s2[1:]    
    while s1[-1] == '-' and s2[-1] == '-' :
        s1, s2 = s1[:-1], s2[:-1]
    return s1, s2


def score_the_alignments(s1, s2, Msubs):
    
    L1 = len(s1)
    L2 = len(s2)
    Na = L1 + L2
    
    imax = -1
    s1pmax = ''
    s2pmax = ''
    scoremax = Na * (-2)
    
    s1p0 = L2 * '-' + s1 + (L2 - 1) * '-'
    for i in range(Na):
        s2p0 = i * '-' + s2 + (Na - 1 - i) * '-'
        s1p, s2p = prune(s1p0, s2p0)

        score = 0
        for i in range(len(s1p)):
            score += Msubs[s1p[i] + s2p[i]]
        print('\n%s\n%s\n%d\n' % (s1p, s2p, score))
        
        if score > scoremax:
            imax = i
            s1pmax = s1p
            s2pmax = s2p
            scoremax = score
        
    print('\n____________\n%s\n%s\n%d' % (s1pmax, s2pmax, scoremax))
        
    return imax, s1pmax, s2pmax, score
  


seq1 = 'TCA'
seq2 = 'GA'
scores = score_the_alignments(seq1, seq2, MsubsVia)