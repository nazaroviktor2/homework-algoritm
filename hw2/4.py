"""
https://leetcode.com/problems/best-sightseeing-pair/
надо найти максмальное сумму из пар цен достопримечательностей по формуле
values[i] + values[j] + i - j
O(n)

"""


def maxScoreSightseeingPair(values):
    current = 0
    max_value = 0
    for i in range(1, len(values)):
        current = max(current, values[i - 1] + i - 1)
        max_value = max(max_value, current + values[i] - i)

    return max_value
