'''
Author: 七画一只妖
Date: 2022-02-20 10:16:26
LastEditors: 七画一只妖
LastEditTime: 2022-02-21 12:09:44
Description: file content
'''


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        index = 0
        while index < len(bits) - 1:
            if bits[index] == 1:
                index += 2
            elif bits[index] == 0:
                index += 1
            else:
                break

        return index + 1 == len(bits)


a = Solution
print(a.isOneBitCharacter(a,[1,0,0]))