# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # if head.next is None:
        #     return None
        
        # node = head
        # l=0
        # while node:
        #     l+=1
        #     node=node.next

        # node = head
        # i = 0
        # if l-n <=0:
        #     head = head.next
        # else:
        #     while node and i < l - n-1: 
        #         node = node.next
        #         i+=1
            
        #     if node.next:
        #         node.next = node.next.next
        # return head


        res = ListNode(0, head)
        dummy = res

        for i in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return res.next

        