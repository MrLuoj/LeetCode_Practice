
# https://leetcode.com/problems/sqrtx/discuss/25061/Python-binary-search-solution-%28O%28lgn%29%29.

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= x:
            mid = l + (r - l) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 < x:
                l = mid + 1
            else:
                r = mid - 1
        return - 1