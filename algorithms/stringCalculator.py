#! python3
# -*- coding: utf-8 -*-
"""
# Created on Aug-13-19 15:49
# stringCalculator.py
# @author: ChangFeng
"""


class Solution:
    def calculate(self, s):
        stack = []
        result = 0
        number = 0
        sign = 1
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c == '+':
                result += sign * number
                number = 0
                sign = 1
            elif c == '-':
                result += sign * number
                number = 0
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ')':
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
        if number != 0:
            result += sign * number
        return result


def main():
    s = Solution()
    r = s.calculate('2-(5-6)')
    print(r)


if __name__ == '__main__':
    main()