#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""
from functools import reduce


class Solution:
    def minDominoRotations(self, a, b) -> int:
        length = len(a)
        # 元素最多有6个
        ele = [0] * 6
        for x, y in zip(a, b):
            # x
            ele[x - 1] = ele[x - 1] + 1
            # y
            ele[y - 1] = ele[y - 1] + 1
            if x == y:
                ele[x - 1] = ele[x - 1] - 1
        possible_value = None
        for i, v in enumerate(ele):
            if v >= length:
                possible_value = i + 1
        if not possible_value:
            return -1
        av = a.count(possible_value)
        bv = b.count(possible_value)
        return length - av if av > bv else length - bv

    def minDominoRotations1(self, a, b):
        # 如果x出现在a中出现的次数加上x在b中出现的次数减去在ab中同时出现的次数等于a,b的长度 则说明有解
        # 又ab元素共有2*len个元素说明只有一个这样的数
        # 所以我们只需要在a,b中哪个集合中x出现的次数最少，用这个最少的次数减去同时出现的次数即为所求
        ca = [0] * 6
        cb = [0] * 6
        cs = [0] * 6
        for index, entry in enumerate(zip(a, b)):
            x = entry[0]
            y = entry[1]
            ca[x - 1] = ca[x - 1] + 1
            cb[y - 1] = cb[y - 1] + 1
            if x == y:
                cs[x - 1] = cs[x - 1] + 1

        for x in range(1, 7):
            x = x - 1
            if ca[x] + cb[x] - cs[x] == len(a):
                return min(ca[x], cb[x]) - cs[x]
        return -1

    def minDominoRotation2(self, a, b):
        s = reduce(set.__and__, [set(d) for d in zip(a, b)])
        if not s:
            return -1
        x = s.pop()
        return min(len(a) - a.count(x), len(a) - b.count(x))


def main():
    a = [3, 5, 1, 2, 3]
    b = [3, 3, 3, 3, 4]
    result = Solution().minDominoRotations(a, b)
    print(result)


if __name__ == '__main__':
    main()
