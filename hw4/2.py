"""
https://leetcode.com/problems/trim-a-binary-search-tree/description/
Сделать так чтобы в БИНАРНОМ дереве осталось только значение low<val<hight
O(n)
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        def trim(root, low, high):
            if root is None:
                return None
            if root.val < low:# если уже меньше то нет смысла брать левое дерево так как там все еще меньше
                return trim(root.right, low, high)
            elif root.val > high:# если уже больше то нет смысла брать правое дерево так как там все еще больше
                return trim(root.left, low, high)
            else:
                root.left = trim(root.left, low, high)
                root.right = trim(root.right, low, high)
                return root
        return trim(root, low, high)