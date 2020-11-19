
# https://leetcode.com/problems/minimum-path-sum/discuss/23466/Simple-python-dp-70ms

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid
        for i in range(1, len(grid)):
            dp[i][0] += dp[i-1][0]
        for j in range(1, len(grid[0])):
            dp[0][j] += dp[0][j-1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]