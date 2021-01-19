"""
Given two arrays: arr1[0..m-1] of size m and arr2[0..n-1] of size n. Task is to check whether arr2[] is a subset of arr1[] or not. Both the arrays can be both unsorted or sorted. It may be assumed that elements in both array are distinct.
"""
arr1 = [1,2,3,4,5,6]
arr2 = [4,5,6]
n1 = len(arr1)
n2 = len(arr2)
count = 0
for i in arr2:
    for j in arr1:
        if(i == j):
            count +=1
if(count == n2):
    print("yes")
else:
    print("no")
