class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n>0:
            digit = n%2
            if digit == 1:
                count+=1
            n=n//2
        return count