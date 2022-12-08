from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.dic = dict()

        def tree_len(root, h):
            stack = {(root, h)}
            while stack:
                rt, i = stack.pop()
                if rt:
                    if i in self.dic:
                        self.dic[i] += [rt.val]
                    else:
                        self.dic[i] = [rt.val]

                    stack.add((rt.left, i + 1))
                    stack.add((rt.right, i + 1))

        tree_len(root, 1)
        res = []
        for key in sorted(self.dic.keys()):
            res.append(round(sum(self.dic[key]) / len(self.dic[key]), 6))
        return res


