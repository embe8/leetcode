'''
  Problem: Given two singly linked lists with values sorted in ascending order, 
    merge the two lists into one, keeping duplicate values
  Solution/Approach: Store all values of the two lists in a vector, sort the vector,
    and create a new linked list to store the vector values
'''
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // create a vector to store the linked list values
        vector <int> vec; 
        // insert values from first and second linked lists
        while (list1)
        {
            // store value from linked list 1
            vec.push_back(list1->val);
            // move to next value
            list1 = list1->next;
        }
        while (list2)
        {
            // store value from linked list 2
            vec.push_back(list2->val);
            // move to next value
            list2 = list2->next;
        }
        // sort the vector values in ascending order
        sort(vec.begin(), vec.end());
        // edge case if empty vector
        if (vec.empty()) { return NULL;}
        // create the linked list with the sorted values
        // pass first element of vector
        ListNode* head = new ListNode(vec[0]);
        // pointer to head of new list
        ListNode* current = head;
        // traverse vector and place its element in the new linkedlist
        for (int i =1; i< vec.size(); i++)
        {
            //set next nodes in new list to elements in the vector
            current->next = new ListNode(vec[i]); // start from index 1 since vec[0] already in the vector
            current = current->next; // go to next node
        }

        return head;

    }
};
