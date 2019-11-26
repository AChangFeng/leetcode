#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""
import collections


class Solution:

    def rearrangeBarcodes(self, packages):
        length = len(packages)
        i = 0
        res = [0] * length
        for k, v in collections.Counter(packages).most_common():
            for _ in range(v):
                res[i] = k
                i = i + 2
                if i >= length:
                    i = 1
        return res


def main():
    test_cases = []
    test_cases.append([1, 1, 1, 2, 2, 2])
    test_cases.append([1, 1, 1, 1, 2, 2, 3, 3])
    for test_case in test_cases:
        print(Solution().rearrangeBarcodes(test_case))


if __name__ == '__main__':
    main()
