
# https://leetcode.com/problems/sliding-puzzle/discuss/142758/Python-very-easy-to-understand-BFS-w-backtracking-concise-solution-beats-98

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4}, 4:{1, 3, 5}, 5:{2, 4}}
        used = set()
        s = "".join(str(c) for row in board for c in row)
        queue = [(s, s.index("0"))]
        count = 0
        while queue:
            new = []
            for s, i in queue:
                used.add(s)
                if s == "123450":
                    return count
                arr = [c for c in s]
                for move in moves[i]:
                    new_arr = arr[:]
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                    new_s = "".join(new_arr)
                    if new_s not in used:
                        new.append((new_s, move))
            count += 1
            queue = new
        return -1