# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float("inf")

        def dfs(root):
            nonlocal ans

            if not root:
                return 0
            
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            max_path = max(left_sum, right_sum, 0)
            ans = max(ans, root.val + max_path, root.val + left_sum + right_sum)
            return root.val + max_path

        dfs(root)
        return ans