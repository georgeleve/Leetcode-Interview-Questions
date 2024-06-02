# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS algorithm (for this case we use inorder traveral, since the items come sorted) - iterative method
# We pick the element kth element since it is the kth smallest in the inorder traversal
class Solution(object):
    def kthSmallest(root, k):
        if not root:
            return 0
        stack = []
        while True:
            while root: #go to the left child
                stack.append(root)
                root = root.left
            root = stack.pop() # go to the parent
            #print(root.val)
            k -= 1
            if k == 0: #k now is the kth smallest element of the binary search tree
                return root.val
            root = root.right

# Recursive method - O(n) Time Complexity to build a traveral |
# O(n) Space Complecity to keep an inorder traversal in the recursive stack
    def kthSmallestRecursive(self, root, k):
        returnArray = []
        def inorderTraversal(root):
            if root == None:
                return []
            inorderTraversal(root.left)
            returnArray.append(root.val)
            inorderTraversal(root.right)
            return returnArray
        #print(inorderTraversal(root))
        return inorderTraversal(root)[k-1]

if __name__ == "__main__":
    k = 3
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right = TreeNode(6)
    print(Solution.kthSmallest(root, k))