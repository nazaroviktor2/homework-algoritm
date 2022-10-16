"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
посчитать за какое количество шагов число станет - 0
сложность ~ O(log(n)), n - введеное число
"""


def count_to_zero(num):
    count = 0
    while num != 0:  # пока число не 0
        if num % 2 == 0:  # если число четно то делим на 2
            num //= 2
        else:  # если нечетное
            num -= 1

        count += 1  #  считаем количество шагов
    return count


if __name__ == '__main__':
    print(count_to_zero(14))
    print(count_to_zero(8))
    print(count_to_zero(123))
