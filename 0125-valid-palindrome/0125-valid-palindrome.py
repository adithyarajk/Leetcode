class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        e = ""
        for ele in s:
            if ele.isalnum():
                e = e +ele
        
        return e == e[::-1]