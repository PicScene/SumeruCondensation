'''
Author: 七画一只妖
Date: 2022-03-29 22:18:19
LastEditors: 七画一只妖
LastEditTime: 2022-03-29 22:33:44
Description: file content
'''
class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        def get_cnt(ch):
            n, ans = len(answerKey), 0
            i, j, cnt = 0, 0, 0
            while i < n:
                # 外循环：右指针向右移动
                if answerKey[i] == ch:
                    cnt += 1
                while cnt > k:
                    # 外循环：左指针向右移动（最大值受保护）
                    if answerKey[j] == ch:
                        cnt -= 1
                    j += 1
                ans = max(ans, i - j + 1)
                i += 1
            return ans
        return max(get_cnt('T'), get_cnt('F'))


a = Solution
print(a.maxConsecutiveAnswers(a,"TTFF",2))