
# (·¨1)https://leetcode.com/problems/house-robber/discuss/55696/Python-solution-3-lines.

class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last+num, now)
        return now

# (·¨2)https://leetcode.com/problems/house-robber/discuss/846002/Python-dynamic-programming-easy-solution-faster-than-95

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]


