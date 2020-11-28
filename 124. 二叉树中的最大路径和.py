
# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float("-inf")
        if not root:
            return 0
        def depth(node):
            if not node:
                return 0
            left_gain = max(depth(node.left), 0)
            right_gain = max(depth(node.right), 0)
            cur_max = node.val + left_gain + right_gain
            self.res = max(cur_max, self.res)
            return max(left_gain, right_gain) + node.val
        depth(root)
        return self.res