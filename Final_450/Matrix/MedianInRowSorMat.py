"""
Given a row wise sorted matrix of size RxC where R and C are always odd, find the median of the matrix.
"""

class Solution:
    def median(self, matrix, r, c):
    	#code here 
    	alist=[]
    	for i in range(r):
    	    for j in range(c):
    	        alist.append(matrix[i][j])
        alist.sort()
        n = int(len(alist) / 2)
        med = alist[n]
        return med