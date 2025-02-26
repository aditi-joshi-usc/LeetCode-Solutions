# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self.sum_val = 0


        def dfs(node):
            sumv = 0
            if node is None:
                return 0
            if node.val<= high and node.val>=low:
                sumv = node.val
            
            if node.val > low:
                sumv += dfs(node.left)
            if node.val < high:
                sumv += dfs(node.right)

            return sumv

        return dfs(root)