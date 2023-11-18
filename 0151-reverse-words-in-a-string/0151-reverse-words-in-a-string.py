class Solution:
    def reverseWords(self, s: str) -> str:
        s=s[::-1]
        curr=""
        ran=len(s)
        flag=0
        for i in range(ran):
            if s[i]==" " and len(curr)!=0:
                s+=f"{curr[::-1]} "
                # print(f"adding a word to s and it is now -{s[ran:]}-" )
                curr=""
            elif s[i]==" " and len(curr)==0:
                continue
            else:
                curr+=s[i]
#         adding last word
        if len(curr):
            s+=f"{curr[::-1]}"
        s=s[ran:]
        if s[-1]==" ":
            return s[:-1]
        return s