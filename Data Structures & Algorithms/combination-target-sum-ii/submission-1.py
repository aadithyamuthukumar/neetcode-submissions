class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        currComb = []
        combs = []
        self.helper(0, nums, target, currComb, combs)
        return combs

    def helper(self, i, nums, target, currComb, combs):
        if target == 0:
            combs.append(currComb.copy())
            return 
        if i >= len(nums) or target < 0:
            return 
        
        currComb.append(nums[i])
        self.helper(i + 1, nums, target - nums[i], currComb, combs)

        currComb.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i + 1, nums, target, currComb, combs)