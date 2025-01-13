# Explanation
# We can use a slow and fast pointer for cycle detection
# The slow pointer will move one node per iteration and the fast pointer will move two nodes per iteration
# If a cycle exists, the fast and slower pointer will eventually be equal because the fast pointer will loop 
# around to lap the slow pointer
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
