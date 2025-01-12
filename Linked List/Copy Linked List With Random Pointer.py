# Explanation
# The tricky part of this problem is establishing the links, this is alleviated by a hashmap
# We use two passes:
# First pass) The first pass is to create deep copies of all the nodes and to also
# link all the original nodes to their deep copies using a hash map
# Second pass) Leverage the hash map created by the first pass to create all the next and random links
# for the deep copy of the linked list
# Return hashmap[head] because that is the head of the deep copy
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head # Curr will be used to iterate through the linked list 
        oldToCopy = {None : None} # Hashmap to link old nodes to the copied versions

        # First pass to create deep copy of all the nodes and create the hash map to link old nodes to new copies
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        curr = head

        # Second pass to set all next and random references
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next] 
            copy.random = oldToCopy[curr.random] 
            curr = curr.next
        
        return oldToCopy[head]

# Helper function to create a linked list from a list
def createLinkedList(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
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
    reversed_head = solution.copyRandomList(head)  # Reverse the linked list
    print(f'Reversed Linked List: {printLinkedList(reversed_head)}')  # Print the reversed linked list
