'''
Author: 七画一只妖
Date: 2022-08-29 09:38:35
LastEditors: 七画一只妖
LastEditTime: 2022-08-29 09:47:42
Description: file content
'''
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res = [0 for _ in range(2 * n)]
        index = 0

        left = 0
        right = n
        while left < n:
            res[index] = nums[left]
            left += 1
            index += 1
            res[index] = nums[right]
            right += 1
            index += 1
        return res




a = Solution
print(a.shuffle(a, nums = [1,2,3,4,4,3,2,1], n = 4))