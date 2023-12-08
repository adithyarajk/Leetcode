# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        if root:
            result = str(root.val)
            if root.left is None and root.right is None:
                return result
            
            
            result += "("+ self.tree2str(root.left)+")"
            if root.right:
                result += "("+self.tree2str(root.right)+")"
            return result
