#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""
import sys


class Solution:
    def shortestToChar(self, S, C):
        prev = -sys.maxsize
        ans = []
        for i, v in enumerate(S):
            if v == C:
                prev = i
            ans.append(i - prev)

        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return ans


def main():
    print(Solution().shortestToChar('loveleetcode', 'e'))


if __name__ == '__main__':
    main()
