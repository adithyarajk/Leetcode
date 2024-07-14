class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = nums[0]
        maxi = nums[0]

        for i in nums[1:]:
            if cur_max < 0:
                cur_max = 0
            cur_max += i
            maxi = max(maxi, cur_max)
        return maxi