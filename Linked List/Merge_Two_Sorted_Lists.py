# Explanation
# To merge the two sorted lists and maintain the list's sorted property we can iterate through the lists
# within a while loop and compare the values of the current nodes
# We set the head.next to the smaller value and then iterate the list that was added from to prevent repeated processing
# of nodes
# Then we also set head to head.next to make sure we are building out the linked list properly
# At the end, there still may be unprocessed nodes so we can simply check to see which list contains
# unprocessed nodes and reference them with head.next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            
            else:
                head.next = list2
                list2 = list2.next
            
            head = head.next
        
        if list1:
            head.next = list1
        
        if list2:
            head.next = list2
        
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
    list1 = createLinkedList([1,2,4])  # Convert array to linked list
    list2 = createLinkedList([1,3,5])
    reversed_head = solution.mergeTwoLists(list1, list2)  # Reverse the linked list
    print(f'Reversed Linked List: {printLinkedList(reversed_head)}')  # Print the reversed linked list
