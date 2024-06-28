class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0], max(nums[1], nums[2]))

        maxi = 0

        f_1, f_2, f_n = 0, 0, 0
        for i in range(0, len(nums)-1):
            f_n = max(nums[i]+ f_2, f_1)
            f_2 = f_1
            f_1 = f_n
        maxi = max(maxi, f_n)

        f_1, f_2, f_n = 0, 0, 0
        for i in range(1, len(nums)):
            f_n = max(nums[i]+ f_2, f_1)
            f_2 = f_1
            f_1 = f_n
        maxi = max(maxi, f_n)
    
        return maxi

