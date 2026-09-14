class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, currSet = [], []
        self.helper(0, nums, subsets, currSet)
        return subsets
    
    def helper(self, i, nums, subsets, currSet):
        if i >= len(nums):
            subsets.append(currSet.copy())
            return

        currSet.append(nums[i])
        self.helper(i + 1, nums, subsets, currSet)
        currSet.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i + 1, nums, subsets, currSet)

        