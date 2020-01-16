import sys



def read_matrix(filename):
    Msubs = {}
    A = 'ARNDCQEGHILKMFPSTWYV'
    Lab = len(A)
    with open(filename) as infile:
        infile.readline()
        for i in range(Lab):
            line = infile.readline()
            for j in range(1 + i):
                Msubs[A[i] + A[j]] = int(float(line.split()[j]))
                Msubs[A[j] + A[i]] = int(float(line.split()[j]))
    return Msubs



def read_aligns(filename):
    seq_pairs = []
    Np = 3
    with open(filename, 'r') as infile:
        for n in range(Np):
            infile.readline()
            s1 = infile.readline().rstrip()
            infile.readline()
            s2 = infile.readline().rstrip()
            seq_pairs.append((s1, s2))
    return seq_pairs



def score_align(sp, Msubs, d):  # sp = "sequence pair" = 2-tple (s1, s2)
    L = len(sp[0])
    score = 0
    for i in range(L):
        if sp[0][i] == '-' or sp[1][i] == '-':
            score -= d
        else:
            score += Msubs[sp[0][i] + sp[1][i]]
    return score



def score_align_affine(sp, Msubs, d, e): # sp = "sequence pair" = 2-tple (s1, s2)
    L = len(sp[0])
    score = 0
    i = 0
    while i < L:
        g = 0
        if sp[0][i] == '-' or sp[1][i] == '-':
            c = sp[0][i] == '-' # c = index of the gapped seq
            g = 1
            while sp[c][i + g] == '-':
                g += 1
            score += - d - (g - 1) * e
        else:
            score += Msubs[sp[0][i] + sp[1][i]]
        i += 1 + g

    return score



def main():
    
    PAM250 = read_matrix(sys.argv[1])
    BLOSUM62 = read_matrix(sys.argv[2])
    d = 2
    # e = 0.5
    
    seq_pairs = read_aligns(sys.argv[3])

    N = 3
    print('\n')
    for n in range(N):
        print('Alignment %d: ' % (1 + n))
        print('PAM250:\t\t%d' % score_align(seq_pairs[n], PAM250, d))
        print('BLOSUM62:\t%d' % score_align(seq_pairs[n], BLOSUM62, d))
        # print('PAM250:\t\t%d' % score_align_affine(seq_pairs[n], PAM250, d, e))
        # print('BLOSUM62:\t%d' % score_align_affine(seq_pairs[n], BLOSUM62, d, e))
        print('\n')



if __name__ == '__main__':
    main()