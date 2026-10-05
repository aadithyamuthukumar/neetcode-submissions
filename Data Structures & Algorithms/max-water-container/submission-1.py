class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        res = 0


        while l < r:
            left = heights[l]
            right = heights[r]


            width = min(heights[l], heights[r])
            length = r - l
            area =  length * width
            res = max(area, res)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res
