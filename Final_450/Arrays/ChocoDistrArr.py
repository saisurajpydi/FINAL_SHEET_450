"""
Given an array A of positive integers of size N, where each value represents number of chocolates in a packet. Each packet can have variable number of chocolates. There are M students, the task is to distribute chocolate packets such that :
1. Each student gets one packet.
2. The difference between the number of chocolates given to the students having packet with maximum chocolates and student having packet with minimum chocolates is minimum.
"""
#T = int(input("enter no. of test cases : "))
n = int(input("enter the size of array "))
arr = []
print('enter the array elements ')
for i in range(n):
    arr.append(int(input()))
m = int(input("enter the no. of students " ))
result = 1000 # any big value
arr.sort() 
print(arr)
for i in range(n-m):
    result = min(result , arr[i+m-1] - arr[i])
print(result)