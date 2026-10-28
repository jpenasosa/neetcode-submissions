# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {val:idx for idx, val in enumerate(inorder)}

        def build(preorder, start, end):
            if not preorder or start >= end:
                return None

            val = preorder.pop(0)
            root = TreeNode(val=val)
            mid = index[val]

            root.left = build(preorder, start, mid)
            root.right = build(preorder, mid+1, end)

            return root
        
        return build(preorder, 0, len(preorder))
