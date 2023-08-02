class Solution:
    def firstUniqChar(self, s: str) -> int:

        for index, element in enumerate(s):
            if s.count(element)==1:
                return index
        return -1