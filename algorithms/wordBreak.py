#! python3
# -*- coding:UTF-8 -*-
"""
# 139. Word Break
# Created on 2020/3/30 19:15
# wordBreak
# @author: ChangFeng
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dynamic program
        f[i] stands for whether subarray(0, i) can be segmented into words from the dictionary.
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        word_set = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        word_set = set(wordDict)

        len_set = set()
        for w in wordDict:
            len_set.add(len(w))

        for i in range(len(s)):
            if dp[i]:
                for j in len_set:
                    if i + j <= len(s) and not dp[i + j] and s[i:i + j] in word_set:
                        dp[i + j] = True
        return dp[-1]


def main():
    test_case = ["leetcode", ["leet", "code"]]
    print(Solution().wordBreak(*test_case))


if __name__ == '__main__':
    main()
