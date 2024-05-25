# https://www.youtube.com/watch?v=HG2tiAZWccg
# Very similar problem (not the exact same): https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# How to solve leetcode problems during the interview
# 0. Read the question and understand it, repeat back the question in simple terms to the interviewer
# 1. Ask clarifying questions! (talk about: base cases, input representation, other edge cases: e.g. product overflow)
# 2. Discuss proposed solution aproarch with the interviewer. Discuss different solutions with time and space complexity
#  aslo clarify how the solution should be done: e.g. should i do a recursive or iterative solution?
# 3. Code the solution
# 4. Step by step walkthrough, line by line (Dry run the solution) and cautch bugs
# 5. Time and Space Complexity Analysis

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Given a binary tree, return the product of the largest value in each level of the tree
    # Use Breadth First Search (Level Order Traversal) with a queue and keep tract of largest variable
    # At end of each level, multiple running product by largest node value of that level
    # O(n) Time Complexity | O(n) Space Complexity, where n is the total number of nodes in the tree
    def productOfLargestValue(self, root):
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        product = 1
        while queue:
            currentLevelLargestValue = float("-inf")
            for i in range(0, len(queue)):
                node = queue.popleft()
                currentLevelLargestValue = max(currentLevelLargestValue, node.val)
                # add all of the children
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            product = product * currentLevelLargestValue
        return product

if __name__ == "__main__":
    """
    Good questions to ask the interviewer
    1) How is tree represented -> Is it norde class (val, left, right)
    2) We are calculating the product, can this overflow?
    3) If root is null, return 0?
    Constructed binary tree is
                 10
               /     \
             3        4
           /  \     /   \
          7    10  12    9
         / \       /  \   \
        1   6     24   3   7
       /              / \
      12              5  8
    """
    root = TreeNode(10)
    root.left = TreeNode(3)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(10)
    root.left.left.left = TreeNode(1)
    root.left.left.right = TreeNode(6)
    root.left.left.left.left = TreeNode(12)

    root.right = TreeNode(4)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(7)
    root.right.left.left = TreeNode(24)
    root.right.left.right = TreeNode(3)
    root.right.left.right.left = TreeNode(5)
    root.right.left.right.right = TreeNode(8)
    a = Solution()
    print("The product of the largest value in each level of the tree is", a.productOfLargestValue(root))