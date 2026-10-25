/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public TreeNode InvertTree(TreeNode root) {
        if (root is null) {
            return root;
        }

        Queue<TreeNode> qq = new();
        qq.Enqueue(root);

        while (qq.Count > 0) {
            TreeNode node = qq.Dequeue();
            (node.left, node.right) = (node.right, node.left);
            if (node.left is not null) {
                qq.Enqueue(node.left);
            }
            if (node.right is not null) {
                qq.Enqueue(node.right);
            }
        }
        return root;
    }
}
