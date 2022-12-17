"""
https://leetcode.com/problems/delete-operation-for-two-strings/description/
O(n*m)
"""


def out(arr):
    for i in arr:
        print(i)
class Solution(object):
    def minDistance(self, word1, word2):

        word1_len = len(word1)
        word2_len = len(word2)
        dp = [[0 for _ in range(word2_len+1)] for _ in range(word1_len+1)]
        for i in range(word1_len+1):


            for j in range(word2_len+1):
                #print("_________________-")
                #out(dp)
                if i == 0 and j == 0:  # Если строки пустые
                    #print(1)
                    dp[i][j] = 0
                elif i == 0:  # Левый вертикальный край
                    #print(2)
                    dp[i][j] = dp[i][j-1]+1
                elif j == 0:  # Верхний горизонтальный край
                    #print(3)
                    dp[i][j] = dp[i-1][j]+1
                elif word1[i - 1] == word2[j - 1]:  # Когда буквы в словах совпадают
                    dp[i][j] = dp[i-1][j-1]
                    #print(4)
                else:  # Когда буквы в словах не совпали
                    #print(5)
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1
        return dp[word1_len][word2_len]

Sol = Solution()

print(Sol.minDistance("set","eat"))