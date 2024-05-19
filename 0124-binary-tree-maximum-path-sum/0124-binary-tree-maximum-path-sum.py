# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if not root:
            return -sys.maxsize, -sys.maxsize  # Return negative infinity for non-existent nodes

        left_max_path, left_max_sum = self.dfs(root.left)
        right_max_path, right_max_sum = self.dfs(root.right)
        
        # Max path through root considering the left or right child
        max_single_path = max(left_max_path, right_max_path, 0) + root.val
        
        # Max path that could be the final answer
        max_top = max(max_single_path, left_max_path + root.val + right_max_path)
        
        # The best of the paths so far
        max_sum = max(max_top, left_max_sum, right_max_sum)
        
        return max_single_path, max_sum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _, max_sum = self.dfs(root)
        return max_sum
