"""
https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
посчитать количество периодов дней когда prices[i+1] - prices[i] = 1
массив num с длинной len(prices):

num[i] = 1 если prices[i-1] - prices[i] != 1
num[i] = num[i-1] +2 если prices[i-1] - prices[i] == 1

ответ сумма всех элементов списка
O(n), n = len(prices)
"""


def getDescentPeriods(prices):
    num = [1] * len(prices)
    for i in range(1, len(num)):
        if prices[i - 1] - prices[i] == 1:
            num[i] = num[i - 1] + 1

    return sum(num)


print(getDescentPeriods([ 3, 2, 1,4]))
