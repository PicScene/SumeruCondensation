'''
Author: 七画一只妖
Date: 2022-08-26 08:29:21
LastEditors: 七画一只妖
LastEditTime: 2022-08-26 08:37:35
Description: file content
'''
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        a, b = nums[0], nums[1]
        if a < b:#确保a最大，b次大
            a, b = b, a
        for i in range(2, len(nums)):
            num = nums[i]
            if num > a:
                a, b = num, a
            elif num > b:
                b = num
        return (a - 1) * (b - 1)


