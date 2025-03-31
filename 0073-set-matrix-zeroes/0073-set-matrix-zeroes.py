class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        row_list = set()
        col_list = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row_list.add(r)
                    col_list.add(c)
     
        for c in range(COLS):
            for r in range(ROWS):
                if c in col_list or r in row_list:
                    matrix[r][c] = 0