"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head =  Node(insertVal)
            head.next = head
            return head
        if head.next == head:
            head.next = Node(insertVal)
            head.next.next = head
            return head
        
        
        
        prev = head
        curr =head.next
        inserted = False

        while True:

            if (prev.val <= insertVal and insertVal<=curr.val) or ((prev.val > curr.val and insertVal < curr.val)) or (prev.val > curr.val and insertVal > prev.val):
                prev.next = Node(insertVal, curr)
                inserted = True
                break
            prev = prev.next
            curr =curr.next
            if prev == head:
                break
        
        if not inserted:
            prev.next = Node(insertVal, curr)

        return head
