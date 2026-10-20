# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def descend(root: Optional[TreeNode]) -> Tuple[int, bool]:
            if not root:
                return 0, True

            left_depth, left_balanced = descend(root.left)
            right_depth, right_balanced = descend(root.right)
            
            if not (left_balanced and right_balanced) or abs(left_depth - right_depth) > 1:
                return - 1, False
            
            return 1 + max(left_depth, right_depth), True
        
        _, is_balanced = descend(root)
        return is_balanced
        