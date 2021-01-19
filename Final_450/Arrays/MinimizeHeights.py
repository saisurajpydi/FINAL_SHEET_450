"""
 Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.
"""
arr = []
k = int(input("enter the k value : "))
n = int(input("enter the size of the array  : "))
for i in range(n):
    arr.append(int(input()))
for i in range (n):
    if(arr[i] - k < 0):
        arr[i] = arr[i]+k
    else:
        arr[i] = arr[i]-k
mi = min(arr)
ma = max(arr)
print(arr)
print("the reault is : " , ma-mi)
