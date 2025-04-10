# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float('-inf')

        def findsum(root, sumval):
            if not root:
                return 0
           
            gain_left = max(findsum(root.left, sumval), 0)
            gain_right = max(findsum(root.right, sumval), 0)
            self.maxsum = max( gain_left+ root.val+gain_right, self.maxsum)
            return max(gain_left, gain_right) + root.val
        findsum(root,0)
        return self.maxsum