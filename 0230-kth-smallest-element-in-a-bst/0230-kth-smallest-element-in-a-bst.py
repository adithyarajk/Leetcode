# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if root:
            return self.dfs(root.left) + [root.val] + self.dfs(root.right)
        else:
            return []
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = self.dfs(root)
        return inorder[k-1]

