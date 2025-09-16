/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:

bool hasCycle(ListNode* head) {
    if (!head || !head->next) {
        return false;
    }

    ListNode* tortoise = head;
    ListNode* hare = head->next;

    while (tortoise != hare) {
        if (!hare || !hare->next) {
            return false;
        }
        tortoise = tortoise->next;
        hare = hare->next->next;
    }

    return true;
}
};
