'''
Author: 七画一只妖
Date: 2022-02-26 19:06:43
LastEditors: 七画一只妖
LastEditTime: 2022-02-26 21:49:27
Description: file content
'''
class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = -1
        min_p = nums[0]
        for i in range(1,n):
            if nums[i] > min_p:
                ans = max(ans, nums[i] - min_p) # 判断差值是否是更大的
            min_p = min(min_p, nums[i]) # 保护最小值
        return ans


a = Solution
print(a.maximumDifference(a,[9,4,3,2]))