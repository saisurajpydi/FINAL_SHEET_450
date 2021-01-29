"""
Write a function that reverses a string. The input string is given as an array of characters char[].
"""
class Solution:
    def reverseString(self, s) -> None:
        return s[::-1]
print("enter the string : ")
s = input()
so = Solution()
print(so.reverseString(s))