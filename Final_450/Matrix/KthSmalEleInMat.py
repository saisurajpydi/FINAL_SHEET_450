"""
Given a N x N matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.
"""
def kthSmallest(mat, n, k): 
    # Your code goes here
    temp = []
    for i in range(n):
        for j in range(n):
            temp.append(mat[i][j])
    temp.sort()
    return temp[k-1]