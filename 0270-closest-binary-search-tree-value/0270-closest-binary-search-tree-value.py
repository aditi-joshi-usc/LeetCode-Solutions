# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        

        floor = root.val
        ceil = root.val

        curr = root

        while curr:

            if curr.val == target:
                return curr.val
            
            if curr.val>target:
                ceil = curr.val
                curr = curr.left
            else:
                floor = curr.val
                curr = curr.right
        
        d1 = abs(target - ceil)
        d2 = abs(target - floor)

        if d1< d2:
            return ceil
        else:
            return floor