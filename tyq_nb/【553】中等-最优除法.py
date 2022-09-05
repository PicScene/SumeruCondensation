'''
Author: 七画一只妖
Date: 2022-02-27 10:25:40
LastEditors: 七画一只妖
LastEditTime: 2022-02-27 10:43:17
Description: file content
'''
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        re = ""
        n = len(nums)
        for i in range(0,n):
            re = re + str(nums[i])
            if i + 1 < n:
                re = re + "/"
        if n > 2:
            re = list(re)
            re.insert(re.index("/") + 1, "(")
            re = "".join(re)
            re = re + ")"
        return re


a = Solution
print(a.optimalDivision(a,[2,3,4]))
