import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Define helpers to build and use heap
        def heappush(i):
            node = lists[i]
            if node:
                heapq.heappush(heap, (node.val, i))
        
        def heappop():
            _, i = heapq.heappop(heap)
            node = lists[i]
            lists[i] = node.next
            heappush(i)
            return node

        # Build inital heap, exiting early if heap is empty
        for i in range(len(lists)):
            heappush(i)

        if not heap: return

        head = heappop()
        cur = head

        while heap:
            cur.next = heappop()
            cur = cur.next

        return head
