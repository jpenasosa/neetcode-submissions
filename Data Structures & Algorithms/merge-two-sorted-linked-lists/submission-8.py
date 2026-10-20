# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None

        if list1 and (not list2 or list1.val <= list2.val):
            head = list1
            list1 = list1.next
        elif list2:
            head = list2
            list2 = list2.next

        node = head
        while list1 or list2:
            if list1 and (not list2 or list1.val <= list2.val):
                node.next = list1
                list1 = list1.next
            elif list2:
                node.next = list2
                list2 = list2.next

            node = node.next

        return head
