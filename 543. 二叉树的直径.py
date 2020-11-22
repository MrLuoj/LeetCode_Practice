
# https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/er-cha-shu-de-zhi-jing-by-leetcode-solution/

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 1

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.res = max(self.res, left + right + 1)
            return max(left, right) + 1
        depth(root)
        return self.res - 1