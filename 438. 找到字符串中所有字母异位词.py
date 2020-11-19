
# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92009/Python-Sliding-Window-Solution-using-Counter

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_Counter = Counter(p)
        s_Counter = Counter(s[:len(p) - 1])

        for i in range(len(p) - 1, len(s)):
            s_Counter[s[i]] += 1
            if s_Counter == p_Counter:
                res.append(i - len(p) + 1)
            s_Counter[s[i-len(p)+1]] -= 1
            if s_Counter[s[i - len(p) + 1]] == 0:
                del s_Counter[s[i - len(p) + 1]]
        return res