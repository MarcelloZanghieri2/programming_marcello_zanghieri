import sys


def import_PAM250():

    import re
    PAM250 = {}
    filename = 'PAM250.txt'
    with open(filename, 'r') as infile:
        line = infile.readline()
        match = re.search(r'rows = (.{20})', infile.readline())
        A = list(match.group(1))
        Lab = len(A)
        for i in range(Lab):
            line = infile.readline()
            for j in range(len(line.split())):
                PAM250[A[i] + A[j]] = int(float(line.split()[j]))
    for c1 in A:
        for c2 in A:
            if c1 + c2 not in PAM250:
                PAM250[c1 + c2] = PAM250[c2 + c1]
    
    return PAM250


def import_BLOSUM62():
    
    import re
    BLOSUM62 = {}
    filename = 'BLOSUM62.txt'
    with open(filename, 'r') as infile:
        line = infile.readline()
        match = re.search(r'rows = (.{20})', infile.readline())
        A = list(match.group(1))
        Lab = len(A)
        for i in range(Lab):
            line = infile.readline()
            for j in range(len(line.split())):
                BLOSUM62[A[i] + A[j]] = int(float(line.split()[j]))
    for c1 in A:
        for c2 in A:
            if c1 + c2 not in BLOSUM62:
                BLOSUM62[c1 + c2] = BLOSUM62[c2 + c1]
    
    return BLOSUM62


def score_one_align(s1, s2, Msubs, d):
    
    L = len(s1)
    score = 0
    for i in range(L):
        if s1[i] == '-' or s2[i] == '-':
            score += - d
        else:
            score += Msubs[s1[i] + s2[i]]
    
    return score


def main():

    # seq1 = 'ALSKLASPALSAKDLDSPAL'
    # seq2 = 'ALSKIADSLAPIKDLSPASL'
    # print((score_one_align(seq1, seq2, PAM250, -1),
    #        score_one_align(seq1, seq2, BLOSUM62, -1)))
    
    # seq1 = 'ALSKLA-SPALSAKDLDSPAL'
    # seq2 = 'ALSKIADSLAP-IKDLSPASL'
    # print((score_one_align(seq1, seq2, PAM250, -1),
    #        score_one_align(seq1, seq2, BLOSUM62, -1)))
    
    # seq1 = 'ALSKLASPALSAKDLDSPA-L'
    # seq2 = 'ALSKIADSLAPIKDLS-PASL'
    # print((score_one_align(seq1, seq2, PAM250, -1),
    #        score_one_align(seq1, seq2, BLOSUM62, -1)))
    
    # seq1 = 'ALSKLASPALSAKDLDSPA-LS'
    # seq2 = 'ALSKIADSLAPIKDLS-PASLT'
    # print((score_one_align(seq1, seq2, PAM250, -1),
    #        score_one_align(seq1, seq2, BLOSUM62, -1)))
    
    if sys.argv[1].upper() == 'PAM250':
        Msubs = import_PAM250()
    if sys.argv[1].upper() == 'BLOSUM62':
        Msubs = import_BLOSUM62()
    
    d = int(sys.argv[2])
    
    
    seq1 = 'ALSKLASPALSAKDLDSPAL'
    seq2 = 'ALSKIADSLAPIKDLSPASL'
    print(score_one_align(seq1, seq2, Msubs, d))
    
    seq1 = 'ALSKLA-SPALSAKDLDSPAL'
    seq2 = 'ALSKIADSLAP-IKDLSPASL'
    print(score_one_align(seq1, seq2, Msubs, d))
    
    seq1 = 'ALSKLASPALSAKDLDSPA-L'
    seq2 = 'ALSKIADSLAPIKDLS-PASL'
    print(score_one_align(seq1, seq2, Msubs, d))
    
    seq1 = 'ALSKLASPALSAKDLDSPA-LS'
    seq2 = 'ALSKIADSLAPIKDLS-PASLT'
    print(score_one_align(seq1, seq2, Msubs, d))


if __name__ == '__main__':
    main()
    