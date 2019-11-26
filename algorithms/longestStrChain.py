#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""


class Solution:
    def longestStrChain(self, words):
        words = sorted(words, key=len)
        dp = {}
        for word in words:
            dp[word] = max(dp.get(word[:i] + word[i + 1:], 0) + 1 for i in range(len(word)))
        return max(dp.values())


def main():
    testcase = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(Solution().longestStrChain(testcase))


if __name__ == '__main__':
    main()
