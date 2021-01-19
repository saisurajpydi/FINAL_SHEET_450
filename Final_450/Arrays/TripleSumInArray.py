"""
Given an array and an integer K. Find if there's a triplet in the array which sums up to the given integer K. 

arr = [1 ,4 ,45 ,6 ,10 ,8]
n = len(arr)
k = int(input("enter the k value : "))
"""
n = int(input("enter the size of the array "))
k = int(input("enter the value "))
print("enter the",n,"elements of the array ")
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
def fu( arr, n , k):
    for i in range(n-2):
        l = i + 1
        r = n - 1
        while ( l < r ):
            if(arr[i] + arr[l] + arr[r] == k):
                return bool(1) 
            elif(arr[i] + arr[l] + arr[r] < k):
                l += 1
            else:
                r -= 1
    return bool(0)
print(fu(arr,n,k))