class Solution:
    arr = [1, 4, 45, 6, 0, 19]
    n = len(arr)
    x = int(input("enter the sum value : "))
    def __init__(self, arr, n, x):
        self.arr = arr
        self.n = n
        self.x = x
    def func(self):
        curSum = 0
        result = n + 1
        start = 0
        end = 0
        while (end < n):
            
            while ( curSum <= x and end < n):
                curSum += arr[end]
                end += 1
                
            while ( curSum > x and start < n ):
                if(end - start < result ):
                    result = end - start
                curSum -= arr[start]
                start += 1
        return result
   
    s = Solution(arr,n,x)
    print(s.func)
        


