class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # we will use base as 2 to perform string addition
        #making the length o both string equal
        l1=len(a)
        l2=len(b)
        if l1<l2:
            
            a="0"*(abs(l1-l2))+a
        else:
            b="0"*(abs(l1-l2))+b
        l1=len(a)
        ans=""
        carry=0
        # print("final a is ",a)
        # print("final b is ",b)
        for i in range(l1):
            j=l1-i-1
            # adding the reminder
            ans =str((int(a[j])+int(b[j])+carry)%2)+ans
            carry=(int(a[j])+int(b[j])+carry)//2
            # print("ans is ",ans)
            # print("carry is ",carry)
        if carry!=0:
            ans=str(carry)+ans
        # print("final ans is ",ans)
        return ans
            