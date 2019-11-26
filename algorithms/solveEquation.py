#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""


class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        left_arr = self.parse(left)
        right_arr = self.parse(right)
        # x to left digit to right
        l = []
        r = []
        for x in left_arr + [self.nagate(e) for e in right_arr]:
            if 'x' in x:
                l.append(x[:-1])
            else:
                r.append(self.nagate(x))
        lr = eval(''.join(l)) if l else 0
        rr = eval(''.join(r)) if r else 0
        if not lr:
            return 'Infinite solutions' if not rr else 'No solution'
        return 'x=' + str(int(rr / lr))

    def nagate(self, num):
        if '-' in num:
            return '+' + num[1:]
        else:
            return '-' + num[1:]

    def parse(self, equ):
        result = []
        operand = ''
        op = '+'
        for x in equ:
            if x in '-+':
                if operand:
                    result.append(self.getEle(op, operand))
                op = x
                operand = ''
            else:
                operand += x
        if operand:
            result.append(self.getEle(op, operand))
        return result

    def getEle(self, op, operand):
        if operand == 'x':
            operand = '1x'
        return op + operand


def main():
    _input = "x=x"
    result = Solution().solveEquation(_input)
    print(result)


if __name__ == '__main__':
    main()
