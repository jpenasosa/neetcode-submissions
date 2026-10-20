# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle of the array with a fast and slow pointer
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        node = slow.next
        slow.next = None
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev, node = node, temp

        # Step 3: Alternate elements from reversed half into the original head
        node = prev
        while node:
            temp1 = head.next
            temp2 = node.next

            node.next = temp1
            head.next = node

            # Advance
            head = temp1
            node = temp2


