class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for num in nums:
            numSet.add(num)
        
        if len(numSet) == len(nums):
            return False
        else:
            return True