#! python3
# -*- coding:UTF-8 -*-
"""
200. Number of Islands
# Created on 2020/1/15 18:05
# numIslands
# @author: ChangFeng
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        def dfs_mark(y, x):
            if y < 0 or x < 0 or y >= m or x >= n or grid[y][x] != '1':
                return
            grid[y][x] = '0'
            dfs_mark(y, x + 1)
            dfs_mark(y, x - 1)
            dfs_mark(y + 1, x)
            dfs_mark(y - 1, x)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs_mark(i, j)
                    count += 1
        return count


def main():
    # test_case = [
    #     ['1', '1', '1', '1', '0'],
    #     ['1', '1', '0', '1', '0'],
    #     ['1', '1', '0', '0', '0'],
    #     ['0', '0', '0', '0', '0'],
    # ]
    # print(Solution().numIslands(test_case))  # 1
    # test_case = [
    #     ['1', '1', '0', '0', '0'],
    #     ['1', '1', '0', '0', '0'],
    #     ['0', '0', '1', '0', '0'],
    #     ['0', '0', '0', '1', '1'],
    # ]
    # print(Solution().numIslands(test_case))  # 3
    test_case = [["1", "0", "1", "1", "0", "1", "1"]]
    print(Solution().numIslands(test_case))  # 3


if __name__ == '__main__':
    main()
