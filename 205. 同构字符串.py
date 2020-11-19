
# https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-%28dictionary-etc%29.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for i, val in enumerate(s):
            dic1[val] = dic1.get(val, []) + [i]
        for i, val in enumerate(t):
            dic2[val] = dic2.get(val, []) + [i]
        return list(dic1.values()) == list(dic2.values())