'''
Author: 七画一只妖
Date: 2022-09-04 09:05:41
LastEditors: 七画一只妖
LastEditTime: 2022-09-04 09:18:54
Description: file content
'''
class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
            rows_sum = [sum(row) for row in mat]
            cols_sum = [sum(col) for col in zip(*mat)]
            res = 0
            for i, row in enumerate(mat):
                for j, x in enumerate(row):
                    if x == 1 and rows_sum[i] == 1 and cols_sum[j] == 1:
                        res += 1
            return res



a = Solution
print(a.numSpecial(a,[[1,0,0],
            [0,0,1],
            [1,0,0]]))