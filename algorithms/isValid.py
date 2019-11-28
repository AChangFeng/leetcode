#! python3
# -*- coding:UTF-8 -*-
"""
# 20. Valid Parentheses
# Created on 2019/11/28 17:15
# isValid
# @author: ChangFeng
"""


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', ']': '[', '}': '{'}
        if not s:
            return True
        stack = []
        for c in s:
            # 栈空、元素是左括号或者元素是右括号但栈顶不是对应的左括号，入栈
            if not stack or c in brackets.values() or brackets[c] != stack[-1]:
                stack.append(c)
            else:
                # 否则出栈
                stack.pop()
        return len(stack) == 0


def main():
    test_case = '()'
    print(Solution().isValid(test_case))  # True
    test_case = '()[]{}'
    print(Solution().isValid(test_case))  # True
    test_case = '(]'
    print(Solution().isValid(test_case))  # False
    test_case = '([)]'
    print(Solution().isValid(test_case))  # False
    test_case = '{[]}'
    print(Solution().isValid(test_case))  # True
    test_case = '[])'
    print(Solution().isValid(test_case))  # False


if __name__ == '__main__':
    main()
