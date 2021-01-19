#Cyclically rotate an array by one
arr = [ 1,2,3,4,5]
n=len(arr)
temp = arr[n-1]
arr2=[]
arr2.append(temp)
for i in range(n-1):
    arr2.append(arr[i])
print(arr2)