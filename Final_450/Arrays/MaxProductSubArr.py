"""
Given an array Arr that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.
"""
"""
arr = []
n = int(input("Enter size of array : "))
print("enter ",n," values in the array ")
for i in range(n):
    arr.append(int(input()))
maxi = arr[0]
for i in range(n):
    val = arr[i]
    for j in range(i+1,n):
        val *= arr[j]
        maxi = max(maxi,val)
print("the largest product sub array is : ",maxi )
"""
# method 2
arr = []
n = int(input("Enter size of array : "))
print("enter ",n," values in the array ")
for i in range(n):
    arr.append(int(input()))

def maxProSubArr( arr,n):
    cur_max = arr[0]
    prev_max = arr[0]
    prev_min = arr[0]
    ans = arr[0]

    for i in range(1,n):
        cur_max = max(prev_max * arr[i], prev_min * arr[i], arr[i])
        cur_min = min(prev_max * arr[i], prev_min * arr[i], arr[i])
        ans = max( ans , cur_max )
        prev_max = cur_max
        prev_min = cur_min
    return ans

print("the max product of the sub array is : ",maxProSubArr(arr,n))