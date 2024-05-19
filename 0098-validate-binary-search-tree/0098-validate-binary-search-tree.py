# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root):
        if root:
            left = self.dfs(root.left)
            right = self.dfs(root.right)
            return left + [root.val] + right
        else:
            return []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = self.dfs(root)
        for index in range(len(inorder)-1):
            if inorder[index] >= inorder[index+1]:
                return False
        return True
