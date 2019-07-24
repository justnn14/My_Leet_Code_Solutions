/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        ReadTree(root);
        vector<double> ReturnList;
        for(unsigned int i = 0; i < Total.size(); i++) {
            ReturnList.push_back(Total.at(i)/Divide.at(i));
        }
        return ReturnList;
    }
    void ReadTree(TreeNode* root, int level = 0) {
        if(root) {
            if(Total.size() <= level) {
               Total.push_back(0);
               Divide.push_back(0);
           }
            Total.at(level) += root->val;
            Divide.at(level) += 1;
            ReadTree(root->right, level + 1);
            ReadTree(root->left, level + 1);
       } 
    }
    
private:
    vector<double> Total;
    vector<double> Divide;
};
