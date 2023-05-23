class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
#        we can use the property of xor for a number i.e when we take xor with itself it returns zero
        nums.sort()
        i=0
        while(i<len(nums)-1):
            if nums[i]^nums[i+1]==0:
                i+=2
            else:
                return nums[i]
        return nums[-1]
            
            
            
            
        