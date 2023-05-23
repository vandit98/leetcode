class Solution:
    def Binary_to_int(self,bi_no)->int:
        no=0
        for i in range(len(bi_no)):
            if bi_no[len(bi_no)-i-1]=='1':
                no+=pow(2,i)
        return no
    def numSteps(self, s: str) -> int:
        num=self.Binary_to_int(s)
        # print("returned no is",num)
        count=0
        while(num!=1):
            if num%2!=0:
                num+=1
                # print(num)
            else:
                num=num//2
                # print(num)
            count+=1
        return count
        