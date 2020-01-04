#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2020/1/4 10:14
# leastInterval
# @author: ChangFeng
"""
import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        按照任务数量排序，每次取最大的，然后在冷却时间之内，执行其他数量较少的任务并将任务数-1，
        冷却时间结束或者没有其他任务则重排序，所有任务执行完成后退出
        """
        d = [0 for _ in range(26)]
        for task in tasks:
            d[ord(task) - ord('A')] += 1
        d.sort()
        time = 0
        while d[25] > 0:
            i = 0
            while i <= n:
                if d[25] == 0:
                    break
                if i < 26 and d[25 - i] > 0:
                    d[25 - i] -= 1
                time += 1
                i += 1
            d.sort()
        return time

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        按照任务数量大顶堆化，每次取最大的，然后在冷却时间之内，执行其他数量较少的任务并将任务数-1，
        冷却时间期间，记录其他任务中数量>1的，冷却时间结束后重新将其放入大顶堆
        """
        d = [0 for _ in range(26)]
        for task in tasks:
            d[ord(task) - ord('A')] += 1
        heap = []
        for v in d:
            if v > 0:
                heapq.heappush(heap, -v)
        time = 0
        while heap:
            i = 0
            tmp = []
            while i <= n:
                if heap:
                    v = heapq.heappop(heap)
                    if -v > 1:
                        tmp.append(-(-v - 1))
                time += 1
                if not heap and not tmp:
                    break
                i += 1
            for v in tmp:
                heapq.heappush(heap, v)
        return time

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        取所有任务出现次数的最大值m，以及这个最大值出现的次数mcnt
        耗时为：(m - 1) * (n + 1) + mcnt，其中n为冷却时间，
        m-1因为最后一次不需要考虑冷却时间（最后一次执行的时间为最大值出现的次数而不需要冷却），
        n+1因为执行完某个任务然后才需要进入冷却时间
        len(tasks)与上面求出来的结果中的较大者即为结果
        """
        count = Counter(tasks)
        m = max(count.values())
        mcnt = list(count.values()).count(m)
        return max(len(tasks), (m - 1) * (n + 1) + mcnt)


def main():
    test_case = [["A", "A", "A", "B", "B", "B"], 2]
    print(Solution().leastInterval(*test_case))


if __name__ == '__main__':
    main()
