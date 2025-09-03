# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter=[0]
        c=[]
        def dfs(root,k):
            if not root:
                return
            dfs(root.left,k)
            counter[0]+=1
            if counter[0]==k:
                return c.append(root.val)
            dfs(root.right,k)
        dfs(root,k)
        return c[0]




        

        