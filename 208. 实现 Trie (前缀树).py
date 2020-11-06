
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58834/AC-Python-Solution

import collections
# leetcode submit region begin(Prohibit modification and deletion)

class TreeNode:
    def __init__(self):
        self.children = collections.defaultdict(TreeNode)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False

        return current.is_word


    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True