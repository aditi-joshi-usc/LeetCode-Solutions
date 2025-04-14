# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        minheap = []


        node  =  head

        while node:
            
            heapq.heappush(minheap,node.val)
            node = node.next
        
        dummy = ListNode()
        head = dummy
        while minheap:
            val = heapq.heappop(minheap)
            head.next = ListNode(val)
            head = head.next
        
        return dummy.next