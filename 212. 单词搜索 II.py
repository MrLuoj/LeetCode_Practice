
# https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-%28directly-use-Trie-implemented%29.

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if not current:
                return False
        return current.is_word



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        current = trie.root
        for letter in words:
            trie.insert(letter)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, current, i, j, "", res)
        return res

    def dfs(self, board, current, i, j, path, res):
        if current.is_word:
            res.append(path)
            current.is_word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        current = current.children.get(tmp)
        if not current:
            return
        board[i][j] = "#"
        self.dfs(board, current, i+1, j, path+tmp, res)
        self.dfs(board, current, i-1, j, path+tmp, res)
        self.dfs(board, current, i, j+1, path + tmp, res)
        self.dfs(board, current, i, j - 1, path + tmp, res)
        board[i][j] = tmp