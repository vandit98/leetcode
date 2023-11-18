class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
#         finding minimum and maximum at the starting index
#         initialising the min and max value 
        minn=nums[0]
        maxx=nums[0]
        maxx_index=0
        minn_index=0
        for i in range(indexDifference,len(nums)):
            minn=min(minn,nums[i-indexDifference])
            maxx=max(maxx,nums[i-indexDifference])
            if minn==nums[i-indexDifference]:
                minn_index=i-indexDifference
            if maxx==nums[i-indexDifference]:
                maxx_index=i-indexDifference
            if abs(nums[maxx_index]-nums[i])>=valueDifference:
                return (maxx_index,i)
            elif abs(nums[minn_index]-nums[i])>=valueDifference:
                return (minn_index,i)
#             else:
#                 # print("into the else")
#                 print("this is the value we got to check",nums[i-indexDifference])
#                 print("minn is ",minn)
                
            # print(f"minimum index is {minn_index} and has value as ",minn)
            # print(f"minimum index is {maxx_index} and has value as ",maxx)
            # print("current index is ",i-indexDifference)
        return [-1,-1]
                
                
        
       
                