class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        maxlen = 0
        
        for word in words:
            maxlen = max(maxlen, len(word))
        m = len(board)
        n = len(board[0])
        word_set = set(words)
        prefix_set = set()

        for word in words:
            for i in range(1, len(word)):
                prefix_set.add(word[:i])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        res = set()
        def traverse_board(subword, r, c, visited):
            if len(subword) > maxlen :
                return
            if r<0 or r>=m or c<0 or c>=n or (r,c) in visited: 
                return
            subword+= board[r][c]
            if subword not in prefix_set and subword not in word_set:
                return

            if subword in word_set:
                res.add(subword)
            visited.add((r,c))
            for dr, dc in directions:
                traverse_board(subword, r+dr, c+dc, visited)
            visited.remove((r,c))


        for r in range(m):
            for c in range(n):
                traverse_board('', r,c, set())
        return list(res)
