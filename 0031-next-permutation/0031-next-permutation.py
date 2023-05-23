class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=nums.copy()
        c=nums.copy()
        if nums==sorted(x,reverse=True):
            nums.sort()
            # print("returning since reversed i.e ",nums)
            return
        elif c.sort()==nums:
            # print("got a sorted nums")
            nums[-1]=c[-2]
            nums[-2]=c[-1]
            # print("nums is, swapping last two",nums)
            return
        else:
            for i in range(len(nums)-1,0,-1):
                if nums[i]<=nums[i-1]:
                    # print("continue")
                    continue
                else:
                    # print("we are at ",nums[i])
                    final=nums[i-1:]
                    parent=nums[i]
                    left=nums[i-1]
                    right=nums[i+1:]
                    # print("left is",left)
#                     finding just bigger than left
                    final.sort()
                    print("final is",final)
                    for t in final:
                        if t>left:
                            start=t
                            break
                    final.remove(start)
                    print("start is",start)
                    final.sort()
                    nums[i-1]=start
                    for j in range(i,len(nums)):
                        nums[j]=final[j-i]
                    # print("final nums is ",nums)
                    break
        print(nums)
        return None

