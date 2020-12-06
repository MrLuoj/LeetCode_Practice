
# https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O%28n%29-with-Explanation-Just-walk-each-streak

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best