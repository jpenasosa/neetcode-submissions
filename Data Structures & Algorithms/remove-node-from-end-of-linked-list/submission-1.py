# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        # Calculate index to be removed, handle special case
        rm_index = length - n
        if rm_index == 0:
            return head.next
        
        # Iterate to note before the one deleted, and remove it
        node = head
        for _ in range(rm_index - 1):
            node = node.next
        
        node.next = node.next.next

        return head
