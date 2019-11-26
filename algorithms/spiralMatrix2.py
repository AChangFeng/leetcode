#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/23 15:05
# spiralMatrix2
# @author: ChangFeng
"""


class Solution:
    def generateMatrix(self, n):
        ans = [[0] * n for _ in range(n)]
        # directions:left to right,top to bottom,right to left,bottom to top
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # current direction
        d = 0
        x = y = 0
        for i in range(1, n * n + 1):
            # add num to ans matrix
            ans[y][x] = i
            # get direction
            dy, dx = directions[d % 4]
            # if next coordinate in matrix and not set, move forward in this direction
            if -1 < y + dy < n and -1 < x + dx < n and ans[y + dy][x + dx] == 0:
                y, x = y + dy, x + dx
            else:
                # else we change our direction
                d += 1
                dy, dx = directions[d % 4]
                # and move forward in new direction
                y, x = y + dy, x + dx
        return ans

    def generateMatrix1(self, n):
        ans = [[0] * n for _ in range(n)]
        # 初始化坐标和方向 横坐标也就是x的方向应该是向右的 所以是1
        y, x, dy, dx = 0, 0, 0, 1
        for i in range(n * n):
            ans[y][x] = i + 1
            # 如果下一个位置在目标矩阵上，且填充了元素，改变方向
            # 这里有个trick，因为y+dy,x+dx可能超出[0,n-1]这个区间，正常来说
            # 超出区间的时候应该改变方向，但是这里使用了(x+dx)%n，也就是说：
            # 如果不在[0,n-1]区间范围内，那么坐标会落到已经填充的元素上，获得的元素
            # 肯定是已经填充好的，也能改变方向，达到目的
            if ans[(y + dy) % n][(x + dx) % n]:
                dy, dx = dx, -dy
            y += dy
            x += dx
        return ans


def main():
    print(Solution().generateMatrix(3))
    print(Solution().generateMatrix1(3))


if __name__ == '__main__':
    main()
