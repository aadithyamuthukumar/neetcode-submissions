class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, num in enumerate(nums):
            if num in hashmap:
                return [hashmap[num], i]
            diff = target - num
            hashmap[diff] = i