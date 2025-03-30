# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return []

        q = deque()
        res = []

        q.append(root)


        while q:
            qlen = len(q)
            
            sumval = 0

            for i in range(qlen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sumval += node.val
            res.append(sumval/qlen)
        return res