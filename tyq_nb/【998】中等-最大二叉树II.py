'''
Author: 七画一只妖
Date: 2022-08-30 09:36:03
LastEditors: 七画一只妖
LastEditTime: 2022-08-30 10:32:24
Description: file content
'''
# Definition for a binary tree node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node: TreeNode = TreeNode(val=val)
        # prev = None  # 假设目标位置的父节点
        # cur = root # 目标位置的原节点(左挪)

        prev = None
        cur = root

        # cur = TreeNode(val = max(filter(None, root)))
        # print(filter(None, root))

        # 当val不是最大值时，循环将较大值放在目标父节点，
        while cur != None & cur.val > val:
            prev = cur
            cur = cur.right  # 将目标转移到下一个右子树
            # 目标不可能是左子树，因为val是nums的最后一个元素，递归构建时，val只可能出现在右子树
            # 若出现在左子树，则代表nums中val后面还有元素，这与题意不符

        # 第一步循环时找不到值比val大作为父节点的节点，直接当val为根节点，原树挂在左子树即可
        if prev == None:
            node.left = cur
            return node
        else:
            prev.right = node
            node.left = cur
            return root
        # parent, cur = None, root
        # while cur:
        #     if val > cur.val:
        #         if not parent:
        #             return TreeNode(val, root, None)
        #         node = TreeNode(val, cur, None)
        #         parent.right = node
        #         return root
        #     else:
        #         parent = cur
        #         cur = cur.right
        
        # parent.right = TreeNode(val)
        # return root



def build(root, tree, i):
    if i < len(tree):
        if tree[i] == '+':
            return None
        root = TreeNode(tree[i])
        root.left = build(root.left, tree, 2 * i + 1)
        root.right = build(root.right, tree, 2 * i + 2)
        return root

        
node = TreeNode
tree = [4, 1, 3, None, None, 2]


root = build(None, tree, 0)

a = Solution
print(a.insertIntoMaxTree(a, root=root, val=5))
