def PalinArray(arr ,n):
    # Code here
    i = 0 
    j = n - 1 
    while( i < j):
        if ( i == j):
            j -= 1
            i += 1
        else:
            return 0
    return 1
arr = [1,2,3,4,3,2,1]
n = len(arr)
print(PalinArray(arr ,n))