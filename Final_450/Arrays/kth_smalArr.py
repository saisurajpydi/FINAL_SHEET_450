"""
arr = []
n = int(input("enter the size of the array : "))
for i in range(n):
    arr.append(int(input()))
def ksmall(arr,n,k):
    mi = arr[0]
    while(k != 0):

        k = k - 1
"""

m = int(input("enter the number of testcases : "))
for i in range(m):
    arr = []
    n = int(input("enter the size of the array : "))
    k = int(input("enter the Kth value : "))
    print("enter the array elements")
    for j in range(n):
        arr.append(int(input()))
    arr.sort()
    print("the kth smallest element is : ", arr[k-1])
    arr.clear()
