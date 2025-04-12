class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0), (-1, 0), (0,1), (0, -1)]
        ROWS =len(board) 
        COLS =len(board[0])
        def traverse_region(r,c):
            if 0<=r<ROWS and 0<=c<COLS and board[r][c] == 'O':
                board[r][c] = '#'
                
                for dr, dc in directions:
                    traverse_region(r+dr, c+dc)
            return
                 


        for col in range(COLS):
            traverse_region(0, col)
            traverse_region(ROWS-1, col)
        
        for row in range(ROWS):
            traverse_region(row, 0)
            traverse_region(row, COLS-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
            

        