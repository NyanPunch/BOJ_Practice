# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_Depth = self.maxDepth(root.left)
        right_Depth = self.maxDepth(root.right)
        return max(left_Depth, right_Depth) + 1