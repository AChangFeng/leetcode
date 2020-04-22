#! python3
# -*- coding:UTF-8 -*-
"""
# 72. Edit Distance
# Levenshtein distance
# Created on 2020/4/22 15:57
# minDistance
# @author: ChangFeng
"""
import sys


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        backtracking
        TLE
        """
        ans = sys.maxsize

        def backtrack(i, j, edist):
            nonlocal ans
            if i == len(word1) or j == len(word2):
                if i < len(word1):
                    edist += (len(word1) - i)
                if j < len(word2):
                    edist += (len(word2) - j)
                ans = min(ans, edist)
            if word1[i] == word2[j]:
                backtrack(i + 1, j + 1, edist)
            else:
                # 删除a[i]、或者在b[j]前面添加字符a[i]
                backtrack(i + 1, j, edist + 1)
                # 删除b[j]、或者在a[i]前面添加字符b[j]
                backtrack(i, j + 1, edist + 1)
                # 替换a[i]和b[j]
                backtrack(i + 1, j + 1, edist + 1)

        backtrack(0, 0, 0)
        return ans

    def minDistance(self, word1: str, word2: str) -> int:
        """
        dynamic program
        如果：a[i]!=b[j]，那么：min_edist(i, j)就等于：min(min_edist(i-1,j)+1, min_edist(i,j-1)+1, min_edist(i-1,j-1)+1)
        如果：a[i]==b[j]，那么：min_edist(i, j)就等于：min(min_edist(i-1,j)+1, min_edist(i,j-1)+1，min_edist(i-1,j-1))
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        n, m = len(word1), len(word2)
        dp = [[0 for _ in range(m)] for _ in range(n)]
        # first row
        for j in range(m):
            if word2[j] == word1[0]:
                dp[0][j] = j
            elif j != 0:
                dp[0][j] = dp[0][j - 1] + 1
            else:
                dp[0][j] = 1
        # first column
        for i in range(n):
            if word1[i] == word2[0]:
                dp[i][0] = i
            elif i != 0:
                dp[i][0] = dp[i - 1][0] + 1
            else:
                dp[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                if word1[i] == word2[j]:
                    dp[i][j] = min([dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1]])
                else:
                    dp[i][j] = min([dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1])
        return dp[n - 1][m - 1]


def main():
    pass


if __name__ == '__main__':
    main()
