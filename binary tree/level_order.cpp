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
class Solution {
public:
  
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result; // Store levels

    if (root == nullptr)
    {
        return result;
    }
    // Create queue to store nodes to be processed
    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()){
        int levelSize = q.size();
        vector <int> levelNodes;

        for (int i = 0; i < levelSize; i++)
        {
            // Get current node to process
            TreeNode* currentNode = q.front();
            // Remove current node to process next node for next iteration
            q.pop();
            // Place current node value to vector storing each level
            levelNodes.push_back(currentNode->val);

            //check for left and right children if exists
            if (currentNode->left != nullptr)
            {
                q.push(currentNode->left);
            }
            if (currentNode->right != nullptr)
            {
                q.push(currentNode->right);
            }
        }
        // Store each level to the final result vector
        result.push_back(levelNodes);

    }
    return result;
}
};
