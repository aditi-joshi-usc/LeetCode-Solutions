class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_orange_cnt = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_orange_cnt += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        if fresh_orange_cnt == 0:
            return 0
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]
        time = 0
        while q:
            if fresh_orange_cnt == 0:
                return time
            qlen = len(q)
            for _ in range(qlen):
                r,c = q.popleft()
                
                for dr, dc in directions:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] ==1:
                        q.append((nr,nc))
                        fresh_orange_cnt-=1
                        grid[nr][nc] = 2  
            if q:
                time+=1
            
        if fresh_orange_cnt ==0:
            return time
        else:
            return -1
      





        
