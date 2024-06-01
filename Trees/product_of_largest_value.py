# Given a binary tree, return the product of the largest value in each level of the tree
class Solution():
    def productOfLargestValue(self, root):
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        product = 1
        while queue:
            currentLevelLargestValue = -1
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