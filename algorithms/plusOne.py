#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/31 9:21
# plusOne
# @author: ChangFeng
"""
from typing import List


class Solution:

    def plusOne2(self, digits: List[int]) -> List[int]:
        return [int(d) for d in str(int(''.join([str(i) for i in digits])) + 1)]

    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        a = 1
        for i in range(len(digits) - 1, -1, -1):
            if not a:
                return digits
            if digits[i] < 9:
                digits[i] += a
                a = 0
            else:
                digits[i] = 0
        return [1] + digits


def main():
    test_case = [1, 9, 8]
    print(Solution().plusOne(test_case))
    test_case = [1, 2, 3]
    print(Solution().plusOne(test_case))
    test_case = [4, 3, 2, 1]
    print(Solution().plusOne(test_case))
    test_case = [9, 9, 9]
    print(Solution().plusOne(test_case))
    test_case = [0]
    print(Solution().plusOne(test_case))


if __name__ == '__main__':
    main()
