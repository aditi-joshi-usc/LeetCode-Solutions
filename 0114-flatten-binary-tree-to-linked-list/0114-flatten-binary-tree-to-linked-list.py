# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        

        def dfs(root):
            if root is None:
                return None
            
            if not root.left and not root.right:
                return root
            
            lefttail = dfs(root.left)
            righttail = dfs(root.right)

            if lefttail:
                lefttail.right =root.right
                root.right = root.left
                root.left = None
            
            if righttail:
                return righttail
            else:
                return lefttail
        dfs(root)