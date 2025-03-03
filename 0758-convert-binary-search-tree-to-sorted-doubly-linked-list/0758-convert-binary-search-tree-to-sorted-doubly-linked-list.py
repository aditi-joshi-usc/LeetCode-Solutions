"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':   

        # if not root:
        #     return None
       
        # def convert_to_dll(node):
        #     if not node:
        #         return None, None  # No node, no head or tail

        #     # Recursively convert the left and right subtrees
        #     left_head, left_tail = convert_to_dll(node.left)
        #     right_head, right_tail = convert_to_dll(node.right)

        #     # Connect current node with left tail
        #     if left_tail:
        #         left_tail.right = node
        #         node.left = left_tail
        #     else:
        #         left_head = node  # If no left subtree, current node is the head

        #     # Connect current node with right head
        #     if right_head:
        #         right_head.left = node
        #         node.right = right_head
        #     else:
        #         right_tail = node  # If no right subtree, current node is the tail

        #     return left_head, right_tail
            
        # head, _ = convert_to_dll(root)
        # tail = head
        # while tail and tail.right:
        #     tail = tail.right
        # if head and tail:
        #     head.left = tail
        #     tail.right = head
        # return head

        if root is None:
            return None
        head, tail = None, None


        def inorder(node):
            nonlocal head,tail
            if node is None:
                return 

            inorder(node.left)
            if head:
                tail.right = node
                node.left = tail
            else:
                head = node
            
            tail = node
            inorder(node.right)
            
        
        inorder(root)

        if head and tail:
            head.left = tail
            tail.right = head
        return head

                
                