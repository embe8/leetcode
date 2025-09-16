# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        store_list = []
        
        while list1:
            store_list.append(list1.val)
            list1 = list1.next
        while list2:
            store_list.append(list2.val)
            list2 = list2.next

        sorted_list = sorted(store_list)

        if not sorted_list: return None
        # create new linked list
        newHead = ListNode(sorted_list[0])
        current = newHead

        # place sorted_list values into new linked list
        for i in range(1, len(sorted_list)):
            current.next = ListNode(sorted_list[i])
            current = current.next
        
        return newHead


        
