
# https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-%28DFS%29.

# DFS
def permute(self, nums):
    res = []
    self.dfs(nums, [], res)
    return res


def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)