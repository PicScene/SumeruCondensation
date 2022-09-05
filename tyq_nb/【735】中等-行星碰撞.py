'''
Author: 七画一只妖
Date: 2022-07-13 08:53:36
LastEditors: 七画一只妖
LastEditTime: 2022-07-13 09:42:17
Description: file content
'''
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        resp = []

        for item in asteroids:
            alive = True
            while alive and item < 0 and resp and resp[-1] > 0:
                alive = -item > resp[-1] # True=比当前大，干飞当前的，还存活
                if -item >= resp[-1]: # 需要爆炸的情况
                    resp.pop()
            if alive:
                resp.append(item)
            # if resp == []:
            #     resp.append(item)
            #     continue

            # if resp[-1] < 0: # 栈顶元素向左走，对后面的元素没影响
            #     resp.append(item)
            #     continue

            # if resp[-1] > 0:
            #     if item < 0: # 当前会碰撞
            #         if -item < resp[-1]:
            #             continue
            #         elif -item == resp[-1]:
            #             resp.pop()
            #             continue
            #         elif -item > resp[-1]:
            #             resp.pop()
            #             flag = False
            #             while resp != [] and resp[-1] > 0:
            #                 if -item < resp[-1]:
            #                     flag = True
            #                     break
            #                 elif -item == resp[-1]:
            #                     resp.pop()
            #                     flag = True
            #                     break
            #                 elif -item > resp[-1]:
            #                     resp.pop()
            #                     continue
            #             if not flag:
            #                 resp.append(item)
            #     else:
            #         resp.append(item)
        return resp


a = Solution
print(a.asteroidCollision(Solution,[-2,2,1,-2]))