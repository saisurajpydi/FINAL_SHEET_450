"""
Java Program to Check if a string is a valid shuffle of two distinct strings
"""
class Solution:
    def isSuffle(self,str1,str2, result):
        #print(len(str1+str2) != len(result))
        if(len(str1+str2) != len(result)):
            return False
        i, j, k = 0,0,0
        while(k != len(result)):
            if(i < len(str1) and str1[i] == result[k]):
                i += 1
            elif(j < len(str2) and str2[j] == result[k]):
                j += 1
            else:
                return False
            k += 1

        if( i < len(str1) or j < len(str2)):
            return False
        return True



str1 = input("enter string 1 : ")
str2 = input("enter string 2 : ")
#temp = str1+str2
str3 = input("enter the to be checked string : ")
so = Solution()
print(so.isSuffle(str1,str2,str3))