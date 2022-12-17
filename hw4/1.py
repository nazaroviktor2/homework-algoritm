"""
https://leetcode.com/problems/maximum-length-of-pair-chain/description/
сортируем стулья
находим саммую длинную цепочку
O(n*log(n))
"""

class Solution:
    def findLongestChain(self, pairs):

        pairs.sort(key=lambda x: x[0])
        pair = pairs.pop()[0]
        res = 1
        while pairs:
            mi, ma = pairs.pop()
            if ma < pair:
                res += 1
                pair = mi
        return res