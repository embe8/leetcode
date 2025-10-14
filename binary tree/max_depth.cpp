/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
 #include <deque>

class Solution {
public:
    int maxDepth(TreeNode* root) {
        // check if tree is empty, return 0 if so
        if (!root)
        {
            return 0;
        }
        
        int depthLeft = maxDepth(root->left);
        int depthRight = maxDepth(root->right);

        return 1+std::max(depthLeft, depthRight);

    }
};
