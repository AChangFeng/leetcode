#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""


class Solution:
    cl = set()

    def sumSubseqWidths(self, l):
        # print(l)
        if len(l) == 1:
            return 0
        ls = tuple(l)
        if ls in self.cl:
            return 0
        self.cl.add(ls)
        sum_width = self.list_width(l)
        for i in range(len(l)):
            tl = l.copy()
            tl.pop(i)
            sum_width += self.sumSubseqWidths(tl)
        print(str(l) + ": " + str(sum_width))
        return sum_width

    def list_width(self, l):
        return max(l) - min(l)


def main():
    l = [2, 1, 3, 4, 4, 4, 4]
    print(Solution().sumSubseqWidths(l))


if __name__ == '__main__':
    main()
