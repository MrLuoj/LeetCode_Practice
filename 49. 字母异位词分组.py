
# https://leetcode-cn.com/problems/group-anagrams/solution/python3-99-by-meng-zhi-hen-n/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())
