class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
            i = 0
            for ele in t:
                if i == len(s):
                    return True
                if ele == s[i]:
                    i+=1
            if i == len(s):
                return True
            else:
                return False