'''
Author: 七画一只妖
Date: 2022-08-04 09:35:49
LastEditors: 七画一只妖
LastEditTime: 2022-08-04 09:48:42
Description: file content
'''
class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        ans = []

        sum = 0
        count = [0] * 101
        for num in nums:
            count[num] += 1
            sum += num

        num = 100
        x = 0
        while x <= sum - x:
            if count[num] != 0:
                ans.append(num)
                x += num
                count[num] -= 1
            if count[num] == 0:
                num -= 1

        return ans