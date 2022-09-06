'''
Author: 七画一只妖
Date: 2022-03-24 09:20:22
LastEditors: 七画一只妖
LastEditTime: 2022-03-24 09:32:09
Description: file content
'''
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        # m：行数，n：列数
        m, n = len(img), len(img[0])

        # sum：格子
        sum = [[0] * (n + 10) for _ in range(m + 10)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + img[i - 1][j - 1]

        # ans：当前位置
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 计算单元格
                a, b = max(0, i - 1), max(0, j - 1)
                c, d = min(m - 1, i + 1), min(n - 1, j + 1)
                cnt = (c - a + 1) * (d - b + 1)
                tot = sum[c + 1][d + 1] - sum[a][d + 1] - sum[c + 1][b] + sum[a][b]
                ans[i][j] = tot // cnt
        return ans