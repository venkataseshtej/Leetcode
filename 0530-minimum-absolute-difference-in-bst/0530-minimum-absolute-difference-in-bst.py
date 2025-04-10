# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev= [None]
        minimum=[float(inf)]
        def dfs(node):    
            if node is None:
                return
            dfs(node.left)
            if prev[0]is not None:
                minimum[0]=min(minimum[0], node.val - prev[0])
            prev[0]=node.val
            dfs(node.right)
            # return minimum[0]
        dfs(root)
        return minimum[0]
        
            
            

        

        

        
        