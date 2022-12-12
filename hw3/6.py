from typing import Optional
"""
https://leetcode.com/problems/diameter-of-binary-tree/description/
O(n)
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def tree_len(node):
            left = 0
            right = 0
            if node.left:
                left = tree_len(node.left)
            if node.right:
                right = tree_len(node.right)
            if left + right > self.diameter:
                self.diameter = left + right
            return 1 + max(left, right)

        tree_len(root)
        return self.diameter

