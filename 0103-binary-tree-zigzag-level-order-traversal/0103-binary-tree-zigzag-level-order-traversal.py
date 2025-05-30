# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        flip = False
        q = deque()
        q.append(root)
        
        res = []
        while q:
            qlen = len(q)
            level = [-1]*qlen

            for i in range(qlen):
                node = q.popleft()
                if node is None:
                    continue
                if flip:
                    level[qlen-i-1] = node.val
                else:
                    level[i] = node.val
                
                #level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level:
                # if flip:
                #     res.append(level[::-1])
                # else:
                res.append(level)
            flip =  not flip
        return res