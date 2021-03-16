# Calculate square of a number without using *, / and pow()
"""
Given an integer n, calculate the square of a number without using *, / and pow(). 

Examples : 

Input: n = 5
Output: 25

Input: 7
Output: 49

Input: n = 12
Output: 144
"""

"""
def square(n):

	# Base case
	if (n == 0):
		return 0

	# Handle negative number
	if (n < 0):
		n = -n

	# Get floor(n/2) using
	# right shift
	x = n >> 1

	# If n is odd
	if (n & 1):
		return ((square(x) << 2)
				+ (x << 2) + 1)

	# If n is even
	else:
		return (square(x) << 2)


# Driver Code
for n in range(1, 6):
	print("n = ", n, " n^2 = ",
		square(n))
"""
a = 10 
n = 0
b = a
for i in range(1,a):
    a += b    
print(a)