
# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31381/Python-recursive-and-iterative-solutions.

def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.val)