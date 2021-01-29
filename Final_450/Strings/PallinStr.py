"""
Given a string S, check if it is palindrome or not.
"""
class Solution:
	def isPlaindrome(self, s):
		# code here
		x = s
		if( x[::-1] == s):
		    return 1
		return 0
s = input("enter the string : ")
so = Solution()
print(so.isPlaindrome(s))