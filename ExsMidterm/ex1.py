def my_prod(A, B):
    
    N = len(A)
    
    AB = []
    for i in range(N):
        AB.append([])
        for j in range(N):
            AB[i].append(0)
            for k in range(N):
                AB[i][j] += A[i][k] * B[k][j]
    
    return AB


    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



A = [
     [2, 4],
     [3, 1]
     ]
B = [
     [2, 1],
     [1, 3]
     ]
AB = my_prod(A, B)
print(AB)