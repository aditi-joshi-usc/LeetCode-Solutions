# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0

        

        node = ListNode(0)
        dummy = ListNode(0)
        dummy = node 

        while l1 or l2:

            sumval = 0

            if l1:
                sumval+=l1.val
                l1 = l1.next
            if l2:
                sumval+=l2.val
                l2 = l2.next
            if carry>0:
                sumval+=carry
            node.next = ListNode(sumval%10)
            node = node.next
            carry = sumval//10
        if carry:
            node.next = ListNode(carry)
        return dummy.next

        