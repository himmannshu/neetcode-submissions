# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode()
        tmp = ans
        while l1 and l2:
            v = l1.val + l2.val + carry
            tmp.next = ListNode()
            tmp = tmp.next
            tmp.val = v % 10
            carry = v // 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            v = l1.val + carry
            tmp.next = ListNode()
            tmp = tmp.next
            tmp.val = v % 10
            carry = v // 10
            l1 = l1.next

        while l2:
            v = l2.val + carry
            tmp.next = ListNode()
            tmp = tmp.next
            tmp.val = v % 10
            carry = v // 10
            l2 = l2.next

        if carry > 0:
            tmp.next = ListNode()
            tmp = tmp.next
            tmp.val = carry

        return ans.next            

