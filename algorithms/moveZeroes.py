from typing import List


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        j = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                for x in range(i, j):
                    nums[x] = nums[x + 1]
                nums[j] = 0
                j -= 1

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


def main():
    test_case = [0, 1, 0, 3, 12]
    Solution().moveZeroes(test_case)
    print(test_case)


if __name__ == '__main__':
    main()
