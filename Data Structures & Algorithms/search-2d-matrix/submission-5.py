class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        
        l = 0
        r = rows * cols - 1

        while l <= r:

            m = (l + r) // 2

            x = m // cols
            y = m % cols

            if target < matrix[x][y]:
                r = m - 1
            elif target > matrix[x][y]:
                l = m + 1
            else:
                return True
        
        return False


