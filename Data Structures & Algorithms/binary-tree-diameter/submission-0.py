# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def descend(root: Optional[TreeNode]) -> Tuple[int, int]:
            if not root:
                return 0, 0

            depth_left, d_left = descend(root.left)
            depth_right, d_right = descend(root.right)

            # Max child depth + diamter
            max_depth = max(depth_left, depth_right)
            max_diameter = max(d_left, d_right)

            max_diameter = max(
                max_diameter,
                depth_left + depth_right
            )
            return 1 + max_depth, max_diameter


        depth, diameter = descend(root)
        return max(depth - 1, diameter)