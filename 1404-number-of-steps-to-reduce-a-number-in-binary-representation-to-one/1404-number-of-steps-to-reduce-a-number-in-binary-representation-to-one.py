class Solution:
    # def Binary_to_int(self,bi_no)->int:
    #     no=0
    #     for i in range(len(bi_no)):
    #         if bi_no[len(bi_no)-i-1]=='1':
    #             no+=pow(2,i)
    #     return no
    def numSteps(self, s: str) -> int:
    #     num=self.Binary_to_int(s)
    #     # print("returned no is",num)
    #     count=0
    #     while(num!=1):
    #         if num%2!=0:
    #             num+=1
    #             # print(num)
    #         else:
    #             num=num//2
    #             # print(num)
    #         count+=1
    #     return count
    
    
#     solution-2 O(n)
#     initially no of operation for 0 and 1
        dictt={"0":1,"1":2}
        first_one=False
        ans=0
        for j in range(len(s)-1):
            i=s[len(s)-j-1]
            print("we got i as",i)
            if i=="1" and first_one==False:
                first_one=True
                dictt["0"]=2
                dictt["1"]=1
                ans+=2
                print("changing the dicctt pattern")
                print("ans is",ans)
                continue
            ans+=dictt[i]
            print("ans is",ans)
        print(ans)
        if first_one==True:
            ans+=1
            
        return ans
            
            
            
        
        