
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n:
            return []
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()
        self.backtrack(n, 0, [])
        return self._generate_results(n)

    def backtrack(self, n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return
        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)

            self.backtrack(n, row+1, cur_state+[col])

            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)

    def _generate_results(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        return [board[i:i+n] for i in range(0, len(board), n)]