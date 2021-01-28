"""
Given an NxN matrix Mat. Sort all elements of the matrix.
"""
class Solution:
    def sortedMatrix(self,N,Mat):
        #code here
        count = 0
        temp = []
        for i in range(N):
            for j in range(N):
                temp.append(Mat[i][j])
        temp.sort()
        if(count < N*N):
            for i in range(N):
                for j in range(N):
                    Mat[i][j] = temp[count]
                    count += 1
        return Mat