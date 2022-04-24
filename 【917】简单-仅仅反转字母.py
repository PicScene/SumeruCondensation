'''
Author: 七画一只妖
Date: 2022-02-23 09:36:53
LastEditors: 七画一只妖
LastEditTime: 2022-02-23 09:40:29
Description: file content
'''
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        left, right = 0, len(ans) - 1 # 左右指针位置
        while True:
            while left < right and not ans[left].isalpha():  # 判断左边是否扫描到字母
                left += 1
            while right > left and not ans[right].isalpha():  # 判断右边是否扫描到字母
                right -= 1
            if left >= right: # 左右指针相遇，结束循环
                break
            ans[left], ans[right] = ans[right], ans[left] # 交换位置

            # 左右指针同时往内走准备下一个循环
            left += 1
            right -= 1
        return ''.join(ans)
