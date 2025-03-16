# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []

        def dfs(root, dist):
            if not root:
                return dist+1
            if root == target:
                dist = 0
            
            dist = min(dist, dfs(root.left, dist+1))
            prev_dist = dist
            dist = min(dist, dfs(root.right, dist+1))
            if prev_dist != dist:
                dfs(root.left, dist+1)
            if dist == k:
                res.append(root.val)
            return dist+1
        

        dfs(root, float('inf'))
        return res