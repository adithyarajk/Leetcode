class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_list = s.split(" ")
        for ele in split_list[::-1]:
            if len(ele) != 0:
                return len(ele)
        return 0        
