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
 #include <queue>
class Solution {
public:
    bool isSymmetric(TreeNode* root) {

        // Create two queues
        if (root == nullptr)
        {
            return true;
        }
        queue <TreeNode*> q1, q2;

        q1.push(root->left);
        q2.push(root->right);


        while(!q1.empty() && !q2.empty())
        {
            TreeNode* left_node = q1.front(); q1.pop();
            TreeNode* right_node = q2.front(); q2.pop();
       
         
            if (left_node == nullptr && right_node == nullptr)
            {
                continue;
            }
      
            if (left_node == nullptr || right_node == nullptr)
            {
                return false;
            }
     
            if (left_node->val != right_node->val) 
            {
                return false;
            }
            q1.push(left_node->left);
            q2.push(right_node->right);
            q1.push(left_node->right);
            q2.push(right_node->left);

        }

        return true;
    }
};
