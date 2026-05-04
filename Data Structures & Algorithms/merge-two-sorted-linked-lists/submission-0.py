# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ansNode = ListNode()
        cur = ansNode
        
        while list1 and list2:
            cur.next = ListNode()
            cur = cur.next            
            if list1.val <= list2.val:
                cur.val = list1.val
                list1 = list1.next
            else:
                cur.val = list2.val
                list2 = list2.next
        while list1:
            cur.next = ListNode()
            cur = cur.next            
            cur.val = list1.val
            list1 = list1.next

        while list2:
            cur.next = ListNode()
            cur = cur.next            
            cur.val = list2.val
            list2 = list2.next

        return ansNode.next