'''
Given the head of a singly linked list, check if it contains a cycle
by returning boolean True if it does and otherwise, False
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # handle edge case if empty and one node
        if not head or not head.next:
            return False
        # initialize nodes for floyd cycle detection algo
        node1 = head # tortoise traversed list normally
        node2 = head.next # hare is one node ahead than tortoise

        # if node1 and node2 meet then there's a cycle
        while(node1 != node2):
            # check if node2 exists and two nodes ahead
            if not node2 or not node2.next:
                return False
            # else go to next node
            node1 = node1.next
            node2 = node2.next.next

        # if node1 and node2 meet, then there's a cycle
        return True
      
# improved solution
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head

        # traverse list
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # cycle detected
            if slow == fast:
                return True

        # if end of linked list is reached
        return False
