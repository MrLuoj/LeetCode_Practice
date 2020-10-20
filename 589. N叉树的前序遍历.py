
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/155806/Python-iterative-and-recursive-solution-with-explanation

def postorder(self, root):
    """
    :type root: Node
    :rtype: List[int]
    """
    res = []
    if root == None: return res

    def recursion(root, res):
        res.append(root.val)
        for child in root.children:
            recursion(child, res)

    recursion(root, res)
    return res