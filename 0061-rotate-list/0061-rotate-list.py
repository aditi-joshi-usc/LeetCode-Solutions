# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        length = 0
        point = head
        while point:
            length+=1
            point=point.next

        fast = head

        for i in range(k%length):
            fast = fast.next
        
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = head
        temp = slow.next
        slow.next = None
        slow = temp
        return temp
