class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach- take all size of possible substr and check for palindrome
        
        """ 
        ans=s[0]
        if s==s[::-1]:
            return s
        for i in range(1,len(s)):
            for j in range(len(s)-i+1):
                sub=s[j:j+i]
                # print(sub)
                if sub==sub[::-1]:
                    if len(sub)>len(ans):
                        ans=sub
                
        
        return ans