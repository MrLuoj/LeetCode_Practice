
# https://leetcode.com/problems/majority-element/discuss/51712/Python-different-solutions-%28dictionary-bit-manipulation-sorting-divide-and-conquer-brute-force-etc%29.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num in nums:
            if dic[num] > len(nums) // 2:
                return num