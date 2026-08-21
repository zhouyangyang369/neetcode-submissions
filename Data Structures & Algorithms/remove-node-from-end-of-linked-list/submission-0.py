# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        reversed_head = ListNode(0, prev)
        curr = reversed_head

        while n != 0:
            prev = curr
            curr = curr.next
            n -= 1

        prev.next = curr.next
        curr.next = None



        prev = None
        curr = reversed_head.next
        reversed_head.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev