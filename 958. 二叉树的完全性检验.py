
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/discuss/205682/JavaC++Python-BFS-Solution-and-DFS-Soluiton

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        return self.dfs(root) > 0

    def dfs(self, root):
        if not root:
            return 0
        l, r = self.dfs(root.left), self.dfs(root.right)
        if l & (l + 1) == 0 and l / 2 <= r <= l:
            return l + r + 1
        if r & (r + 1) == 0 and r <= l <= r * 2 + 1:
            return l + r + 1
        return -1