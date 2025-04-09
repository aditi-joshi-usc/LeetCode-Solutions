"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # if not root:
        #     return root
        # q = deque()

        # q.append(root)

        # while q:
        #     qlen = len(q)
        #     prev = None
        #     for i in range(qlen):
        #         node = q.popleft()
        #         if prev:
        #             prev.next = node
        #         prev = node
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return root
        head = root

        while head:
            temp = Node()
            current = temp

            while head:

                if head.left:
                    current.next = head.left
                    current = current.next

                if head.right:
                    current.next = head.right
                    current = current.next
                    
                head = head.next

            head = temp.next

        return root    