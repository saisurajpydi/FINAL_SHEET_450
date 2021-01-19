arr = [2,1,7,9,5]
n = len(arr)
k = 5
def minSwap(arr,n,k):
    good = 0
    bad = 0
    for i in range(n):
        if( arr[i] <= k):
            good += 1
    for i in range(good):
        if(arr[i] > k):
            bad += 1
    ans = bad
    j = good

    for i in range(n):
        if ( j == n):
            break
        if( arr[i] > k):
            bad -= 1
        if( arr[j] > k):
            bad += 1
        
        ans = min(ans, bad)
        j += 1
    return ans
print("the minimum no. of swaps are ", end = " ")
print(minSwap(arr,n,k))
