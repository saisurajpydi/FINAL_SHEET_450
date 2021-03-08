# Find four elements that sum to a given value
def findFourElements(A, n, X): 
	for i in range(0,n-3): 
		for j in range(i+1,n-2): 
			for k in range(j+1,n-1): 
				for l in range(k+1,n): 
					
					if A[i] + A[j] + A[k] + A[l] == X: 
						print ( A[i], A[j], A[k], A[l])

A = [10, 2, 3, 4, 5, 9, 7, 8] 
n = len(A) 
X = 23
findFourElements (A, n, X) 
