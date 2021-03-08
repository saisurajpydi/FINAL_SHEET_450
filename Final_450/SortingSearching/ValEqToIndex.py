# Value equal to index value
"""
Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value.

Example 1:

Input: 
N = 5
Arr[] = {15, 2, 45, 12, 7}
Output: 2
Explanation: Only Arr[2] = 2 exists here.
Example 2:

Input: 
N = 1
Arr[] = {1}
Output: 1
Explanation: Here Arr[1] = 1 exists.
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
