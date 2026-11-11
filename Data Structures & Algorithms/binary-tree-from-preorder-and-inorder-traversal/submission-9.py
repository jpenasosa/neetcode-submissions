# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {n: i for i, n in enumerate(inorder)}

        def build(l, r):
            if not preorder or l >= r:
                return None

            val = preorder.pop(0)
            root = TreeNode(val)
            mid = index[val]

            root.left = build(l, mid)
            root.right = build(mid+1, r)

            return root

        return build(0, len(inorder))