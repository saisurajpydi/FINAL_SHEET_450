"""
Weighted Job Scheduling in O(n Log n) time
Difficulty Level : Hard
Last Updated : 26 Apr, 2020
Given N jobs where every job is represented by following three elements of it.

Start Time
Finish Time
Profit or Value Associated
Find the maximum profit subset of jobs such that no two jobs in the subset overlap.

Example:

Input: Number of Jobs n = 4
       Job Details {Start Time, Finish Time, Profit}
       Job 1:  {1, 2, 50} 
       Job 2:  {3, 5, 20}
       Job 3:  {6, 19, 100}
       Job 4:  {2, 100, 200}
Output: The maximum profit is 250.
We can get the maximum profit by scheduling jobs 1 and 4.
Note that there is longer schedules possible Jobs 1, 2 and 3 
but the profit with this schedule is 20+50+100 which is less than 250.
"""
"""
algorithm:
1.Sort the jobs by non-decreasing finish times.
2.For each i from 1 to n, determine the maximum value of the schedule from the subsequence of jobs[0..i]. Do this by comparing the inclusion of job[i] to the schedule to the exclusion of job[i] to the schedule, and then taking the max.
To find the profit with inclusion of job[i]. we need to find the latest job that doesn’t conflict with job[i]. The idea is to use Binary Search to find the latest non-conflicting job.
"""


class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit


class Solution:
    def binarySearch(self, job, start_index):
        lo = 0
        hi = start_index-1
        while(lo <= hi):
            mid = (lo + hi)//2
            if(job[mid].finish <= job[start_index].start):
                if(job[mid+1].finish <= job[start_index].start):
                    lo = mid+1
                else:
                    return mid
            else:
                hi = mid-1
        return -1

    def schedule(self, job):
        job = sorted(job, key=lambda j: j.finish)
        n = len(job)
        table = [0]*n
        table[0] = job[0].profit
        for i in range(1, n):
            inProfit = job[i].profit
            l = self.binarySearch(job, i)
            if(l != -1):
                inProfit += table[l]
            table[i] = max(inProfit, table[i-1])
        return table[n-1]


if __name__ == "__main__":
    so = Solution()
    job = [Job(1, 2, 50), Job(3, 5, 20), Job(6, 19, 100), Job(2, 100, 200)]
    print("optimal profit")
    print(so.schedule(job))
