class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[-1,0], [-1,1], [0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        
        def findlivcount(r,c):
            count = 0
            for dr, dc in directions:
                row, col = r+dr, c+dc
              
                if 0<=row<ROWS and 0<=col<COLS : 
                    count += board[row][col] % 2
            return count


        for r in range(ROWS):
            for c in range(COLS):
                count = findlivcount(r,c)
                if board[r][c]== 1 and (count < 2 or count>3):
                    board[r][c] = -1
                elif board[r][c] == 0 and count == 3:
                    board[r][c] = 2
            
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
                    
                

