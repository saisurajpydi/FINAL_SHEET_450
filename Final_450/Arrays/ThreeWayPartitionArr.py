def threeWayPartition(array, a, b):
    l = 0 
    r = len(array) - 1
    i = 0
    while ( i <= r):
        if(array[i] < a ):
            array[i],array[l] = array[l],array[i]
            l += 1
            i += 1
            
        elif(array[i] > b):
            array[i],array[r] = array[r],array[i] 
            r -= 1
        else:
            i += 1
    print(array)
array = [1,2,3]
a = 10
b = 20
threeWayPartition(array, a, b)

