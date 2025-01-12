

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_l1 = 0
        count_l1 = 0
        
        cur = l1
        while cur:
            sum_l1 += cur.val * 10 ** count_l1 
            count_l1 += 1
            cur = cur.next
        
        
        sum_l2 = 0
        count_l2 = 0

        cur = l2
        while cur:
            sum_l2 += cur.val * 10 ** count_l2
            count_l2 += 1
            cur = cur.next
        
        sum_l3 = sum_l1 + sum_l2

        dummy = ListNode()
        pointer = dummy

        for digit in str(sum_l3)[::-1]:
            pointer.next = ListNode(int(digit))
            pointer = pointer.next
        
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
    l1 = createLinkedList([1,2,3])  # Convert array to linked list
    l2 = createLinkedList([4,5,6])
    sumLinkedList = solution.addTwoNumbers(l1, l2)  # Reverse the linked list
    print(f'Sum: {printLinkedList(sumLinkedList)}')  # Print the reversed linked list
