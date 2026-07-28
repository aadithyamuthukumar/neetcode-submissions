class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > majority:
                return num
