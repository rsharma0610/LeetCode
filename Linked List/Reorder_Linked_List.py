# Explanation, this was a tricky one, but fun to combine multiple algorithms into one
# First we want to seperate the linked list into two halves, the left and right
# 1) Use the tortoise and the hare algorithm to split the linked lists in two halves
#    The algorithm works by using two points, one slow and one fast, in order to locate the middle of the
#    linked list
#    The slow pointer will stop on the final node of the first half because we want to disconnect the first and
#    second halves so we first save a reference to the slow pointer's next reference and then set slow's next
#    reference to None 
# 2) Use the basic reverse linked list algorithm
#    Set prev equal to None and current = slow.next and then perform linked list reversal so the second half of 
#    the linked list is reversed and prev references the head of the reversed linked list
# 3) Finally we want to reorder the linked list inplace
#    Create a references to the fist and second half of the linked list, head and prev
#    Temporarily save the reference of the next pointers for first and second because they will be modified in the next
#    step which will result in them losing their next references
#    Set first.next = second and second.next = tmp1, this interweaves the linked lists and then we iterate through the linked
#    lists and return head which references the start of the reordered linked list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # First step is to find the middle of the linked list(right-biased)
        # Use slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now we need to reverse the right half of the Linked List, we can use the basic reverse linked list algorithm
        # But first, we also need to set the next of the last node of the first half to none to "disconnect" the two halves
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Prev now is at the head of the second half of the linked list which has been reversed and disconnected from the first half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        return head
            
            

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
    head = createLinkedList([2,4,6,8])  # Convert array to linked list
    reversed_head = solution.reorderList(head)  # Reverse the linked list
    print(f'Reversed Linked List: {printLinkedList(reversed_head)}')  # Print the reversed linked list
