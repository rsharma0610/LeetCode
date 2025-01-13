# Explanation
# We can use the properties of integer addition to solve this algorithm
# We need to account for two values, what we contribute at the decimal place and what we carry over
# What to contribute:
# If for example you add 9 + 9, which equals 18, you would contribute an 8 to the decimal place
# The value to contribute can be extracted using % 10
# What to carry over:
# In the example of 9 + 9 above, which equals 18, a 1 would be carried over for thr addition of the next 
# decimal place, the number to be carried over can be calucluated by ineteger division by 10
# We can then run the loop while list 1, list 2, or carry still need to be processed


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        carry = 0
        while l1 or l2 or carry:
            # Get the value from each linked list to sum if there is no value at the decimal place then contribute 0
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0

            val = val_l1 + val_l2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next


        

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
