'''
Author: 七画一只妖
Date: 2022-08-25 10:36:12
LastEditors: 七画一只妖
LastEditTime: 2022-08-25 10:52:30
Description: file content
'''
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        size = 0
        for _ in arr:
            size += 1
        left = 0
        right = size - 1

        #需要排除元素的个数
        pai = size - k

        while pai > 0:
            if x - arr[left] <= arr[right] - x: #条件  
                right -= 1
            else:
                left += 1
            pai -= 1
        return arr[left:left + k] 


a = Solution
print(a.findClosestElements(self = a, arr = [1,2,3,4,5], k = 4, x = 3))