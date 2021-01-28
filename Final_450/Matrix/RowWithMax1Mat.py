"""
Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.
"""

class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		result = 0
		count = 0
		index = 0
        for i in range(n):
            for j in range(m):
                if(arr[i][j]==1):
                    count += 1
                    if(count > result):
                        result = count
                        index = i
            count = 0
            i += 1
        if(result == 0):
            return -1
        else:
            return index