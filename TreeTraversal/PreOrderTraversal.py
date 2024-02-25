# Definition for a binary tree node.

# Pre order traversal, how it works:
# 1) Visit node
# 2) traverse left subtree
# 3) traverse right subtree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        self.doPreOrderTraversal(root, answer)

        for i in range(0, len(answer)):
            print(answer[i])


    def doPreOrderTraversal(self, root, answer):

        if root is None:
            return None

        # adding the current node
        answer.append(root.val)

        if root.left:
            # since pre order goes to left we will keep on calling this until left is null
            self.doPreOrderTraversal(root.left, answer)
        if root.right:
            # after left is done we will move to rightl
            self.doPreOrderTraversal(root.right, answer)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    s = Solution();
    s.preorderTraversal(root)



