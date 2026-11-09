import json

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

        node = root
        def dfs(root):
            if not root:
                arr.append(None)
                return
            
            arr.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return json.dumps(arr)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        arr = json.loads(data)

        def build():
            val = arr.pop(0)
            if not val:
                return None
            
            node = TreeNode(val)
            node.left = build()
            node.right = build()
            return node

        return build()

