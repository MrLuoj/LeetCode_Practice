
# https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-%28top-down-bottom-up%29.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]