
import sys


class Solution:

    # Function to find minimum number of pages.
    def solve(self, arr, n, mid, m):
        su = 0
        stu = 1
        for i in range(n):
            if(arr[i] > mid):
                return False
            if(arr[i] + su > mid):
                stu += 1
                su = arr[i]
                if(stu > m):
                    return False
            else:
                su += arr[i]
        return True

    def findPages(self, arr, n, m):
        # code here
        lb = 0
        mid = 0
        ub = sum(arr)
        ans = 0
        while(lb <= ub):
            mid = (lb + ub)//2
            if(self.solve(arr, n, mid, m)):
                ans = mid
                ub = mid - 1
            else:
                lb = mid + 1
        return ans


if __name__ == "__main__":
    s = Solution()
    N = int(input())
    alist = list(map(int, input().split()))
    M = int(input())
    print(s.findPages(alist, N, M))
