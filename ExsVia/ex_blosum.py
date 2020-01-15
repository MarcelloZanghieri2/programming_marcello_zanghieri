BLOSUM50 = {}
filename = 'blosum.txt'
with open(filename, 'r') as infile:
    alphabet = infile.readline().split()
    Lab = len(alphabet)
    for line in infile:
        for i in range(Lab):
            BLOSUM50[alphabet[i] + line.split()[0]] = int(line.split()[1 + i])


def score(s1, s2, Msubs):
    score = 0
    Ls = len(s1)
    for i in range(Ls):
        score += Msubs[s1[i] + s2[i]]
    return score


seq1 = 'ALASVLIRLITRLYP'
seq2 = 'ASAVHLNRLITRLYP'
s = score(seq1, seq2, BLOSUM50)