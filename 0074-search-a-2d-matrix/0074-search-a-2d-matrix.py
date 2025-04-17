class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        high = len(matrix) - 1
        low =  0

        while high>=low:
            mid = (high+low)//2

            if matrix[mid][0]<= target <= matrix[mid][-1]:
                return target in matrix[mid]
            elif target < matrix[mid][0]:
                high = mid-1
            else:
                low = mid+1
        return False