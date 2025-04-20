# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(p,q):
            if not p and not q:
                return True
            elif (p and not q) or (q and not p) or (p.val != q.val):
                return False
            else:
                return same_tree(p.left, q.left) and same_tree(p.right, q.right)

        def check(l,m):
            if not l and not m:
                 return True
            return same_tree(l, m) or same_tree(l.left, m) or same_tree(l.right,m)
            
        return check(root, subRoot)

