class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_of_nums = set()
        for num in nums:
            list_of_nums.add(num)
        if len(list_of_nums) < len(nums):
            return True
        else:
            return False
            