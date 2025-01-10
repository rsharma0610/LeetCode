# Explanation
# Reverse Linked List is a classic problem
# We want to reverse the order of the links, so we want to set the curent ListNode's next pointer to point to the
# previous ListNode
# But, if we simply set the current node's next pointer to the previous node, we would lose reference to
# the rest of the linked list because we would no longer be able to reference it through the current's
# next pointer
# To prevent this problem, before changing the reference of the next pointer, we can save the original
# reference of the next pointer in a temporary node so that we still have access to the rest of the linked
# list
# Then we simply repeat this cycle of 
# 1) Save reference of original next pointer
# 2) Set current's next pointer to the previous node
# 3) Set previous node to the current node
# 4) Set current node to the temporary reference of the original next pointer
# Continue this process until current is None, meaning current has iterated through the entire linked list
# and return prev because it is the head of the reversed linked list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head 

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

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
    head = createLinkedList([0, 1, 2, 3])  # Convert array to linked list
    reversed_head = solution.reverseList(head)  # Reverse the linked list
    print(f'Reversed Linked List: {printLinkedList(reversed_head)}')  # Print the reversed linked list
