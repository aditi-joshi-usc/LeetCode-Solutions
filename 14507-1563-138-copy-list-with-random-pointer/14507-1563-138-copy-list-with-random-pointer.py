"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {None: None}
        node =  head
        
        while node:
            hmap[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            hmap[node].next = hmap[node.next]
            hmap[node].random = hmap[node.random]
            node = node.next

        return hmap[head]

