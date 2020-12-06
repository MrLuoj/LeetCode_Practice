
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        self.pre = None
        self.dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

    def dfs(self, cur):
        if not cur:
            return
        self.dfs(cur.left)
        if self.pre:
            self.pre.right, cur.left = cur, self.pre
        else:
            self.head = cur
        self.pre = cur
        self.dfs(cur.right)