class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for i in range(m)]
        
        def backtrack(r, c, index):
            if index == len(word)-1:
                return True
            
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and visited[nr][nc] == False and  board[nr][nc] == word[index+1]:
                    if backtrack(nr, nc, index+1):
                        return True
            visited[r][c] = False
            return False
                






        start_word = word[0]

        for i in range(m):
            for j in range(n):
                if board[i][j] == start_word:
                    if backtrack(i, j, 0):
                        return True
        return False
        
        