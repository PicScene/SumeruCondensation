'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-07-27 09:06:41
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-07-27 09:35:43
FilePath: \SumeruCondensation\tyq_nb\【2500】简单-删除每行中的最大值.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution(object):
    def deleteGreatestValue(self, grid:list[list]):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # resp = 0
        # for item in grid:
        #     item.sort()
        # l = len(grid[0])
        # for _ in range(l):
        #     max_list = []
        #     for item2 in grid:
        #         max_list.append(item2[-1])
        #         item2.pop()
        #     resp += max(max_list)
        # return resp
        return sum(max(col) for col in zip(*(sorted(col) for col in grid)))





a = Solution()
print(a.deleteGreatestValue([[1,2,4],[3,3,1]]))