'''
Author: 七画一只妖
Date: 2022-04-04 12:35:11
LastEditors: 七画一只妖
LastEditTime: 2022-04-04 13:40:24
Description: file content
'''
class NumArray(object):

    def __init__(self, nums:list[int]):
        """
        :type nums: List[int]
        """
        n = len(nums)
        size = int(n ** 0.5)
        sums = [0] * ((n + size - 1) // size)  # n/size 向上取整
        for i, num in enumerate(nums):
            sums[i // size] += num
        self.nums = nums
        self.sums = sums
        self.size = size



    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.sums[index // self.size] += val - self.nums[index]
        self.nums[index] = val



    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        m = self.size
        b1, b2 = left // m, right // m
        if b1 == b2:  # 区间 [left, right] 在同一块中
            return sum(self.nums[left:right + 1])
        return sum(self.nums[left:(b1 + 1) * m]) + sum(self.sums[b1 + 1:b2]) + sum(self.nums[b2 * m:right + 1])



# Your NumArray object will be instantiated and called as such:
# numArray = NumArray([1, 3, 5])
# numArray.sumRange(0, 2)
# numArray.update(1, 2)
# numArray.sumRange(0, 2)