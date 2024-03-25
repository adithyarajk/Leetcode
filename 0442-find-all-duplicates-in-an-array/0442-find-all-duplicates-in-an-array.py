class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = {}
        result = []
        for num in nums:
            if num not in dup:
                dup[num] = 1
            else:
                dup[num]+=1
        
        for key, val in dup.items():
            if val == 2:
                result.append(key)
        return result