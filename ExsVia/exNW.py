# Implementation of the Needleman-Wunsch algorithm.



def max_argmax_of_list(l):
    iM, M = 0, l[0]
    for i in range(1, len(l)):
        if l[i] > M:
            iM, M = i, l[i]
    return M, iM



def NW_alg(s1, s2, Msubs, d):
    
    L1, L2 = len(s1), len(s2)
    
    T, tb = [], []
    for i in range(1 + L2):
        T.append([0] * (1 + L1))
        tb.append([0] * (1 + L1))
    
    for j in range(1, 1 + L1):
        T[0][j], tb[0][j] = - d * j, 2
    for i in range(1, 1 + L2):
        T[i][0], tb[i][0] = - d * i, 1
    
    
    for i in range(1, 1 + L2):
        for j in range(1, 1 + L1):
            M, iM = max_argmax_of_list([
                T[i - 1][j - 1] + Msubs[s1[j - 1] + s2[i - 1]],
                T[i - 1][j] - d,
                T[i][j - 1] - d,
                ])
            T[i][j], tb[i][j] = M, iM
    
    
    s1a, s2a = '', ''
    i, j = L2, L1
    while i != 0 or j != 0: # WHY DOES IT WORK WITH or INTEAD OF and???
        iM = tb[i][j]
        if iM == 0:
            s1a += s1[-1 + j]
            s2a += s2[-1 + i]
            i -= 1
            j -= 1
        elif iM == 1:
            s1a += '-'
            s2a += s2[-1 + i]
            i -= 1
        elif iM == 2:
            s1a += s1[-1 + j]
            s2a += '-'
            j -= 1
    s1a, s2a = s1a[::-1], s2a[::-1]
    
    
    return T, T[L2][L1], tb, s1a + '\n' + s2a



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



Msubs = {
    'AA': +2, 'AT': -1, 'AC': -1, 'AG': -1,
    'TA': -1, 'TT': +2, 'TC': -1, 'TG': -1,
    'CA': -1, 'CT': -1, 'CC': +2, 'CG': -1,
    'GA': -1, 'GT': -1, 'GC': -1, 'GG': +2,
    }
d = 2

seq1 = 'GAATTC'
seq2 = 'GATTA'
T, s, tb, seqseq = NW_alg(seq1, seq2, Msubs, d)

print('\n')
for i in range(1 + len(seq2)):
    print(T[i])
print('\n')
print(s)
print('\n')
for i in range(1 + len(seq2)):
    print(tb[i])
print('\n')
print(seqseq)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



BLOSUM50 = {}
filename = 'blosum_Durbin.txt'
with open(filename, 'r') as infile:
    A = infile.readline().split()
    L = len(A)
    for line in infile:
        for i in range(L):
            BLOSUM50[A[i] + line.split()[0]] = int(line.split()[1 + i])
            
Msubs, d = BLOSUM50, 8
seq1 = 'HEAGAWGHEE'
seq2 = 'PAWHEAE'
T, s, tb, seqseq = NW_alg(seq1, seq2, BLOSUM50, d)

print('\n')
for i in range(1 + len(seq2)):
    print(T[i])
print('\n')
print(s)
print('\n')
for i in range(1 + len(seq2)):
    print(tb[i])
print('\n')
print(seqseq)