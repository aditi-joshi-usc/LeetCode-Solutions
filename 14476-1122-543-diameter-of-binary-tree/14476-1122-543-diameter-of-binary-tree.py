# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diam = 0

        def dfs(root):
            if root is None:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            self.max_diam = max(self.max_diam, r+l)

            return 1 + max(l,r)

        dfs(root)
        return self.max_diam