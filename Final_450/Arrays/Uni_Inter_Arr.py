arr1 = [1,3,5,6,7]
arr2 = [2,3,4,5,6]
# intersection of arrays
n = len(arr1)
m = len(arr2)
arr3 = []
for i in range(m):
    for j in range(n):
        if(arr2[i] == arr1[j]):
            arr3.append(arr2[i])
print("the intersection of arrays is : ",arr3)
# union of arrays 
arr4 = []
for i in range(n):
    arr4.append(arr1[i])
for i in range(m):
    arr4.append(arr2[i])
print("the union of arrays : ",arr4)
