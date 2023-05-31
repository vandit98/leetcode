class Solution:
    def compress(self, chars: List[str]) -> int:
        tar=chars[0]
        count=0
        ans=""
        j=0
        for i in range(len(chars)):
            if chars[i]==tar:
                count+=1
                # print(f"we got {chars[i]} and increasing count to ",count)
            else:
                ans+=tar
                chars[j]=tar
                j+=1 
                if count>1:
                    if count>9:
                        a=str(count)
                        for k in a:
                            chars[j]=k
                            j+=1
                        
                    else:
                        # ans+=f"{count}"
                        chars[j]=f"{count}"
                        j+=1
                tar=chars[i]
                count=1
        # ans+=tar
        chars[j]=tar
        j+=1
        if count>1:
            if count>9:
                a=str(count)
                for i in a:
                    chars[j]=i
                    j+=1
            else:
                # ans+=f"{count}"
                chars[j]=f"{count}"
                j+=1
        print(ans)
        # print("j is",j)
        chars=chars[:j]
        return len(chars)
        