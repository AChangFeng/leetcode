#! python3
# -*- coding:UTF-8 -*-
"""
# 96. Unique Binary Search Trees
# Created on 2019/12/30 19:04
# numTrees
# @author: ChangFeng
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        dynamic program
        """
        # dp下标代表给定数字可以组成多少个BFS树
        dp = [0 for _ in range(n + 1)]
        # 很容易能得出dp[0]=dp[1]=1
        dp[0] = dp[1] = 1
        # 每次构建一个树，需要先算出一个根节点，然后计算左右两边子树的数量，最后左右相乘
        # 对于dp[n]，可以n前面结果计算而来
        # 计算规则就是：for x in range(1,n+1): dp[n]+=dp[n-x]*dp[x-1]
        for level in range(2, n + 1):
            # 分别选取第1,2,3...n作为根节点，计算其可能组成的树的数量，相加
            for root in range(1, level + 1):
                dp[level] += dp[level - root] * dp[root - 1]
        return dp[n]


def main():
    test_case = 3
    res = Solution().numTrees(test_case)
    assert res == 5, "error"


if __name__ == '__main__':
    main()
