class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):  # Assuming 32-bit unsigned integer
            ans = (ans << 1) | (n & 1)
            n >>= 1
        return ans
