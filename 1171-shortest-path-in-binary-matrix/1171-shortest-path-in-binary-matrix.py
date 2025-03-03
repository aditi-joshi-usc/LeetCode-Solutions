class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        directions = [(1,0), (0,1), (1,1), (-1,1), (1,-1), (-1,-1), (-1,0), (0,-1)]
        
        
        visited = [[False]*n for _ in range(n)]
        q = deque([(0,0,1)])
        visited[0][0] = True



        while q:
            i,j,path = q.popleft()

            if i == n-1 and j == n-1:
                return path
            
            for dr, dc in directions:
                row = i+dr
                col = j+dc
                if 0<=row<n and 0<=col<n and grid[row][col] == 0 and not visited[row][col]:
                    q.append((row,col,path+1))
                    visited[row][col] = True
        return -1