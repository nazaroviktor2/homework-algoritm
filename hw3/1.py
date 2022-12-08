from typing import List

matrix = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

"""
https://leetcode.com/problems/number-of-enclaves/
острова из которого нельзя выйти за приделы карты
O(len(matrix))
"""


def numEnclaves(grid: List[List[int]]) -> int:
    stack = {(0, 0)}
    for i in range(len(grid)):
        stack.add((i,0))
        stack.add((i,len(grid[i])-1))
    for i in range(len(grid[0])):
        stack.add((len(grid)-1,i))
        stack.add((0,i))
    while stack:
        i,j = stack.pop()
        if grid[i][j] == 1:
            grid[i][j] = 0
            if len(grid) > i+1:
                stack.add((i+1,j))
            if len(grid[i]) > j+1:
                stack.add((i,j+1))
            if 0 <= i-1:
                stack.add((i-1,j))
            if 0 <= j-1:
                stack.add((i,j-1))
    su = 0
    for i in grid:
        su += sum(i)
    return su

print(numEnclaves([[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0, 0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1, 1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1, 1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[ 0,0,0,0,1,1,0,0,0,1]]))

