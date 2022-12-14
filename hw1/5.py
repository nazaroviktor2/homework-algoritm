import heapq

"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
найти к-ый наибольший элемент в массиве 
реализация за O(n) возможна с использованием приорететной очереди
о приорететной очереди прочитал на :
https://pythobyte.com/python-priority-queue-85409/#:~:text=%D0%9F%D1%80%D0%B8%D0%BE%D1%80%D0%B8%D1%82%D0%B5%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D1%87%D0%B5%D1%80%D0%B5%D0%B4%D1%8C%20%D0%B2%20Python%20%D0%B8%D0%BB%D0%B8%20%D0%BB%D1%8E%D0%B1%D0%BE%D0%BC%20%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%BC%20%D1%8F%D0%B7%D1%8B%D0%BA%D0%B5%2D%D1%8D%D1%82%D0%BE%20%D0%BE%D1%81%D0%BE%D0%B1%D1%8B%D0%B9,%D1%81%20%D0%B8%D1%85%20%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BA%D0%BE%D0%BC%20%D0%B2%20%D0%BE%D1%87%D0%B5%D1%80%D0%B5%D0%B4%D0%B8.
потом открыл документацию модуля heapq
там есть метод который выполняет нужную задачу и использовал его 
"""


def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

if __name__ == '__main__':

    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
