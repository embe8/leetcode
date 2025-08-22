class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    visited = []
    dummy = ListNode(0)  # Create a dummy node to simplify edge cases
    dummy.next = head

    current = dummy
    while current.next is not None:
        if current.next.val not in visited:
            visited.append(current.next.val)
            current = current.next  # Move forward
        else:
            # Skip the duplicate node
            current.next = current.next.next

    return dummy.next

    print()

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # Create sample linked list: 1 -> 2 -> 3 -> 2 -> 4 -> 2 -> None
    n6 = ListNode(2)
    n5 = ListNode(4, n6)
    n4 = ListNode(2, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    print("Original list:")
    print_list(n1)

    # Delete all nodes with value 2
    head = deleteDuplicates(n1)

    print("\nList after deleting value 2:")
    print_list(head)