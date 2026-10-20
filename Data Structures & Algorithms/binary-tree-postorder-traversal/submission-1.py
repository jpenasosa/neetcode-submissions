# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []

        while root or stack:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.right
            
            root = stack.pop()
            root = root.left

        ans.reverse()
        return ans