# An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.
"""
arr = []
n = int(input("enter size of array : "))
for i in range(n):
    arr.append(int(input()))
i = 0
j = 0
while ( j <= n):
    if(arr[i] < 0 and arr[j] < 0):
        i = i + 1
        j = j + 1
    elif(arr[i] >= 0 and arr[j] >= 0 ):
        j = j + 1 
        arr[i],arr[j] = arr[j],arr[i]
        i = i + 1
print(arr)
"""    
def rearrange(arr, n ) :
    j = 0
    for i in range(0, n) :
        if (arr[i] < 0) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j = j + 1
    print(arr)
 
# Driver code
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)


    