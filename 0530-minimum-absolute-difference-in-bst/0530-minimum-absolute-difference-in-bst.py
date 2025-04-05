# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        self.mindiff = float('inf')
        self.prev = None
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.prev:
                self.mindiff = min(self.mindiff, root.val-self.prev.val)
            self.prev = root
            dfs(root.right)

        dfs(root)
        return self.mindiff