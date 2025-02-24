# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapdict = defaultdict(list)
        
        def bfs(node):
            queue = []
            
            queue.append((node, 0))

            while queue:
                node, n = queue.pop(0)
                mapdict[n].append(node.val)
                if node.left is not None:
                    queue.append((node.left, n-1))
                if node.right is not None:
                    queue.append((node.right, n+1))
        if root is None:
            return []
        bfs(root)
        res=[]
        for key in sorted(mapdict.keys()):
            kv = mapdict[key]
            if kv != []:
                res.append(kv)
        return res