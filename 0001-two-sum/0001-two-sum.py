class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = dict()
        for index, num in enumerate(nums):
            if target - num in hash_table:
                return hash_table.get(target - num), index
            else:
                hash_table[num] = index