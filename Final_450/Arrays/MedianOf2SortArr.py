ar1 = [-5, 3, 6, 12, 15]
ar2 = [-12, -10, -6, -3, 4, 10]
ar3 = ar1 + ar2
ar3.sort()
n = len(ar3)
def thisMethod(arr,n):
    print( " the median is ", end = " ")
    if( n % 2 == 0):
        x = n // 2
        median = (x + x + 1 ) // 2
        print[median-1]
    else:
        x = n // 2
        print(arr[x])
thisMethod(ar3,n)