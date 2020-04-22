#! python3
# -*- coding:UTF-8 -*-
"""
# 567. Permutation in String
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""
import datetime
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l2 < l1:
            return False
        s1_dict = {}
        s2_dict = {}
        for i in range(l1):
            s1_dict[s1[i]] = s1_dict.get(s1[i], 0) + 1
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1

        left = 0
        right = l1 - 1
        while right < l2:
            if s1_dict == s2_dict:
                return True
            # left op: count down, if count==0 then del key
            s2_dict[s2[left]] -= 1
            if s2_dict[s2[left]] == 0:
                del s2_dict[s2[left]]
            left += 1
            right += 1
            if right < l2:
                # right op: plus count or init it to 1
                s2_dict[s2[right]] = s2_dict.get(s2[right], 0) + 1
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = defaultdict(int)
        for c in s1:
            need[c] += 1
        window = defaultdict(int)
        left = right = valid = 0
        while right < len(s2):
            c = s2[right]
            # 扩展窗口
            right += 1
            # 更新窗口数据
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            if valid == len(need):
                return True
            # 是否收缩窗口
            while right - left >= len(s1):
                # 更新窗口数据
                d = s2[left]
                # 收缩窗口
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False


def main():
    _input1 = 'ab'
    _input2 = 'eidbaoo'
    now = datetime.datetime.now()
    print(Solution().checkInclusion(_input1, _input2))


if __name__ == '__main__':
    main()
