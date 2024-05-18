# https://leetcode.com/problems/diameter-of-binary-tree/description/
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    #Solve using Depth First Search - using Recursion
    # Height = maximum depth of the binary search tree
    # O(n) Time Complexity | O(log(n))  space complexity in the best case when tree is balanced.
    # If tree is not balanced then worst space complexity O(n), where n is the number of nodes in the tree.
    # findHeightUsingRecursiveDepthFirstSearch
    def findHeightUsingDFS(self, root):
        #Base case if the tree is empty
        if root is None:
            #print("The return value is gonna be 0")
            return 0
        #if tree is not empty, then height = 1 + max of left height and right heights
        leftHeight = self.findHeightUsingDFS(root.left)
        rightHeight = self.findHeightUsingDFS(root.right)
        #print("The return value is gonna be ", 1 + max(leftHeight, rightHeight))
        return 1 + max(leftHeight, rightHeight)
    
    # Use stack instead of recursion
    # O(n) Time Complexity | O(n) Scace Complexity for worst case if we have e.g. only left children
    # and O(log(n)) Space Complexity, for best case, if we have a balanced tree
    def findHeightUsingIterativeDFS(self, root):
        if root is None:
            return 0
        stack = []
        stack.append((1, root))
        maxDepth = 0
        while stack:
            currentDepth, root = stack.pop()
            if root is not None:
                maxDepth = max(maxDepth, currentDepth)
                stack.append((currentDepth + 1, root.left))
                stack.append((currentDepth + 1, root.right))
        return maxDepth

    #Breadth First Search(Level Order Traversal)
    #We increment the height at every level and at the end we return it
    def findHeightUsingBFS(self, root):
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        height = 0
        while queue:
            for i in range(0, len(queue)):
                node = queue.popleft()
                # add all of the children
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            height += 1
        return height



        """
    Constructed binary tree is
                 1
              /    \
             2      3
          /     \ None None
        4        5
    None None  None None
    """
    # 
    def diameterOfBinarySearchTree(self, root):
        return "hello world"


if __name__ == "__main__":
    """
    Constructed binary tree is
                1
              /   \
            2      3
          /  \
        4     5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    a = Solution()
    # By definition, the maximum depth of a binary tree is the maximum number of steps to reach a leaf node from the root node.
    print("The height (maxmimum depth) of the tree is ", a.findHeightUsingDFS(root))
    print("The height (maxmimum depth) of the tree is ", a.findHeightUsingIterativeDFS(root))
    print("The height (maxmimum depth) of the tree is ", a.findHeightUsingBFS(root))
    
    print(a.diameterOfBinarySearchTree(root))