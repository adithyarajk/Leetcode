class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = dict()
        
        for element in nums:
            if element not in counter.keys():
                counter[element]=1
            else:
                counter[element]+=1
        
        for element in nums:
            if counter[element] > len(nums)/2:
                return element
