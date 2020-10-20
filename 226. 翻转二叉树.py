
# https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python

def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root