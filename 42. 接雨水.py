
# https://leetcode.com/problems/trapping-rain-water/discuss/17575/Python-solutions-O%28n%29-space-and-O%281%29-space


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        water = 0
        while l < r:
            if l_max < r_max:
                water += l_max - height[l]
                l += 1
                l_max = max(l_max, height[l])
            else:
                water += r_max - height[r]
                r -= 1
                r_max = max(r_max, height[r])
        return water