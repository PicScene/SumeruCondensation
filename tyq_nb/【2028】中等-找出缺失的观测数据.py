'''
Author: 七画一只妖
Date: 2022-03-27 20:04:55
LastEditors: 七画一只妖
LastEditTime: 2022-03-27 20:27:22
Description: file content
'''
class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        total_ab = (len(rolls) + n) * mean # 总和
        total_a = sum(rolls) # 已知和
        total_b = total_ab - total_a # 待知和

        # 计算total_b取值范围
        min_b = n
        max_b = 6 * n

        # 判断total_b是否在范围内
        if total_b < min_b or total_b > max_b:
            return []
        else:
            # 将total_b分摊到长度为n的数组中，每个元素的范围在[1, 6]
            # 分摊后的数组
            shang,yushu = divmod(total_b, n)
            ans = [shang + 1] * yushu + [shang] * (n - yushu)
        return ans



a = Solution
print(a.missingRolls(a,[3,2,4,3],4,2))