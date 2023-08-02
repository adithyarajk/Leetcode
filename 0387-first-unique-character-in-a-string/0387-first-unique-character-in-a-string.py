class Solution:
    def firstUniqChar(self, s: str) -> int:

        counter = dict()
        for element in s:
            if element not in counter.keys():
                counter[element] =1
            else:
                counter[element]+=1
        
        
        for index, element in enumerate(s):
            if counter[element]==1:
                return index
        return -1