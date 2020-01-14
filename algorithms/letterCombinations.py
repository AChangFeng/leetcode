#! python3
# -*- coding:UTF-8 -*-
"""
# 17. Letter Combinations of a Phone Number
# Created on 2020/1/14 19:25
# letterCombinations
# @author: ChangFeng
"""
from typing import List


class Solution:
    def __init__(self):
        self.d = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        backtracking
        """
        if not digits:
            return []
        ans = []
        n = len(digits)

        def helper(index, path):
            if index == n:
                ans.append("".join(path))
                return

            for v in self.d[digits[index]]:
                helper(index + 1, path + [v])

        helper(0, [])
        return ans

    def letterCombinations(self, digits: str) -> List[str]:
        """
        backtracking
        """
        if not digits:
            return []
        ans = []
        n = len(digits)

        def helper(index, path):
            if index == n:
                ans.append(''.join(path))
                return

            for c in self.d[digits[index]]:
                path.append(c)
                helper(index + 1, path)
                path.pop()

        helper(0, [])
        return ans


def main():
    test_case = "23"
    print(Solution().letterCombinations(test_case))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


if __name__ == '__main__':
    main()
