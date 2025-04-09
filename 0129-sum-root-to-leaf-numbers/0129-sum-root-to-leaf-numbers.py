# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(root, num):
            if not root:
                return
            num = num*10 + root.val
            if not root.left and not root.right:
                res.append(num)
                return
            
            dfs(root.left, num)
            dfs(root.right, num)

        dfs(root, 0)
        return sum(res)