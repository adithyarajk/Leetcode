class Solution:        
    def canJump(self, nums: List[int]) -> bool:
        reacable = 0
        for i in range(len(nums)):
            if reacable < i :
                return False
            reacable = max(reacable, i+nums[i])
        return True
