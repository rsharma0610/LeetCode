# Explanation
# You might wonder, how do we know what the nth node from the end of the linked list is, it is not a list so 
# we cannot leverage the len function to easily figure that out?
# First we want to intiialize two pointers, left and right
# Left is pointing to a dummy node, and dummy.next references head
# Right references the head node
# Next, we want to create a gap of size n + 1 between the left and right node
# To achieve this, we can do right = right.next while n > 0 and decrement n by 1 each iteration
# Next we want to traverse the linked list while maintaing this gap between the left and right pointer
# so that when the right pointer has traversed the entire linked list, the left pointer is referencing
# the n + 1 th node from the end of the linked list, this allows us to then do left.next = left.next.next
# successfully deleting the nth node from the end of the linked list
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, head

        # Create the gap between left and right
        while n > 0:
            right = right.next
            n -= 1
        
        # Iterate both pointers until right references None
        while right:
            left = left.next
            right = right.next
        
        # The left pointer should now sit one before the nth node form the end
        left.next = left.next.next

        return dummy.next

# Helper function to create a linked list from a list
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def printLinkedList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    solution = Solution()
    head = createLinkedList([1,2])  # Convert array to linked list
    n = 2
    reversed_head = solution.removeNthFromEnd(head, n)  # Reverse the linked list
    print(f'Reversed Linked List: {printLinkedList(reversed_head)}')  # Print the reversed linked list
