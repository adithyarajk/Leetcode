class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)

        def dp_count(i):

            if i == len(s):
                return 1
            if dp[i] != -1:
                return dp[i]
            
            total = 0

            if s[i] != '0':
                total += dp_count(i+1)
                if i+1 < len(s) and int(s[i:i+2]) <=26:
                    total += dp_count(i+2)   
                dp[i] = total 
            return total
        return dp_count(0)
