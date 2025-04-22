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
                if 0<=r<ROWS and 0<=c<COLS:
                    if grid[r][c] == 0:
                        continue
                    if grid[r][c] == 1:
                        fresh_orange_cnt-=1
                        grid[r][c] = 2
                    for dr, dc in directions:
                        nr,nc = r+dr, c+dc
                        if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] ==1:
                            q.append((nr,nc))
                else:
                    continue
            if fresh_orange_cnt == 0:
                return time
            time+=1
        return -1
      





        
