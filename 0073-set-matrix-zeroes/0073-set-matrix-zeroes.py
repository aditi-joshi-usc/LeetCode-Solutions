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
        for r in row_list:
            matrix[r] = [0 for _ in range(COLS)]
        for c in col_list:
            for r in range(ROWS):
                matrix[r][c] = 0