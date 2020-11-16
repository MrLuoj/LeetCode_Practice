
# https://leetcode-cn.com/problems/number-of-1-bits/solution/python3-san-chong-fang-fa-qiu-jie-wei-1de-ge-shu-b/

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res