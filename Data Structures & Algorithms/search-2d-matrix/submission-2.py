class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        simplified = []
        for i in matrix:
           simplified += i

        l, r = 0, len(simplified)
        
        while l < r:
            mid = l + (r-l)//2
            if target == simplified[mid]:
                return True
            elif target < simplified[mid]:
                r = mid 
            else:
                l = mid + 1

        return False