class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r = 0
        c = len(matrix[0]) - 1
        m = len(matrix)

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False