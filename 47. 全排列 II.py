
# https://leetcode.com/problems/permutations-ii/discuss/18649/Python-easy-to-understand-backtracking-solution.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(nums, [], res)
        return res

    def backtrack(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.backtrack(nums[:i]+nums[i+1:], path+[nums[i]], res)