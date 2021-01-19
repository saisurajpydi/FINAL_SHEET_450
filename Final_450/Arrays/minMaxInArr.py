"""
arr = []
n = int(input("enter the size of the array : "))
for i in range(n):
    arr.append(int(input()))
arr.sort()
print(arr)
#size = len(arr)
print("max elemnt is ", arr[len(arr)-1])
print("min elemnt is ", arr[0])
"""
arr = []
n = int(input("enter the size of the array : "))
for i in range(n):
    arr.append(int(input()))
mi=arr[0]
for i in range(n):
    if(mi>arr[i]):
        mi=arr[i]
ma=arr[0]
for i in range(n):
    if(ma<arr[i]):
        ma=arr[i]
print("the max is : ", ma)
print("the min is : ",mi)