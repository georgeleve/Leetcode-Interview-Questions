# Given a binary tree, return the product of the largest value in each level of the tree
# We take the max element at each level of the tree and we multiply with the total product
# here the max product is 1*3*50 = 150
from collections import deque

class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution():
    def productOfLargestValue(self, root):
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        product = 1
        while queue:
            currentLevelLargestValue = 0
            for i in range(0, len(queue)):
                node = queue.popleft()
                if node.val > currentLevelLargestValue:
                    currentLevelLargestValue = node.val
                # add all of the children
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            product = product * currentLevelLargestValue
        return product

        """
    Constructed binary tree is
                 1
              /    \
             2      3
          /     \ None None
        40        50
    None None  None None
    """

if __name__ == "__main__":
    """
    Good questions to ask the interviewer
    1) How is tree represented -> Is it norde class (val, left, right)
    2) If root is null, return 0?
    3) should i do it recursively or iteratively? I can do it both with BFS and DFS algorithm
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(50)
    a = Solution()
    print("The product of the largest value in each level of the tree is", a.productOfLargestValue(root))