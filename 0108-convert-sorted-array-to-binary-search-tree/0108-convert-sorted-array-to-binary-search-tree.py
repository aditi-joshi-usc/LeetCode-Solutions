# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums)
        def createTree(left, right):
            if left>right  or right >= n :
                return None
            mid = (left+right)//2

            root= TreeNode(nums[mid])
            root.left = createTree(left, mid-1)
            root.right = createTree(mid+1, right)
            return root
        return createTree(0, n-1)
            
