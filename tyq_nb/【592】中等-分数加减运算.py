'''
Author: 七画一只妖
Date: 2022-07-27 10:31:20
LastEditors: 七画一只妖
LastEditTime: 2022-07-27 10:46:43
Description: file content
'''
import math
from turtle import down
class Solution:
    def fractionAddition(self, expression: str) -> str:
        up, down = 0, 1  # 分子，分母
        i, n = 0, len(expression)
        while i < n:
            # 读取分子，sing用于判断正负
            up1, sign = 0, 1
            # 判断是否为符号位，当符号为负时，符号标志sign记作-1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                up1 = up1 * 10 + int(expression[i])
                i += 1

            # 变换符号
            up1 = sign * up1
            i += 1

            # 读取分母
            down1 = 0
            while i < n and expression[i].isdigit():
                down1 = down1 * 10 + int(expression[i])
                i += 1
            #分子分母相加
            up = up * down1 + up1 * down
            down *= down1
        # 分子为0
        if up == 0:
            return "0/1"
        # 计算公约数g
        g = math.gcd(abs(up), down)
        return str(up // g) + "/" + str(down // g)