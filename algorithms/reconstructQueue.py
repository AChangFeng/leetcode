#! python3
# -*- coding:UTF-8 -*-
"""
# 406. Queue Reconstruction by Height
# Created on 2019/12/4 9:19
# reconstructQueue
# @author: ChangFeng
"""
import os
from typing import List

import requests
from bs4 import BeautifulSoup


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        1. Pick out tallest group of people and sort them in a subarray (S).
        Since there's no other groups of people taller than them,
        therefore each guy's index will be just as same as his k value.
        2.For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
        :param people:
        :return:
        """
        people.sort(key=lambda arr: (-arr[0], arr[-1]))
        ans = []
        for arr in people:
            ans.insert(arr[-1], arr)
        return ans


def main():
    test_case = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(Solution().reconstructQueue(test_case))


if __name__ == '__main__':
    main()
