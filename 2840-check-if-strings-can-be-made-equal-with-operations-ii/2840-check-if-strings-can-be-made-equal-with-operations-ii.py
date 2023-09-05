from collections import defaultdict
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_even=[s1[i] for i in range(0,len(s1),2)]
        s1_odd=[s1[i] for i in range(1,len(s1),2)]
        s2_even=[s2[i] for i in range(0,len(s1),2)]
        s2_odd=[s2[i] for i in range(1,len(s1),2)]
  
        s1_even.sort()
        s2_even.sort()
        s1_odd.sort()
        s2_odd.sort()
        print(s1_even)
        print(s2_even)
        return s1_even==s2_even and s2_odd==s1_odd
        