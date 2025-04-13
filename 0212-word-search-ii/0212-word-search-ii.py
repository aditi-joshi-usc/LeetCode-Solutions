# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         maxlen = 0
        
#         for word in words:
#             maxlen = max(maxlen, len(word))
#         m = len(board)
#         n = len(board[0])
#         word_set = set(words)
#         prefix_set = set()

#         for word in words:
#             for i in range(1, len(word)):
#                 prefix_set.add(word[:i])

#         directions = [(1,0), (-1,0), (0,1), (0,-1)]
#         res = set()
#         def traverse_board(subword, r, c, visited):
#             if len(subword) > maxlen :
#                 return
#             if r<0 or r>=m or c<0 or c>=n or (r,c) in visited: 
#                 return
#             subword+= board[r][c]
#             if subword not in prefix_set and subword not in word_set:
#                 return

#             if subword in word_set:
#                 res.add(subword)
#             visited.add((r,c))
#             for dr, dc in directions:
#                 traverse_board(subword, r+dr, c+dc, visited)
#             visited.remove((r,c))


#         for r in range(m):
#             for c in range(n):
#                 traverse_board('', r,c, set())
#         return list(res)

class TreeNode:
    def __init__(self, val=None, isEnd = False):
        self.val = val
        self.children = {}
        self.isEnd = isEnd


class Trie:
    def __init__(self):
        self.root = TreeNode('#')
    def insert(self, val):

        node = self.root
        for v in val:
            if v in node.children:
                node = node.children[v]
            else:
                node.children[v] = TreeNode(v)
                node = node.children[v]
        node.isEnd = True
    
    def search(self, word):
        node = self.root
        
        for w in word:
            if w not in node.children:
                return False
            else:
                node = node.children[w]
        
        return node.isEnd


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        tri = Trie()
        
        for word in words:
            tri.insert(word)
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        res = []


        node = tri.root


        for r in range(len(board)):
            for c in range(len(board[0])):
                self.dfs(board, node, r,c, '', res, directions)

        return res

    def dfs(self, board, node, i, j, sub, res, directions):
        if node.isEnd:
            res.append(sub)
            node.isEnd = False
        
        if i<0 or i>=len(board) or j< 0 or j>= len(board[0]):
            return
        curr = board[i][j]

        if curr not in node.children:
            return
        else:
            node = node.children[curr]
            board[i][j] = '#'

            for dr, dc in directions:
                self.dfs(board, node, i+dr, j+dc, sub+curr, res, directions)

            board[i][j] = curr


       