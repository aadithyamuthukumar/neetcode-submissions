class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_list = {}
        for i in range(0, len(nums)):
            diff = target-nums[i]
            if diff in final_list:
                return [final_list[diff], i] 
            else:
                final_list[nums[i]] = i
                continue
        return []


