'''
Author: 七画一只妖
Date: 2022-04-25 20:09:08
LastEditors: 七画一只妖
LastEditTime: 2022-04-25 20:41:27
Description: file content
'''
from collections import defaultdict
from random import choice


class Solution:

    def __init__(self, nums: list[int]):
        # defaultdict ：一个会为空值设置默认值以避免keyError异常的dict子类
        self.pos = defaultdict(list)
        # enumerate ：将可迭代迭代对象转成下标+对象的组合
        for i, num in enumerate(nums):
            self.pos[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.pos[target])



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)