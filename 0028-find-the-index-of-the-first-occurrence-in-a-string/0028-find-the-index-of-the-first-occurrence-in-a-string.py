class Solution:
    def checker(self,a,b):
        if a==b:
            return True
        return False
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                if self.checker(needle,haystack[i:len(needle)+i]):
                    return i
                # function check
            else:
                continue
        return -1