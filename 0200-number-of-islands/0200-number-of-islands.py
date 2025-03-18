class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count  = 0

        ROW = len(grid)
        COL = len(grid[0])

        directions = [(1,0), (-1, 0), (0,1), (0, -1)]

        def dfs(r, c):
            if r<0 or r>=ROW or c <0 or c>= COL:
                return
            if grid[r][c] == '0':
                return
            else:
                grid[r][c] = '0'
                for dr, dc in directions:
                    dfs(r+dr, c+dc)
    
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    count+=1
                    dfs(r,c)
        
        return count
