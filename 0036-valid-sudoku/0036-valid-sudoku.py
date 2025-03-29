class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        grid = [[[] for i in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                if num in rows[r] or num in cols[c] or num in grid[r//3][c//3]:
                    return False
                else:
                    rows[r].append(num)
                    cols[c].append(num)
                    grid[r//3][c//3].append(num)
        return True  




        