class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:




        r = 0
        c = len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:



            if target == matrix[r][c]:
                return True
            

            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1
    
        return False
