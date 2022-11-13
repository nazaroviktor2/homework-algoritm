"""
https://leetcode.com/problems/get-maximum-in-generated-array/
есть две формулы
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
найти макс в массиве
O(n) - где n входное число
"""


def getMaximumGenerated(n):
    if n == 0:
        return  0
    nums = [0]*(n+1)
    nums[1] = 1
    for i in range(1,n+1//2):
        if 2 <= 2 * i <= n:
            nums[2 * i ] = nums[i]
        if 2 <= 2 * i + 1 <= n:
            nums[2 * i + 1] = nums[i] + nums[i + 1]

    return max(nums)


print(getMaximumGenerated(2))


