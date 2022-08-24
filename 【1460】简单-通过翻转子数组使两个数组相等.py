'''
Author: 七画一只妖
Date: 2022-08-24 08:36:13
LastEditors: 七画一只妖
LastEditTime: 2022-08-24 08:49:08
Description: file content
'''
from collections import Counter


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)