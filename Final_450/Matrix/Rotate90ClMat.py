"""
Given a square matrix, turn it by 90 degrees in clockwise direction without using any extra space.
"""
def rotateC(A):
    row = len(A)
    col = len(A[0])
    temp = 0
    # transpose the matrix
    for i in range(row):
        for j in range(i,col):
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp
    # reversing each row in the matrix
    for i in range(row):
        A[i].reverse()
    return A    



A = [[1, 2, 3, 4],
     [5, 6, 7, 8], 
     [9, 10, 11, 12], 
     [13, 14, 15, 16]]
A = rotateC(A)
print(A)