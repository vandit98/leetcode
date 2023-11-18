#  using iterative dp- bottom up approach

class Solution:
    def __init__(self):
        self.memo={0:0,1:1,2:1}
        self.ans=0
    def dp(self,n):
        if n==0:
            return 0
        if n<=2:
            return 1
        
        for i in range(3,n+1):
            if i%2==0:
                self.memo[i]=self.memo[int(i/2)]
                self.ans=max(self.ans,self.memo[i])
            else:
                self.memo[i]=self.memo[int((i-1)/2)]+self.memo[int(((i-1)/2))+1]
                # print(f"we have done ans for {i} as by adding {int((i-1)/2)} and {int(((i-1)/2))+1}")
                # print(f"we have {self.memo[int((i-1)/2)]} at {int((i-1)/2)} and {self.memo[int(((i-1)/2))+1]} at {int(((n-1)/2))+1}")
                self.ans=max(self.ans,self.memo[i])
                # print("updated ans is ",self.ans)
        return 
            
        
        
    def getMaximumGenerated(self, n: int) -> int:
        self.dp(n)
        if n==0:
            return 0
        if n<=2:
            return 1
        return self.ans