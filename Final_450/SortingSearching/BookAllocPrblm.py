"""
Allocate minimum number of pages 
Hard Accuracy: 48.87% Submissions: 16724 Points: 8
You are given N number of books. Every ith book has Ai number of pages. 
You have to allocate books to M number of students. There can be many ways or permutations to do so. In each permutation, one of the M students will be allocated the maximum number of pages. Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated to a student is minimum of those in all the other permutations and print this minimum value. 

Each book will be allocated to exactly one student. Each student has to be allocated at least one book.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).


Example 1:

Input:
N = 4
A[] = {12,34,67,90}
M = 2
Output:
113
Explanation: 
Allocation can be done in following ways:
{12} and {34, 67, 90} Maximum Pages = 191
{12, 34} and {67, 90} Maximum Pages = 157
{12, 34, 67} and {90}  Maximum Pages =113
Therefore, the minimum of these cases is 
113, which is selected as the output.
Example 2:

Input:
N = 3
A[] = {15,17,20}
M = 2
Output:
32
Explanation:
Allocation is done as 
{15,17} and {20}

Your Task:
You don't need to read input or print anything. Your task is to complete the function findPages() which takes 2 Integers N, and m and an array A[] of length N as input and returns the expected answer.


Expected Time Complexity: O(NlogN)
Expected Auxilliary Space: O(1)


Constraints:
1 <= N <= 105
1 <= A [ i ] <= 106
1 <= M <= 105
"""
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
