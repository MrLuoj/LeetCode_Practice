
# https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1

        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007