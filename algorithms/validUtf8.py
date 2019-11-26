#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""


class Solution:
    def validUtf8(self, data) -> bool:
        n_byte = 0
        for i in data:
            i = i & 255
            print(bin(i))
            if n_byte == 0:
                # check if i is first byte
                n_byte = self.getNBytes(i)
                if not n_byte:
                    return False
                n_byte -= 1
            else:
                # check if i is a part of an existing UTF-8 character
                if not self.isRemain(i):
                    return False
                n_byte -= 1
        return n_byte == 0

    def getNBytes(self, i) -> int:
        # start with 0
        if not (i & (1 << 7)):
            return 1
        mask = 1 << 7
        b_byte = 0
        while mask & i:
            b_byte += 1
            mask = mask >> 1
        # UTF8 char cant be start with 1XXXXXXX and cant start with 11111000
        if b_byte == 1 or b_byte > 4:
            return 0
        return b_byte

    def isRemain(self, i) -> bool:
        mask1 = 1 << 7
        mask2 = 1 << 6
        if i & mask1 and (not (i & mask2)):
            return True
        return False


def main():
    # testcase1 = [145] #False
    # print(Solution().validUtf8(testcase1))
    # testcase2 = [197, 130, 1]  # True
    # print(Solution().validUtf8(testcase2))
    # testcase3 = [235, 140, 4]  # False
    # print(Solution().validUtf8(testcase3))
    testcase3 = [250, 145, 145, 145, 145]  # False
    print(Solution().validUtf8(testcase3))


if __name__ == '__main__':
    main()
