


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = nums
        res = max_val = min_val = dp[0]
        for i in range(1, len(dp)):
            if dp[i] < 0:
                min_val, max_val = max_val, min_val
            max_val = max(dp[i], max_val*dp[i])
            min_val = min(dp[i], min_val*dp[i])
            res = max(res, max_val)
        return res