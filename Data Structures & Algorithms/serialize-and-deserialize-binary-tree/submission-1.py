from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        arr = []
        q = deque()
        q.append(root)
        h = 0

        # Bfs traversal
        while q:
            h += 1
            for _ in range(len(q)):
                node = q.pop()
                if node:
                    arr.append(node.val)
                    q.appendleft(node.left)
                    q.appendleft(node.right)
                else:
                    arr.append(None)

        return f"{h}|" + ",".join(map(str, arr))

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        h, data = data.split("|")

        arr = []
        for n in data.split(","):
            if n == "None":
                arr.append(None)
            else:
                arr.append(int(n))

        root = TreeNode(arr.pop(0))
        q = deque()
        q.append(root)

        while q and arr:
            for _ in range(len(q)):
                node = q.pop()
                if val := arr.pop(0):
                    node.left = TreeNode(val)
                    q.appendleft(node.left)
                
                if val := arr.pop(0):
                    node.right = TreeNode(val)
                    q.appendleft(node.right)

        return root

