
# https://leetcode-cn.com/problems/move-zeroes/solution/dong-hua-yan-shi-283yi-dong-ling-by-wang_ni_ma/

class Solution(object):
    def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		if not nums:
			return 0
		# ��һ�α�����ʱ��jָ���¼��0�ĸ�����ֻҪ�Ƿ�0��ͳͳ������nums[j]
		j = 0
		for i in range(len(nums)):
			if nums[i]:
				nums[j] = nums[i]
				j += 1
		# ��0Ԫ��ͳ�����ˣ�ʣ�µĶ���0��
		# ���Եڶ��α�����ĩβ��Ԫ�ض���Ϊ0����
		for i in range(j,len(nums)):
			nums[i] = 0

