# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # minheap = []
        # node  =  head

        # while node:
            
        #     heapq.heappush(minheap,node.val)
        #     node = node.next
        
        # dummy = ListNode()
        # head = dummy
        # while minheap:
        #     val = heapq.heappop(minheap)
        #     head.next = ListNode(val)
        #     head = head.next
        
        # return dummy.next

        if not head or not head.next:
            return head
        
        slow  = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)
    

    def merge(self, left, right):
        dummy = ListNode()
        node = dummy
        while left and right:

            if left.val > right.val:
                node.next = right
                right = right.next
            else:
                node.next = left
                left = left.next
            node = node.next
            
            if left:
                node.next = left
            if right:
                node.next = right
        return dummy.next



