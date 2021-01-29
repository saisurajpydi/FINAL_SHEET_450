"""
A Program to check if strings are rotations of each other or not

(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)
"""

class Solution:
    def isRotate(self,str1, str2):
        temp = str1 + str1
        if(str2 in temp):
            return True
        return False

str1 = input("enter string 1 : ")
str2 = input("enter string 2 : ")
so = Solution()
print(so.isRotate(str1,str2))
