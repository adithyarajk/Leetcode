class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_set = set()
        left = 0
        longest_substring_length = 0

        for right in range(len(s)):
            while s[right] in unique_set:
                unique_set.remove(s[left])
                left += 1
            unique_set.add(s[right])
            longest_substring_length = max(longest_substring_length, right - left + 1)

        return longest_substring_length
