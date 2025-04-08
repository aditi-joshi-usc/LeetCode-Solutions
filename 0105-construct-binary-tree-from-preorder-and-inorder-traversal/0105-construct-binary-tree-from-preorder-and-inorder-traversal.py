# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

      
        
        
        # def buildtree(pre, inor):
        #     if not pre or not inor:
        #         return None
            
        #     root = TreeNode(pre[0])
        #     mid = inor.index(pre[0])

        #     leftIn = inor[:mid]
        #     rightIn = inor[mid+1:]
        #     leftPre = pre[1:mid+1]
        #     rightPre = pre[mid+1:]

        #     root.left = buildtree(leftPre, leftIn)
        #     root.right = buildtree(rightPre, rightIn)

        #     return root            

        
        # return buildtree(preorder, inorder)

        track = {}

        for index, val in enumerate(inorder):
            track[val] = index
        n = len(preorder)
        def buildtree(prepos, left, right):
            if prepos >=n or right>=n or left>=n or left > right:
                return None
            inpos = track[preorder[prepos]]
            root = TreeNode(preorder[prepos])
            root.left = buildtree(prepos+1, left, inpos-1)
            root.right = buildtree(prepos+ inpos-left +1, inpos+1, right) 
            return root
        return buildtree(0, 0, n-1)
