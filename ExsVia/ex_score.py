from math import log2


def score(s1, s2, A={'A', 'T', 'C', 'G'}, psc=1, K=1):
    
    Lab = len(A)
    psc = 1
    
    q = {}
    p = {}
    for x in A:
        q[x] = psc
        for y in A:
            p[x + y] = psc

    for x in s1 + s2:
        q[x] += 1
    Ls = len(s1)
    for x in A:
        q[x] /= Lab + 2 * Ls
        
    for i in range(Ls):
        x, y = s1[i], s2[i]
        p[x + y] += 1
        p[y + x] += x != y
    for xy in p:
        p[xy] /= Lab * (Lab + 1) / 2 + Ls
    
    S = {}
    for x in A:
        S[x] = {}
        for y in A:
            S[x][y] = round(10 * (log2(p[xy]) - (log2(q[x]) + log2(q[y]))))
    
    score = 0
    for i in range(Ls):
        score += S[s1[i]][s2[i]]
    
    return score, q, p, S


A = {'A', 'T', 'C', 'G'}

seq1 = 'ACAGGTGGACCT'
seq2 = 'ACTGGTCGACTT'
print('\n', score(seq1, seq2, A, K=10), '\n')

seq1 = 'CTATATGG'
seq2 = 'CCGGATCG'
print('\n', score(seq1, seq2, A, K=10), '\n')
