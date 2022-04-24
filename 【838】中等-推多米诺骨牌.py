'''
Author: 七画一只妖
Date: 2022-02-21 12:07:36
LastEditors: 七画一只妖
LastEditTime: 2022-02-21 12:51:33
Description: file content
'''

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        # 思路：
        #      总共四种情况  L.....L => LLLLLLL
        #                   L.....R => L.....R
        #                   R.....L => RRR.LLL 或者 RRRLLL
        #                   R.....R => RRRRRRR
        # 举例：     .L.R...LR..L..
        #              首尾添加LR=> L.L.R...LR..L..R
        #                一番操作=> LLL.RR.LLRRLL..R
        #              首尾减去LR=>  LL.RR.LLRRLL..
        dominoes = "L" + dominoes + "R" # 首尾加上不会影响的力
        res = []
        l = 0

        for r in range(1, len(dominoes)):
            # 为 .     过，继续下一循环
            if dominoes[r] == '.':
                continue

            mid = r - l - 1 # 算出此时单位时间，左右指针中间有多少个位置

            if l: # 虚拟的牌不放入结果
                res.append(dominoes[l])

            # 处理情况：L...L 或者 R...R
            if dominoes[l] == dominoes[r]:
                # 使用 L或者R 覆盖这个区域
                res.append(dominoes[l] * mid) 

            elif dominoes[l] == 'L' and dominoes[r] == 'R':
                # 使用 . 覆盖这个区域
                res.append('.' * mid) 
            else:
                # 往中间坍缩，若位置为偶数，则没有.  若为奇数，则有一个 . 
                res.append('R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2))
            l = r
        return "".join(res)


a = Solution
print(a.pushDominoes(a,".L.R...LR..L.."))