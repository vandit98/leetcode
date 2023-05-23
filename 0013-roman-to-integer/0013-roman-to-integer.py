class Solution:
    def romanToInt(self, s: str) -> int:
        dictt={"I":1,
              "V":5,
              "X":10,
              "L":50,
              "C":100,
              "D":500,
              "M":1000
             }
        ans=dictt[s[0]]
        for i in range(1,len(s)):
            if dictt[s[i-1]]<dictt[s[i]]:
                ans-=2*dictt[s[i-1]]
                ans+=dictt[s[i]]
            else:
                ans+=dictt[s[i]]
            print("alpha is",s[i])
            print(ans)
        return ans
        
            
            
            
        