'''
Author: 七画一只妖
Date: 2022-07-24 09:50:27
LastEditors: 七画一只妖
LastEditTime: 2022-07-24 10:23:02
Description: file content
'''
class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        n = len(distance)
        i = start
        j = start

        a = 0
        b = 0

        while i != destination:
            a += distance[i]
            i += 1
            if i == n:
                i = 0
        while j != destination:
            j -= 1
            if j < 0:
                j = n - 1
            b += distance[j]
        return min(a, b)