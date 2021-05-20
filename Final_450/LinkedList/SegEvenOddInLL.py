"""
Given a link list of size N, modify the list such that all the even numbers appear before all the odd numbers in the modified list. The order of appearance of numbers within each segregation should be same as that in the original list.


Example 1:

Input: 
N = 7
Link List = 
17 -> 15 -> 8 -> 9 -> 2 -> 4 -> 6 -> NULL

Output: 8 2 4 6 17 15 9

Explaination: 17,15,8,9 are odd so they appear 
first and 2,4,6 are the even numbers that appear later.

Example 2:

Input:
N = 4
Link List = 1 -> 3 -> 5 -> 7

Output: 1 3 5 7

Explaination: There is no even number. 
So ne need for modification.

Your Task:
You do not need to read input or print anything. Your task is to complete the function divide() which takes N and head of Link List as input parameters and returns the head of modified link list.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
"""


class Solution:
    def divide(self, N, head):
        # code here
        e = None
        o = None
        even = None
        odd = None
        while(head):
            if(head.data % 2 == 0):
                if(even == None):
                    even = head
                    e = head
                else:
                    e.next = head
                    e = e.next
            else:
                if(odd == None):
                    odd = head
                    o = head
                else:
                    o.next = head
                    o = o.next
            head = head.next
        if(e):
            e.next = odd
        if(o):
            o.next = None
        if(even):
            return even
        return odd
