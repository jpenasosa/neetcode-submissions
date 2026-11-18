# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, node, prev, k):
        i = 0
        while i < k and node:
            tmp = node.next
            node.next = prev
            prev, node = node, tmp
            i += 1
        
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = 1
        cur = head

        while i < k and cur:
            cur = cur.next
            i += 1

        # Reverse only if we traversed enough elements
        if i == k and cur:
            tmp = cur.next
            cur.next = None

            prev = self.reverse(head, None, k)
            head.next = self.reverseKGroup(tmp, k)

            return prev
        
        return head