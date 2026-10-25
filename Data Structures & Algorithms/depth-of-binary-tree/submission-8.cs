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
    public int MaxDepth(TreeNode root) {
        if (root is null)
            return 0;
        Stack<Tuple<TreeNode, int>> stk = new();
        stk.Push(new(root, 1));
        int depth = 0;
        while (stk.Count > 0) {
            (TreeNode node, int height) = stk.Pop();
            if (node is not null) {
                depth = Math.Max(height, depth);
                if (node.left is not null) {
                    stk.Push(new(node.left, height + 1));
                }
                if (node.right is not null) {
                    stk.Push(new(node.right, height + 1));
                }
            }
        }
        return depth;
    }
}
