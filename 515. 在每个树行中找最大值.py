
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/99018/Python-BFS-and-DFS

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            res.append(max(x.val for x in queue))
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return res