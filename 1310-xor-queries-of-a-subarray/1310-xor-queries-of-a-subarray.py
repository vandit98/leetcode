# from collections import defaultdict
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor=[0]
        run_xor=0
        for i in range(len(arr)):
            run_xor=run_xor^arr[i]
            prefix_xor.append(run_xor)
        # print("prefix_xor is",prefix_xor)
        ans=[]
        for i in queries:
            # print(i)
            start=i[0]
            end=i[1]
            ans.append(prefix_xor[end+1]^   prefix_xor[start])
            # print(ans)
        return ans
    
    