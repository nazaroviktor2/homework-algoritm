"""
https://leetcode.com/problems/jewels-and-stones/
подсчитать сколько наших камней драгоцены
сложность ~ O(n)
"""


def num_jewels_in_stones(jewels, stones):
    count = 0
    for stone in stones:
        if stone in jewels:  # если наш камень есть в драгоценностят то он драгоценность
            count += 1
    return count


if __name__ == '__main__':
    print(num_jewels_in_stones("z", "aAAbbbb"))
