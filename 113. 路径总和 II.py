
# https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-%28Recursively-BFS+queue-DFS+stack%29

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.dfs(root, sum, [], res)
        return res


    def dfs(self, root, sum, path, res):
        if not root:
            return
        if not root.left and not root.right and sum == root.val:
            path.append(root.val)
            res.append(path)
        self.dfs(root.left, sum - root.val, path + [root.val], res)
        self.dfs(root.right, sum - root.val, path + [root.val], res)