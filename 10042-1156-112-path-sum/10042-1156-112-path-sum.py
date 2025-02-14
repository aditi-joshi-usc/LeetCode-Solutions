# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        
        def find_target(root, targetSum, sumval):
            if root is None:
                    return False
            
            if root.left is None and root.right is None and sumval+root.val ==targetSum:
                return True
            leftNode = find_target(root.left, targetSum, sumval+root.val)
            rightNode = find_target(root.right, targetSum, sumval+root.val)
            return leftNode or rightNode

        return find_target(root, targetSum, 0)
        