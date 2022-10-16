""""
https://leetcode.com/problems/count-of-matches-in-tournament/
посчитать количество сыгранных матчей в турнирной сетки
сложность ~ O(log(n)), n - количество команд
"""


def count_matches(teams):
    count = 0
    while teams > 1:
        if teams % 2 == 0:
            count += teams // 2
            teams //= 2
        else:
            count += (teams - 1) // 2
            teams = (teams - 1) // 2 + 1

    return count


if __name__ == '__main__':
    print(count_matches(14))
