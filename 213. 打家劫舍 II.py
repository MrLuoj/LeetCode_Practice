
# https://leetcode.com/problems/house-robber-ii/discuss/893957/Python-Just-use-House-Robber-twice

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums):
            last, now = 0, 0
            for num in nums:
                last, now = now, max(last+num, now)
            return now
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1])) if len(nums) != 1 else nums[0]