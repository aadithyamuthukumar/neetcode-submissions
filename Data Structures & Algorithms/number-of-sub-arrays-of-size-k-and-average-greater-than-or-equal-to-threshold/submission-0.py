class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        R = 0
        res = 0
        currSum = 0
        target = threshold * k


        for R in range (len(arr)):
            currSum += arr[R]

            if R >= k - 1:

                if currSum >= target:
                    res += 1

                currSum -= arr[R - k + 1]
        
        return res