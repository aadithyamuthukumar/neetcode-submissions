class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        onesList = []
        maxOnes = 0
        for num in nums:
            if num == 0:
                onesList.append(maxOnes)
                maxOnes = 0
            elif num == 1:
                maxOnes += 1
        if maxOnes > 0:
            onesList.append(maxOnes)
        maxOnes = 0
        for ones in onesList:
            if ones > maxOnes:
                maxOnes = ones
        return maxOnes
            
                
