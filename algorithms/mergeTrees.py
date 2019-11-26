# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        print(self.left)
        print(self.right)
        return str(self.val)


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


def main():
    # [1, 3, 2, 5]
    h1 = TreeNode(1)
    h1.left = TreeNode(3)
    h1.right = TreeNode(2)
    h1.left.left = TreeNode(5)
    # [2, 1, 3, null, 4, null, 7]
    h2 = TreeNode(2)
    h2.left = TreeNode(1)
    h2.right = TreeNode(3)
    h2.left.right = TreeNode(4)
    h2.right.right = TreeNode(7)
    test_case = [h1, h2]
    trees = Solution().mergeTrees(*test_case)
    print(trees)


if __name__ == "__main__":
    main()
