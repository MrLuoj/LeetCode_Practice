
# https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-%28DFS-recursively-Bit-Manipulation-Iteratively%29.


class Solution(object):
    def subsets(self, nums):
        ret = []
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], path + [nums[i]], ret)

