"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
перевести односвязный список из 1 и 0 в число в 10 системе 
O(n)
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(self, head):
    """
    :type head: ListNode
    :rtype: int
    """
    s=0
    while head:
        s*=2
        s += head.val
        head=head .next
    return s