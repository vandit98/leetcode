class Solution:
    def __init__(self):
        self.memo={0:0,1:0,2:1}
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0 
        if n<=2:
            return 1
        if n in self.memo:
            return self.memo[n]
        self.memo[n]=sum([self.tribonacci(i) for i in range(n-3,n)])
        return self.memo[n]
    
        
        