class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            complement = target-num
            if complement in hash_map:
                return hash_map[complement], index
            hash_map[num] = index

        return -1, -1