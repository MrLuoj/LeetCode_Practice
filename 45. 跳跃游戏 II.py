
# https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            next = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, next
        return times