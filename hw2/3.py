"""
https://leetcode.com/problems/unique-paths-ii/
путь до ячейки[i][j] = ячейка[i][j-1] + ячейка[i-1][j]
O(m*n) m,n- длинны входного массива
"""


def uniquePathsWithObstacles(obstacleGrid):
    nums = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
    nums[0][0] = 1
    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[i])):
            if obstacleGrid[i][j] == 1:

                nums[i][j] = 0
            else:

                if i - 1 >= 0:

                    nums[i][j] += nums[i - 1][j]
                if j - 1 >= 0:

                    nums[i][j] += nums[i][j - 1]

    return nums[len(nums) - 1][len(nums[len(nums) - 1]) - 1]


print(uniquePathsWithObstacles([[0,1],[0,0]]))
