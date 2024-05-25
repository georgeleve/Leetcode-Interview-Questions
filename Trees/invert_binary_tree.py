from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # O(n) Time Complexity | O(n) Space Complexity for both solutions, were n is the number of nodes in the tree

    # Solve the problem using Depth First Search (Preorder Traversal) and recursion - We can solve it using postorder traversal as well
    def invertBinaryTree(self, root):
        if root is None:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root

    # Solve using Breadth First Search and a Queue (level order traversal)
    def invertBinaryTreeBFS(self, root):
        if root is None:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            for i in range(0, len(queue)):
                node = queue.popleft()
                
                temp = node.left
                node.left = node.right
                node.right = temp

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return root
        

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(10)
    root.right.left = TreeNode(70)
    root.right.right = TreeNode(33)
    a = Solution()
    a.invertBinaryTree(root)
    a.invertBinaryTreeBFS(root)