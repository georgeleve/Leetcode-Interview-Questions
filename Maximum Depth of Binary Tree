/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int maxDepth(TreeNode root) {
        if(root == null) return 0;
        int depth_left = maxDepth(root.left) + 1;
        int depth_right = maxDepth(root.right) + 1;
        return depth_left > depth_right ? depth_left :depth_right;
    }
}
