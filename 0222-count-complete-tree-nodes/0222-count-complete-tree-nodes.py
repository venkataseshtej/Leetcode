# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # count = 1 (for root) + left subtree + right subtree
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        