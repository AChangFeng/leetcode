from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans


def main():
    test_case = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(test_case))


if __name__ == '__main__':
    main()
