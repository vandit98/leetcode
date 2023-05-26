#         using xor concept
#         creating two pointer to comaprare both ends
    
class Solution:
    def palindrome_checker(self,s:str):
        if s==s[::-1]:
            return True
        else:
            return False
    def validPalindrome(self, s: str) -> bool:
        j=len(s)-1
        i=0
        while(i<j):
            if s[i]==s[j]:
                i+=1
                j-=1
                continue
            else:
#                 deleting the jth element or ith element
                if self.palindrome_checker(s[:i]+s[i+1:]) or self.palindrome_checker(s[:j]+s[j+1:]):
                    return True
                return False
        return True
            
            

        
        