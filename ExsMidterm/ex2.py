def prune(s1, s2):
    while s1[0] == '-' and s2[0] == '-':
        s1, s2 = s1[1:], s2[1:]
    while s1[-1] == '-' and s2[-1] == '-':
        s1, s2 = s1[:-1], s2[:-1]
    return s1, s2
    

def align_score(s1, s2, Msubs):
    
    # --TCA  -TCA  TCA  TCA  TCA-  TCA--
    # GA---  GA--  GA-  -GA  --GA  ---GA
    
    L1 = len(s1)
    L2 = len(s2)
    
    N = L1 + L2
    aligns = []
    scores = []
    for n in range(N):
        s1_l = L2 * '-' + s1 + (L2 - 1) * '-'
        s2_l = n * '-' + s2 + (L2 + L1 - 1 - n) * '-'
        
        s1_s, s2_s = prune(s1_l, s2_l)
        aligns.append((s1_s, s2_s))
        
        L = len(s1_s)
        score = 0
        for l in range(L):
            if s1_s[l] != '-' and s2_s[l] != '-':
                score += Msubs[s1_s[l] + s2_s[l]]
        scores.append(score)
        
        # Find maximum
        nmax = 0
        alignmax = aligns[0]
        scoremax = scores[0]
        for n in range(n):
            if scores[n] > scoremax:
                nmax = n
                alignmax = aligns[n]
                scoremax = scores[n]
    
    
    return aligns, scores, nmax, alignmax, scoremax


    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



seq1 = 'TCA'
seq2 = 'GA'
score_matrix = {
    'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
    'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
    'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
    'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2,
    }
aligns, scores, nmax, alignmax, scoremax = align_score(seq1, seq2, score_matrix)