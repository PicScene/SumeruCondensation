'''
Author: 七画一只妖
Date: 2022-04-24 22:19:19
LastEditors: 七画一只妖
LastEditTime: 2022-04-24 22:26:45
Description: file content
'''
class Solution:
    def binaryGap(self, n: int) -> int:
        last, ans, i = -1, 0, 0
        while n:
            if n & 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
            n >>= 1
            i += 1
        return ans

a = Solution
print(a.binaryGap(a, 22))