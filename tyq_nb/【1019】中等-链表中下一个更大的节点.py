'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-10-18 18:47:56
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-10-18 19:29:34
FilePath: \SumeruCondensation\tyq_nb\【1019】中等-链表中下一个更大的节点.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List, Optional

from sqlalchemy import null


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        st = []
        cur = head
        while cur:
            res.append(0)
            cur_idx = len(res) - 1
            while len(st) > 0 and cur.val > st[-1][0].val:
                node, idx = st.pop()
                res[idx] = cur.val
            st.append((cur, cur_idx))
            cur = cur.next
        return res


a = Solution
print(a.nextLargerNodes(a,[2,1,5]))