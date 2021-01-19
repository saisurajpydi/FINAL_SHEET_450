# Python3 program to merge overlapping Intervals  
# in O(n Log n) time and O(1) extra space 
def mergeIntervals(arr): 
          
        # Sorting based on the increasing order  
        # of the start intervals 
        arr.sort(key = lambda x: x[0])  
          
        # array to hold the merged intervals 
        m = [] 
        s = -10000
        max = -100000
        for i in range(len(arr)): 
            a = arr[i] 
            if a[0] > max: 
                if i != 0: 
                    m.append([s,max]) 
                max = a[1] 
                s = a[0] 
            else: 
                if a[1] >= max: 
                    max = a[1] 
          
        #'max' value gives the last point of  
        # that particular interval 
        # 's' gives the starting point of that interval 
        # 'm' array contains the list of all merged intervals 
  
        if max != -100000 and [s, max] not in m: 
            m.append([s, max]) 
        print("The Merged Intervals are :", end = " ") 
        for i in range(len(m)): 
            print(m[i], end = " ") 
  
# Driver code 
arr = [[6, 8], [1, 9], [2, 4], [4, 7],[13,19]] 
mergeIntervals(arr)

# easy solution 
"""
class Solution:
    def merge(self, A):
        ans = [] #stack
        A.sort(key=lambda x:x[0]) #sort by start time
        for x,y in A:
            #if stack is empty just append it
            if not ans: 
                ans.append([x,y]) 
                continue
            #stack is nonempty
            x0, y0 = ans[-1]
            if x>y0:
                ans.append([x,y]) #if there is no overlap just append it
            else:
                ans.pop()
                ans.append([x0,max(y0,y)]) #there is overlap, for end point pick max(y0,y)
        return ans   
"""