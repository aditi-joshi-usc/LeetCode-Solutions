class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr_color = image[sr][sc]
        if curr_color == color:
            return image
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]
        m = len(image)
        n = len(image[0])
        #visited = set()
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n:
                return
            # if (r,c) in visited:
            #     return

            if image[r][c] !=curr_color:
                return
        
            image[r][c] = color
            #visited.add((r,c))
            for dr, dc in directions:
                dfs(dr+r, dc+c)
        
        dfs(sr,sc)
        return image
