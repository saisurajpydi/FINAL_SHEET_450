"""
Longest Palindrome in a String
"""
# not wrkng
#code
class Solution:
    def longPalindrome(self,s):
        if(len(s) < 1 or s== None ):
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            leng = max(len1,len2)
             
            if(leng > end - start):
                start = i - (( leng - 1)// 2)
                end = i + (leng // 2 )
        return s[start: end + 1]
    def expand(self,s,left,right):
        if(len(s) == 0 or left > right):
            return 0
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1
t = int(input())
so = Solution()
for i in range(t):
    s=input()
    print(so.longPalindrome(s)