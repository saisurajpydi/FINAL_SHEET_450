"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.
"""
# method 1 (naive)

arr = []
n = int(input("enter the size of the array  : "))
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(n-1):
    if(arr[i] == arr[i+1]):
        print("the duplicate is : ",arr[i])
        break
"""
# method 2  (using pointers)
arr = []
n = int(input("enter the size of the array  : "))
for i in range(n):
    arr.append(int(input()))
#count = 0
slow = 0
fast = 1
while (1):
    slow += 1
    fast += 2
    if(arr[slow] == arr[fast]):
        print("the duplicate is : ",arr[slow])
        break
"""

