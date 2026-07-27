class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_of_nums = []
        for num in nums:
            if num in list_of_nums:
                return True
            list_of_nums.append(num)
        return False

            