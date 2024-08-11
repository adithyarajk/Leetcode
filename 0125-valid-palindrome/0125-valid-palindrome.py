class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        process = ""
        s = s.lower()
        for char in s:
            if char.isalnum():
                process+= char

        return process == process[::-1]