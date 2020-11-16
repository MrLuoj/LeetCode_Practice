
# https://leetcode.com/problems/relative-sort-array/discuss/334585/Python-Straight-Forward-1-line-and-2-lines

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {b : i for i, b in enumerate(arr2)}
        return sorted(arr1, key = lambda item : dic.get(item, 1000+item))