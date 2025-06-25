# Given
# the
# head
# of
# a
# linked
# list, remove
# the
# nth
# node
# from the end
#
# of
# the
# list and
# return its
# head.
#
# Example
# 1:
#
# Input: head = [1, 2, 3, 4, 5], n = 2
# Output: [1, 2, 3, 5]
# Example
# 2:
#
# Input: head = [1], n = 1
# Output: []
# Example
# 3:
#
# Input: head = [1, 2], n = 1
# Output: [1]

# How it works:
#
# Setup:
# Create a dummy node pointing to head to handle edge cases (like removing the first node)
# Initialize two pointers: fast and slow, both starting at dummy
# Create Gap:
# Move fast pointer n+1 steps ahead to create a gap of n nodes between fast and slow
# Move Pointers:
# Move both pointers one step at a time until fast reaches the end
# When fast reaches null, slow will be at the node before the one to be deleted
# Remove Node:
# Update slow.next to skip the nth node from the end
# Return dummy.next as the new head
# Time and Space Complexity:
#
# Time: O(L), where L is the length of the linked list (single pass)
# Space: O(1), only using constant extra space
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head:[ListNode], n: int):
        dummy= ListNode()
        dummy.next = head
        fast = slow = dummy
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


