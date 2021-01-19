# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
arr = []
n = int(input("enter the size of the array : "))
print("enter only 0's , 1's , 2's ")
for i in range(n):
    arr.append(int(input()))
l = 0
m = 0
h = n - 1

while( m <= h):
    if(arr[m] == 0):
        arr[l],arr[m] = arr[m],arr[l]
        l = l + 1
        m = m + 1
    elif(arr[m] == 1):
        m = m + 1
    elif(arr[m] == 2):
        arr[m],arr[h] = arr[h],arr[m]
        h = h - 1
print(arr)