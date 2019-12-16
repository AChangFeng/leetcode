#! python3
# -*- coding:UTF-8 -*-
"""
# 647. Palindromic Substrings
# Created on 2019/12/5 14:39
# countSubstrings
# @author: ChangFeng
"""
from typing import List


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        def expand_center(l,r):
            nonlocal ans
            while l>=0 and r<len(s) and s[l]==s[r]:
                ans+=1
                l-=1
                r+=1
        for i in range(len(s)):
            # odd
            expand_center(i,i)
            # even
            expand_center(i,i+1)
        return ans



def main():
    test_case = 'abc'
    print(Solution().countSubstrings(test_case))
    test_case = 'aaa'
    print(Solution().countSubstrings(test_case))


if __name__ == '__main__':
    main()
