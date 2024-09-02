class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) -1

        while i <= j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return self.utils(s, i+1, j) or self.utils(s, i, j-1)
        return True
    
    def utils(self, s, i, j):
        while i<j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True