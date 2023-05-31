class Solution:
    def compress(self, chars: List[str]) -> int:
        tar=chars[0]
        count=0
        ans=""
        for i in range(len(chars)):
            if chars[i]==tar:
                count+=1
                # print(f"we got {chars[i]} and increasing count to ",count)
            else:
                ans+=tar
                if count>1:
                    ans+=f"{count}"
                tar=chars[i]
                count=1
        ans+=tar
        if count>1:
            ans+=f"{count}"
        print(ans)
        chars.clear()
        for i in ans:
            chars.append(i)
        # chars=list(ans)
        print("chars is ",chars)
        return len(chars)
        