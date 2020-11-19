
# https://leetcode.com/problems/jewels-and-stones/discuss/113553/C++JavaPython-Set-Solution-O%28J-+-S%29

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        set_J = set(J)
        return sum(s in set_J for s in S)

        # sum(s in set_J for s in S) µÈ¼ÛÓÚ
        # res = 0
        # for s in S:
        #     if s in setJ:
        #        res += 1
        # return res