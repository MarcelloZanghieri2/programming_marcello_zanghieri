Msubs = {}
filename = 'ex_subs_matr.txt'
with open(filename, 'r') as infile:
    A = infile.readline().split()
    Lab = len(A)
    for line in infile:
        print(line)
        for i in range(Lab):
            Msubs[A[i] + line.split()[0]] = int(line.split()[1 + i])



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


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



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



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
            
            
            
            