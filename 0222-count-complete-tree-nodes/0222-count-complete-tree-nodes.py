# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # return 1 + self.countNodes(root.left) + self.countNodes(root.right) 

        def findLeftHt(node):
            if not node:
                return 0
            ht =1
            while node:
                if node.left:
                    ht+=1
                else:
                    break
                node = node.left
            return ht
        
        def findRightHt(node):
            if not node:
                return 0
            ht =1
            while node:
                if node.right:
                    ht+=1
                else:
                    break
                node = node.right
            return ht
        
        if not root:
            return 0
        
        leftHt = findLeftHt(root)
        rightHt = findRightHt(root)
        if leftHt == rightHt:
            return (2**leftHt) -1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)