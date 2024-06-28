class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans = i ^ ans
        
        for i in range(len(nums)+1):
            ans = ans ^ i
        return ans