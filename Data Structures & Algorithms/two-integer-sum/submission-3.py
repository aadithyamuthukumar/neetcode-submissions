class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(0, len(nums)):
            if (target-nums[i]) in diffs:
                return [diffs[target-nums[i]], i]
            diffs[nums[i]] = i
                
        
                 

