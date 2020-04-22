#! python3
# -*- coding:UTF-8 -*-
"""
# 76. Minimum Window Substring
# Created on 2020/4/22 9:06
# minWindow
# @author: ChangFeng
"""
import sys
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        left = right = valid = start = 0
        l = sys.maxsize
        while right < len(s):
            # 将要进入窗口的字符
            c = s[right]
            # 窗口右移
            right += 1
            # 更新窗口内数据
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # 判断是否要收缩窗口
            while valid == len(need):
                # 更新结果集
                if right - left < l:
                    start = left
                    l = right - left
                # 将要移除窗口的字符
                d = s[left]
                # 收缩窗口
                left += 1
                # 更新窗口内数据
                if d in need:
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if l == sys.maxsize else s[start:start + l]


def main():
    src = "ADOBECODEBANC"
    target = "ABC"
    print(Solution().minWindow(src, target))


if __name__ == '__main__':
    main()
