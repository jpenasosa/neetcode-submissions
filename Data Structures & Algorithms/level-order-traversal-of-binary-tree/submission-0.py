from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        q = deque()
        q.appendleft(root)

        while q:
            row = []
            for _ in range(len(q)):
                node = q.pop()
                if node:
                    row.append(node.val)
                    q.appendleft(node.left)
                    q.appendleft(node.right)

            if row:
                ans.append(row)
        
        return ans