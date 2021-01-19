class Solution:
    arr = [1, 4, 45, 6, 0, 19]
    n = len(arr)
    x = int(input("enter the sum value : "))
    def __init__(self, arr, n, x):
        self.arr = arr
        self.n = n
        self.x = x
    
        curSum = 0
        result = self.n + 1
        start = 0
        end = 0
        while (end < self.n):
            
            while ( curSum <= self.x and end < self.n):
                curSum += self.arr[end]
                end += 1
                
            while ( curSum > self.x and start < self.n ):
                if(end - start < result ):
                    result = end - start
                curSum -= self.arr[start]
                start += 1
        return result
    s = Solution(arr,n,x)
    print(s)
        


