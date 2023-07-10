class Solution:
    
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        arr=[0,1]
        for i in range(2,n+1):
            arr=[arr[1],arr[0]+arr[1]]
        return arr[1]
            
            