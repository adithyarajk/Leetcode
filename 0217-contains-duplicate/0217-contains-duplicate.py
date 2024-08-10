class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        contains = set()
        for i in nums:
            if i in contains:
                return True
            else:
                contains.add(i)
        
        return False
        