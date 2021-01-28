"""
Given an n x n matrix mat[n][n] of integers, find the maximum value of mat(c, d) – mat(a, b) over all choices of indexes such that both c > a and d > b.
"""
def findMaxVal(mat):
    row = len(mat)
    col = len(mat[0])
    maxVal = 0
    for a in range(row-1):
        for b in range(col-1):
            for c in range(a+1,row):
                for d in range(b+1,col):
                    if(maxVal < mat[c][d] - mat[a][b]):
                        maxVal = mat[c][d] - mat[a][b]
    return maxVal

mat = [[ 1, 2, -1, -4, -20 ], 
       [ -8, -3, 4, 2, 1 ], 
       [ 3, 8, 6, 1, 3 ], 
       [ -4, -1, 1, 7, -6 ], 
       [ 0, -4, 10, -5, 1 ]]
print(findMaxVal(mat))