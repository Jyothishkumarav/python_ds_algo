# 143. Reorder List
# Medium
# Topics
# premium lock icon
# Companies
# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Step 1: Handle edge cases
        if not head or not head.next:
            return

        # Step 2: Find the middle of the list using slow and fast pointers
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list: slow is at the last node of the first half
        second_half = slow.next
        slow.next = None  # End the first half

        # Step 3: Reverse the second half
        prev = None
        curr = second_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second_half = prev  # Head of reversed second half

        # Step 4: Merge the two halves
        first_half = head
        while second_half:
            # Store next nodes
            next_first = first_half.next
            next_second = second_half.next
            # Connect first half to second half
            first_half.next = second_half
            second_half.next = next_first
            # Move pointers
            first_half = next_first
            second_half = next_second