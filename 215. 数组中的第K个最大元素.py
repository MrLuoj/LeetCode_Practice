
# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-%28bubble-sort-selection-sort-heap-sort-and-quick-sort%29.
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)