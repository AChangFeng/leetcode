#! python3
# -*- coding:UTF-8 -*-
"""
# 32. Longest Valid Parentheses
# Created on 2020/5/14 18:43
# longestValidParentheses
# @author: ChangFeng
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        brute force
        TLE
        """
        res = 0
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1, 2):
                if self.validParentheses(s[i:j]):
                    res = max(res, j - i)
        return res

    def validParentheses(self, ss):
        stack = []
        for x in ss:
            if not stack or x == '(' or stack[-1] != '(':
                stack.append(x)
            elif stack[-1] == '(' and x == ')':
                stack.pop()
        return len(stack) == 0

    def longestValidParentheses(self, s: str) -> int:
        """
        stack
        @see https://leetcode.com/problems/longest-valid-parentheses/discuss/14126/My-O(n)-solution-using-a-stack
        """
        res = 0
        stack = [-1]
        for i, v in enumerate(s):
            if v == "(":
                stack.append(i)
            else:
                top = stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, top - stack[-1])
        return res

    def longestValidParentheses(self, s: str) -> int:
        """
        count
        """
        res, left, right = 0, 0, 0
        for x in s:
            if x == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, right * 2)
            elif right > left:
                left, right = 0, 0

        left, right = 0, 0
        for x in reversed(s):
            if x == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, right * 2)
            elif right > left:
                left, right = 0, 0
        return res

    def longestValidParentheses(self, s: str) -> int:
        """
        @see https://leetcode.com/problems/longest-valid-parentheses/discuss/14126/My-O(n)-solution-using-a-stack
        """
        res = l = _sum = 0
        for x in s:
            if x == '(':
                _sum += 1
            else:
                _sum -= 1
            if _sum < 0:
                l = _sum = 0
            else:
                l += 1
                if _sum == 0:
                    res = max(res, l)
        l = _sum = 0
        for i in range(len(s) - 1, 0, -1):
            x = s[i]
            if x == ')':
                _sum += 1
            else:
                _sum -= 1
            if _sum < 0:
                l = _sum = 0
            else:
                l += 1
                if _sum == 0:
                    res = max(res, l)
        return res


def main():
    print(Solution().longestValidParentheses("((())"))  # 4
    print(Solution().longestValidParentheses("(()"))  # 2
    print(Solution().longestValidParentheses(")()())"))  # 4


if __name__ == '__main__':
    main()
