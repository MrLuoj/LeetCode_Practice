
# https://leetcode.com/problems/rotate-array/discuss/54294/My-solution-by-using-Python

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        n, k = len(nums), k % len(nums)
        if k:
            swap(0,n-1)
            swap(0,k-1)
            swap(k,n-1)