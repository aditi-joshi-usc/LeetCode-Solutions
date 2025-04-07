# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(head, tail):
           
            prev = None
            node = head
            while node !=  tail:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev
        
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth =  groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            groupNext= kth.next
            newHead = reverseList(groupPrev.next, groupNext)
            tail = groupPrev.next
            groupPrev.next = newHead
            tail.next = groupNext
            groupPrev = tail
        return dummy.next

