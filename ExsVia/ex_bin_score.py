def bin_score(s1, s2, malus=True):
    score = 0
    for c in range(len(s1)):
        
        score += - malus + (1 + malus) * (s1[c] == s2[c])
    return score


seq1 = 'ALASVLIRLITRLYP'
seq2 = 'ASAVHLNRLITRLYP'
print(bin_score(seq1, seq2, malus=True))
print(bin_score(seq1, seq2, malus=False))