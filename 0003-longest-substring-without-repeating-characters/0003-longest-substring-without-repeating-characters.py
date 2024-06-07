class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        charset = set()
        maxLength = 0

        while right < len(s):
            if s[right] not in charset:
                maxLength = max(right-left+1, maxLength)
            else:
                while s[right] in charset:
                    charset.remove(s[left])
                    left +=1
            charset.add(s[right])
            right+=1
        return maxLength