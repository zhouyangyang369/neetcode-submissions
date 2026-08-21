# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        curr1 = l1
        curr2 = l2

        while curr1:
            list1.append(curr1.val)
            curr1 = curr1.next

        while curr2:
            list2.append(curr2.val)
            curr2 = curr2.next

        n1 = 0
        n2 = 0
        for n in range(len(list1)-1, -1, -1):
            n1 = n1 + 10 ** n * list1[n]

        for n in range(len(list2)-1, -1, -1):
            n2 = n2 + 10 ** n * list2[n]

        add = n1 + n2
        sum_listnode = ListNode(0)
        if add == 0:
            return sum_listnode
        curr = sum_listnode
        while add != 0:
            quotient, remainder = divmod(add, 10)
            new = ListNode(remainder)
            curr.next = new
            curr = curr.next
            add = quotient

        return sum_listnode.next

