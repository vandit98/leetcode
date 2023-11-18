import math

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        predicate func:- the first time when the first elem of repeated no takes odd index- true starts from there
        format - FFFFFFTTTTTTT
        
        aim:- Find the first True
    
        """
        # if len(nums)==1:
        #     return 1
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            # mid will be lower mid since lo is getting updated
            mid = lo + math.floor((hi - lo) / 2)
            # false condition
            if (nums[mid] != nums[mid - 1] and nums[mid] == nums[mid + 1] and mid % 2 == 0) or ((nums[mid] == nums[mid - 1] and nums[mid] != nums[mid + 1] and mid % 2 != 0)):
                # ans will be in the right half
                lo = mid + 1
            elif nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]    
            else:
                hi = mid
        return nums[lo]
