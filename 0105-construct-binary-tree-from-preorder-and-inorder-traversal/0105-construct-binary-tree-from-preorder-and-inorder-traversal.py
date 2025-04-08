# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

      
        
        
        def buildtree(pre, inor):
            if not pre or not inor:
                return None
            
            root = TreeNode(pre[0])
            mid = inor.index(pre[0])

            leftIn = inor[:mid]
            rightIn = inor[mid+1:]
            leftPre = pre[1:mid+1]
            rightPre = pre[mid+1:]

            root.left = buildtree(leftPre, leftIn)
            root.right = buildtree(rightPre, rightIn)

            return root            

        
        return buildtree(preorder, inorder)
        