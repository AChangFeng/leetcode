#! python3
# -*- coding:UTF-8 -*-
"""
# 79. Word Search
# Created on 2020/4/7 18:41
# exist
# @author: ChangFeng
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        TLE
        """
        if not board or not word:
            return False
        ans = False
        m = len(board)
        n = len(board[0])

        def helper(last, path, w):
            nonlocal ans
            if w == word:
                ans = True
            if len(w) >= len(word):
                return
            if not last:
                for i in range(m):
                    for j in range(n):
                        if board[i][j] == word[0]:
                            helper([i, j], {(i, j)}, word[0])
            else:
                # top
                if last[0] - 1 >= 0:
                    curr = (last[0] - 1, last[1])
                    curr_c = board[curr[0]][curr[1]]
                    if curr not in path and curr_c == word[len(path)]:
                        path.add(curr)
                        helper(curr, path, w + curr_c)
                        path.remove(curr)
                # left
                if last[1] - 1 >= 0:
                    curr = (last[0], last[1] - 1)
                    curr_c = board[curr[0]][curr[1]]
                    if curr not in path and curr_c == word[len(path)]:
                        path.add(curr)
                        helper(curr, path, w + curr_c)
                        path.remove(curr)
                # right
                if last[1] + 1 < n:
                    curr = (last[0], last[1] + 1)
                    curr_c = board[curr[0]][curr[1]]
                    if curr not in path and curr_c == word[len(path)]:
                        path.add(curr)
                        helper(curr, path, w + curr_c)
                        path.remove(curr)
                # bottom
                if last[0] + 1 < m:
                    curr = (last[0] + 1, last[1])
                    curr_c = board[curr[0]][curr[1]]
                    if curr not in path and curr_c == word[len(path)]:
                        path.add(curr)
                        helper(curr, path, w + curr_c)
                        path.remove(curr)

        helper([], None, "")

        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        TLE
        """
        if not board or not word:
            return False
        m = len(board)
        n = len(board[0])

        def dfs(i, j, w):
            if len(w) == 0:
                return True
            if i < 0 or i >= m or j < 0 or j >= n or w[0] != board[i][j]:
                return False
            curr = board[i][j]
            # avoid visit again
            board[i][j] = "#"
            # forward bottom top right and left
            res = dfs(i + 1, j, w[1:]) \
                  or dfs(i - 1, j, w[1:]) \
                  or dfs(i, j + 1, w[1:]) \
                  or dfs(i, j - 1, w[1:])
            board[i][j] = curr
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, word):
                    return True
        return False


def main():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    test_case = [board, "ABCCED"]
    print(Solution().exist(*test_case))  # True
    test_case = [board, "SEE"]
    print(Solution().exist(*test_case))  # True
    test_case = [board, "ABCB"]
    print(Solution().exist(*test_case))  # False
    test_case = [[["a", "b"]], "ba"]
    print(Solution().exist(*test_case))  # True


if __name__ == '__main__':
    main()
