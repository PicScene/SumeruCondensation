'''
Author: 七画一只妖
Date: 2022-07-17 09:08:07
LastEditors: 七画一只妖
LastEditTime: 2022-07-17 09:52:32
Description: file content
'''
from re import A


class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            cnt = 0
            while nums[i] < n:
                num = nums[i]
                nums[i] = n
                i = num
                cnt += 1
            ans = maxmax(ans, cnt)
        return ans

def maxmax(a, b):
    return a if a>= b else b


a = Solution
print(a.arrayNesting(Solution, [5,4,0,3,1,6,2]))