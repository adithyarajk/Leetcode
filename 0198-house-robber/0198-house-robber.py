class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n_1, n_2 = 0, 0
        for i in range(len(nums)):
            fn = max(nums[i]+ n_2, n_1)
            n_2 = n_1
            n_1 = fn
        return fn