arr = [10, 22, 5, 75, 65, 80]
n = len(arr)

def maxProf(arr, n ):
    profit = 0
    for i in range( 1, n):
        sub = arr[i] - arr[i-1]
        if(sub > 0):
            profit += sub
    print("the profit is :",profit)
maxProf(arr, n )    