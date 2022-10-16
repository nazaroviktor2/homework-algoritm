import heapq

"""
https://leetcode.com/problems/sort-integers-by-the-power-value/
есть две формулы;
if x is even then x = x / 2
if x is odd then x = 3 * x + 1
с помощью этих формул отсортивать числа по силе числа (за сколько шагов число превращается в единицу)
и вывести к-ый элемент в отсортированом массиве
сложность ~
"""


def get_power(num):
    count = 0
    while num > 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        count += 1
    return count


def get_kth(lo, hi, k):
    arr = []
    for i, num in enumerate(range(lo, hi + 1)):

        arr.append((num,get_power(num)))
        power = get_power(num)
    # c помощью приорететной очереди нахоим к-ый наименьший элемент
    power_k = heapq.nsmallest(k, arr, key= lambda x:x[1])[-1]

    return power_k[0]




print(get_kth(10, 20, 5))
"""

def get_kth(lo, hi, k):
    arr_1 = []  # создаем массив элементов
    arr_power = []  # массив сил чисел
    power_to_arr = {}  # словарь где ключ сила чисел и ключ индексы элементов arr_1
    for i, num in enumerate(range(lo, hi + 1)):

        arr_1.append(num)
        power = get_power(num)
        arr_power.append(power)
        if power in power_to_arr.keys():

            power_to_arr[power].append(i)
        else:
            power_to_arr[power] = [i]
    # c помощью приорететной очереди нахоим к-ый наименьший элемент
    print(arr_power)
    print(sorted(arr_power))
    power_k = heapq.nsmallest(k, arr_power)[-1]

    print(heapq.nsmallest(k, arr_power))

    if len(power_to_arr[power_k]) == 1: # если элемент с такой силой только один то вернем его
        return arr_1[power_to_arr[power_k][0]]
    else:
        return arr_1[power_to_arr[power_k][k-1]] # если больше одного ио вернем к-ый


"""