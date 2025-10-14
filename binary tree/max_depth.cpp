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
// Recursive solution: O(n)
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

//Iterative solution: O(n)

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

 using namespace std;

class Solution {
public:
    int maxDepth(TreeNode* root) {
        // check if tree is empty, return 0 if so
        if (!root)
        {
            return 0;
        }

        // store root in queue
        std::deque <TreeNode*> dq;
        dq.push_back(root);
        // initialize depth var
        int depth = 0;
        while(!dq.empty()){
            // get number of nodes in the level
            int levelSize = dq.size();
            // traverse nodes at each level
            for(int i=0;i<levelSize;i++){
                // get node and check if it has left and right children
                TreeNode* current = dq.front();
                dq.pop_front();
                if(current->right){
                    dq.push_back(current->right);
                }
                if(current->left){
                    dq.push_back(current->left);
                }
            }
            depth += 1;
        }
        // after visiting each level increase depth
    return depth;
    }
};
