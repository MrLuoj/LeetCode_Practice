
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/306427/Different-Python-solutions-with-thinking-process

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit += max(prices[i + 1] - prices[i], 0)
        return max_profit