import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for i in s:
            if i.isalnum():
                ans+=i.lower()
        t=ans
        t=t[::-1]
        if ans==t:
            return True
        return False