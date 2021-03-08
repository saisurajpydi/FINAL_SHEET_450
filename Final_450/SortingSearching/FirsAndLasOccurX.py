#First and last occurrences of X 
"""
Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

Note: If the number x is not found in the array just print '-1'.

Input:
The first line consists of an integer T i.e number of test cases. The first line of each test case contains two integers n and x. The second line contains n spaced integers.

Output:
Print index of the first and last occurrences of the number x with a space in between.

Constraints: 
1<=T<=100
1<=n,a[i]<=1000

Example:
Input:
2
9 5
1 3 5 5 5 5 67 123 125
9 7
1 3 5 5 5 5 7 123 125

Output:
2 5
6 6
"""
T = int(input())
result = []
for t in range(T):
    a = list(map(int,input().split()))
    n = a[0]
    x = a[1]
    arr = list(map(int,input().split()))
    first = -1
	last = -1
	for i in range(0, n) :
		if (x != arr[i]) :
			continue
		if (first == -1) :
			first = i
		last = i
	if(first == -1 and last == -1):
	    subresult = [-1]
	else:
        subresult = [first,last]
    result.append(subresult)
for i in result:
    if(len(i) == 2):
        print(i[0], i[1])
    else:
        print(i[0])
