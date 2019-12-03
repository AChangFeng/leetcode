#! python3
# -*- coding:UTF-8 -*-
"""
# 338. Counting Bits
# Created on 2019/12/3 9:31
# countBits
# @author: ChangFeng
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        """
        dynamic program
        the total number of 1 bits = the last bit is 1 ? 1 : 0 + the number of the prefix 1 bits(exclude the last bit)
        :param num:
        :return:
        """
        ans = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


def main():
    pass


if __name__ == '__main__':
    main()
