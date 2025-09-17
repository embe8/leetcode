'''
Problem: Given a singly linked list and two integers representing 
positions of nodes in the linked list, reverse all nodes from position1 to position2

Approach: use three pointers, previous, current, and forward
where previous will be set to the left hand side/before current
and forward will be to the right/after current

Forward node will be in previous node's place, current will be in forward's place,
and previous will be in current node's place after reversal
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        # create dummy list for case where left = 1 
        # it will have a previous pointer
        dummy = ListNode(0)
        prev = dummy # set dummy as previous
        dummy.next = head # next will be the head

        # find and set prev pointer according to left
        for i in range(left-1):
            prev = prev.next

        # set current pointer (should be next to previous)
        current = prev.next

        # swap pointers within left and right indices
        for i in range(right-left):
            # set forward pointer (should be after current)
            forw = current.next
            current.next = forw.next
            forw.next = prev.next
            prev.next = forw
        
        return dummy.next # return head



        
        
