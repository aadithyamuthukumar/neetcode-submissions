# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr = l1
        l1_str = ""
        l2_str = ""
        while curr:
            l1_str = str(curr.val) + l1_str
            curr = curr.next

        curr = l2
        while curr:
            l2_str = str(curr.val) + l2_str
            curr = curr.next
        total = int(l1_str or 0) + int(l2_str or 0)
        total_str = str(total)[::-1]

        dummy = ListNode(0)
        curr = dummy
        for digit in total_str:
            curr.next = ListNode(int(digit))
            curr = curr.next
            
        return dummy.next

        