# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val <= root.val <= p.val:
            return root
        
        if q.val < root.val:
            return self._lowestCommonAncestor(root.left, p, q)

        return self._lowestCommonAncestor(root.right, p, q)


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Rearrange to guarantee p < q:
        if q.val > p.val:
            p, q = q, p

        return self._lowestCommonAncestor(root, p, q)