"""
Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum
"""
"""
arr = []
n = int(input("enter the size of the array"))
print("enter the elements of the array  ")
for i in range(n):
    arr.append(int(input()))
neg = 0
plu = 0
sum = 0
for i in range(n):
    if(arr[i] == 0):
        print("yes")
        break
    if(arr[i] > 0):
        plu += arr[i]
    elif(arr[i] < 0):
        neg += arr[i]
if(neg < plu):
    for i in range(n):
        if(arr[i] > 0):
            sum += arr[i]
            if( neg == sum):
                print("yes")
            else:
                print("no")
elif(neg > plu):
    for i in range(n):
        if(arr[i] < 0):
            sum += arr[i]
            if(plu == sum):
                print("yes")
            else:
                print("no")
elif(neg == plu):
    print("yes")
"""
def subArrayExists(arr,n): 
    # traverse through array  
    # and store prefix sums  
    n_sum = 0
    lis = []
  
    for i in range(n): 
        n_sum += arr[i] 
  
        # If prefix sum is 0 or  
        # it is already present  
        if n_sum == 0 or n_sum in lis: 
            return True
        lis.append(n_sum) 
  
    return False
  
# Driver code 
arr = [4,2,-3,1,6]     
n = len(arr) 
if subArrayExists(arr, n) == True: 
    print("Found a sunbarray with 0 sum") 
else: 
    print("No Such sub array exits!") 