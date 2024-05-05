class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        if set(s) != set(t):
            return False

        count_s = {}
        count_t = {}
        for ele in s:
            if ele not in count_s:
                count_s[ele] = 1
            else:
                count_s[ele] += 1
        for ele in t:
            if ele not in count_t:
                count_t[ele] = 1
            else:
                count_t[ele] += 1
        
        for ele in s:
            if count_s[ele] != count_t[ele]:
                return False
        
        return True