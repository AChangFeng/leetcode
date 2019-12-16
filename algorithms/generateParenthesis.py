#! python3
# -*- coding:UTF-8 -*-
"""
22. Generate Parentheses
# Created on 2019/12/16 19:01
# generateParenthesis
# @author: ChangFeng
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Brute Force
        """
        left_parenthesis = '('
        right_parenthesis = ')'
        parenthesises = (left_parenthesis + right_parenthesis) * n

        ans = []

        def generate(path):
            if len(path) == len(parenthesises):
                if is_well_formed(path):
                    ans.append("".join(path))
                return
            path.append(left_parenthesis)
            generate(path)
            path.pop()
            path.append(right_parenthesis)
            generate(path)
            path.pop()

        def is_well_formed(ss):
            stack = []
            for s in ss:
                if stack and right_parenthesis == s and stack[-1] == left_parenthesis:
                    stack.pop()
                else:
                    stack.append(s)
            return len(stack) == 0

        generate([])
        return ans

    def generateParenthesis(self, n: int) -> List[str]:
        """
        backtracking
        """
        ans = []

        def backtacking(s='', l=0, r=0):
            if len(s) == n * 2 and is_well_formed(s):
                ans.append(s)
            if l < n:
                backtacking(s + "(", l + 1, r)
            if r < n:
                backtacking(s + ")", l, r + 1)

        def is_well_formed(ss):
            stack = []
            for s in ss:
                if stack and ')' == s and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
            return len(stack) == 0

        backtacking()
        return ans

    def generateParenthesis(self, n: int) -> List[str]:
        """
        backtracking
        """
        ans = []

        def backtacking(s='', l=0, r=0):
            if len(s) == n * 2:
                ans.append(s)
            if l < n:
                backtacking(s + "(", l + 1, r)
            # 放置的右括号数量不能大于左括号
            if r < l:
                backtacking(s + ")", l, r + 1)

        backtacking()
        return ans


def main():
    test_case = 3
    print(Solution().generateParenthesis(test_case))


if __name__ == '__main__':
    main()
