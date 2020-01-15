from math import sqrt

filename1 = 'model8_1.pdb'
filename2 = 'model8_2.pdb'


infile1 = open(filename1, 'r')
infile2 = open(filename2, 'r')

L1 = []
for line in infile1:
    if line[:4] == 'ATOM' and line[13:15] == 'CA':
        l = line.split()[6:9] # [6:9] for Model 1, [5:8] for Model 2
        L1.append([float(l[0]), float(l[1]), float(l[2])])

L2 = []
for line in infile2:
    if line[:4] == 'ATOM' and line[13:15] == 'CA':
        l = line.split()[5:8] # [6:9] for Model 1, [5:8] for Model 2
        L2.append([float(l[0]), float(l[1]), float(l[2])])

# Numpy
import numpy as np
X = np.array(L1)
Y = np.array(L2)
RMSD = np.sqrt(np.square(X - Y).sum(1).mean())
print('RMSD = %.3fnm' % RMSD)

# On list
n = len(L1)
sum = 0
for i in range(n): # -2 !
    Di = (L1[i][0] - L2[i][0])**2 + (L1[i][1] - L2[i][1])**2 + (L1[i][2] - L2[i][2])**2
    sum += Di
rmsd = sqrt(sum / n)
print('rmsd = %.3fnm' % rmsd)