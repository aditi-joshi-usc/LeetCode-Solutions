class Solution(object):
    def numRookCaptures(self, board):
        # Find the rook's position
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_row, rook_col = i, j
                    break
        
        captures = 0
        # Define the 4 possible directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
        for dr, dc in directions:
            r, c = rook_row, rook_col
            while True:
                r += dr
                c += dc
                # If we go out of bounds, stop searching in this direction.
                if r < 0 or r >= 8 or c < 0 or c >= 8:
                    break
                # If we hit a bishop, the rook cannot go past it.
                if board[r][c] == 'B':
                    break
                # If we hit a pawn, count it and stop in this direction.
                if board[r][c] == 'p':
                    captures += 1
                    break
                
        return captures