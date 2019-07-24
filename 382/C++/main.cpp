/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <stdlib.h> 

class Solution {
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        curhead = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int count = 1;
        int random;
        ListNode *Current = curhead;
        while (Current) {
            if((rand() % count) == 0) {
                random = Current->val;
            }
            Current = Current->next;
            count++;
        }
        return random;
    }
private:
ListNode *curhead;  
};
