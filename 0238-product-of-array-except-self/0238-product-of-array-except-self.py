class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_product = [1]*len(nums)
        suffix_product = [1] *len(nums)
        result = [1] *len(nums)
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i-1]*nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            suffix_product[i] = suffix_product[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            result[i] = prefix_product[i] * suffix_product[i]

        return result