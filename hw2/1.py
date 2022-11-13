matrix = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]
"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/
O(len(matrix)^2)
"""

def count_squares(matrix):
    new_matrix = []
    res = 0
    for i in range(len(matrix) - 1):
        new_matrix.append([0] * len(matrix[i]))
        if matrix[i][-1] == 1:
            new_matrix[i][-1] = 1
            res += 1

    new_matrix.append(matrix[-1])
    res += matrix[-1].count(1)
    for i in range(len(new_matrix) - 1, 0, -1):
        for j in range(len(new_matrix[i]) - 1, 0, -1):
            if matrix[i - 1][j - 1] == 1:
                new_matrix[i - 1][j - 1] = min(new_matrix[i][j], new_matrix[i - 1][j], new_matrix[i][j - 1]) + 1
                res += new_matrix[i - 1][j - 1]
    return res


if __name__ == '__main__':
    count_squares(matrix)
