'''
Author: 七画一只妖
Date: 2022-09-19 11:20:24
LastEditors: 七画一只妖
LastEditTime: 2022-09-19 11:20:54
Description: file content
'''
from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        nums.sort(key=lambda x: (cnt[x], -x))
        return nums