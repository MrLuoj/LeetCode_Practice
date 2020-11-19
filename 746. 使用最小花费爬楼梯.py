
# https://leetcode.com/problems/min-cost-climbing-stairs/discuss/112870/Simple-Python-Solution
# 思路 https://leetcode-cn.com/problems/min-cost-climbing-stairs/solution/yi-bu-yi-bu-tui-dao-dong-tai-gui-hua-de-duo-chong-/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2]+cost[i], dp[i-1] + cost[i])
        return min(dp[-2], dp[-1])