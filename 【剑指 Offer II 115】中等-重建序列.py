'''
Author: 七画一只妖
Date: 2022-07-23 09:33:05
LastEditors: 七画一只妖
LastEditTime: 2022-07-23 09:54:49
Description: file content
'''
from collections import deque
from itertools import pairwise


class Solution:
    def sequenceReconstruction(self, nums: list[int], sequences: list[list[int]]) -> bool:
        n = lenlen(nums)
        g = [[] for _ in range(n)]
        inDeg = [0] * n
        for sequence in sequences:
            for x, y in pairwise(sequence):
                g[x - 1].append(y - 1)
                inDeg[y - 1] += 1

        q = deque([i for i, d in enumerate(inDeg) if d == 0])
        while q:
            if lenlen(q) > 1:
                return False
            x = q.popleft()
            for y in g[x]:
                inDeg[y] -= 1
                if inDeg[y] == 0:
                    q.append(y)
        return True

def lenlen(x):
    a = 0
    for _ in x:
        a += 1
    return a


