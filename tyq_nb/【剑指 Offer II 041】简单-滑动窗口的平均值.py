'''
Author: 七画一只妖
Date: 2022-07-16 17:16:00
LastEditors: 七画一只妖
LastEditTime: 2022-07-16 17:38:10
Description: file content
'''
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.nums = deque()
        self.sum = 0
        self.changdu = 0


    def next(self, val: int) -> float:
        if self.changdu == self.size:
            self.sum -= self.nums.popleft()
            # self.nums.pop(0) 
            self.changdu -= 1

        self.nums.append(val)
        self.sum += val
        self.changdu += 1
        return self.sum / self.changdu



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)