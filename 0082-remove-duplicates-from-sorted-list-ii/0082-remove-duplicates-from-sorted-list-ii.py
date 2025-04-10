# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # visited = set()

        # dummy = ListNode(0)
        # dummy.next = head
        # prev= None
        # curr = head
        # repeat = set()

        # while curr:
        #     if curr.val in visited:
        #         prev.next= curr.next
        #         repeat.add(curr.val)
        #     else:
        #         visited.add(curr.val)
        #         prev = curr
        #     curr = curr.next
        
        # curr = head
        # prev = dummy
        # while curr:
        #     if curr.val in repeat:
        #         prev.next= curr.next 
        #     else:
        #         prev = curr
        #     curr = curr.next
        # return dummy.next

        dummy = ListNode(0)
        prev = dummy
        curr = head
        dummy.next = curr

        while curr:
            isduplicate = False
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                isduplicate = True
            if isduplicate:
                prev.next = curr.next
                curr = curr.next
            else:
                curr, prev = curr.next, curr
        return dummy.next

