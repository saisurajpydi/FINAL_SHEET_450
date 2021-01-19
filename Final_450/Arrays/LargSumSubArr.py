arr = [-1,-2,4,5,-6]
n = len(arr)
sum = 0 
maxi = 0
for i in range(n):
    sum += arr[i]
    if(sum < arr[i]):
        sum = arr[i]
    if(sum > maxi ):
        maxi = sum
print("result : ",maxi)