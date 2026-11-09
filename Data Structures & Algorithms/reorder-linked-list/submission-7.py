# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        node = head
        while node:
            arr.append(node)
            node = node.next
        

        cur = arr[0]
        i, j = 1, len(arr)-1
        while i <= j:
            cur.next = arr[j]
            cur.next.next = arr[i]
            cur = cur.next.next            
            i += 1
            j -= 1

        cur.next = None
