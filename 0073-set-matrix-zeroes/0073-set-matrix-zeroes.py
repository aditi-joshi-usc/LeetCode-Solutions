# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         ROWS = len(matrix)
#         COLS = len(matrix[0])

#         row_list = set()
#         col_list = set()

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if matrix[r][c] == 0:
#                     row_list.add(r)
#                     col_list.add(c)
#         for r in row_list:
#             matrix[r] = [0 for _ in range(COLS)]
#         for c in col_list:
#             for r in range(ROWS):
#                 matrix[r][c] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        is_col = False
        for r in range(ROWS):
            if matrix[r][0] == 0:
                is_col = True
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] ==0 or matrix[r][0] ==0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for c in range(COLS):
                matrix[0][c] = 0
            
        if is_col:
            for r in range(ROWS):
                matrix[r][0] = 0