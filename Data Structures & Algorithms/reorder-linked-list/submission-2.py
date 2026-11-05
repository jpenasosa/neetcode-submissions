# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # Step 1: Split list in two
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse list from slow to end
        node = slow.next
        slow.next = None
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            node, prev = tmp, node
        
        # Step 3: Merge the reversed list onto the first half
        while head and prev:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1
            head, prev = tmp1, tmp2


