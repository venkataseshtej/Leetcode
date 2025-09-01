# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diamter=[0]

        def height(root):
            if not root:
                return 0
            leftmax = height(root.left)
            rightmax= height(root.right)

            diamter[0]= max(diamter[0],leftmax+rightmax)

            return 1+ max(leftmax,rightmax)
        height(root)
        return diamter[0]






        