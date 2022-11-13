"""
https://leetcode.com/problems/house-robber-ii/
так как первый и последний дом связаны между собой то надо проверить 2 случая
nums[1:] and nums[:-1]
O(len(nums))
"""


def rob(nums):
    def check(nums):
        rob = 0
        not_rob = 0
        for num in nums:
            rob, not_rob = not_rob + num, max(rob, not_rob)
        return max(rob, not_rob)

    if len(nums) == 1:
        return nums[0]
    elif not nums:
        return 0
    else:
        return max(check(nums[1:]), check(nums[:-1]))

print(rob([2,3,2]))