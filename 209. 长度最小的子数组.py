
# https://leetcode.com/problems/minimum-size-subarray-sum/discuss/59093/Python-O%28n%29-and-O%28n-log-n%29-solution

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = 0
        res = 0
        length = len(nums) + 1
        for r, num in enumerate(nums):
            res += num
            while res >= s:
                length = min(length, r - l + 1)
                res -= nums[l]
                l += 1
        return length if length <= len(nums) else 0