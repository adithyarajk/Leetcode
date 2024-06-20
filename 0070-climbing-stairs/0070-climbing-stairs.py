class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        n_1, n_2 = 1, 1
        for i in range(2, n+1):
            f_n = n_1 + n_2
            n_2 = n_1
            n_1 = f_n
        return f_n