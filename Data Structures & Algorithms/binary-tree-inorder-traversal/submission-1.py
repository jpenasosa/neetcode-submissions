# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], array: List[int]):
        if not root:
            return
        
        self.traverse(root.left, array)
        array.append(root.val)
        self.traverse(root.right, array)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        self.traverse(root, ans)

        return ans