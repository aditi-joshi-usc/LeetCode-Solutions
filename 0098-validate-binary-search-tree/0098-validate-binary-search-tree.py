# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def isvalid(node, low, high):
            if not node:
                return True
            
            if low< node.val<high:
                return isvalid(node.left,low, node.val) and isvalid(node.right, node.val, high)
            else:
                return False
        return isvalid(root, float('-inf'), float('inf'))