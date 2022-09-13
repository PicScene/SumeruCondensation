'''
Author: 七画一只妖
Date: 2022-09-13 22:01:38
LastEditors: 七画一只妖
LastEditTime: 2022-09-13 22:09:10
Description: file content
'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num
        s = list(str(num))
        for i in range(len(s)):
            for j in range(i):
                s[i], s[j] = s[j], s[i]
                ans = max(ans, int(''.join(s)))
                s[i], s[j] = s[j], s[i]
        return ans


a = Solution
print(a.maximumSwap(a, 2736))