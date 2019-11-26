from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)


def main():
    h2 = TreeNode(2)
    h2.left = TreeNode(1)
    h2.right = TreeNode(3)
    h2.left.right = TreeNode(4)
    h2.right.right = TreeNode(7)
    test_case = [h2]
    max_depth = Solution().maxDepth(*test_case)
    print(max_depth)


if __name__ == "__main__":
    main()
