
# https://leetcode.com/problems/reverse-bits/discuss/54748/AC-Python-44-ms-solution-bit-manipulation

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res