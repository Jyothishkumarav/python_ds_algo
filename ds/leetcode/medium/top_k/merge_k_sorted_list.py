from heapq import heappush, heappop
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists):
        if not lists or not any(lists):
            return None

            # Initialize min-heap
        heap = []
        for i, lst in enumerate(lists):
            if lst:  # Only add non-empty lists
                # Push (value, index, node) to handle equal values
                heappush(heap, (lst.val, i, lst))

        # Dummy node to simplify list building
        dummy = ListNode(0)
        current = dummy

        # Process heap until empty
        while heap:
            val, i, node = heappop(heap)
            # Add smallest node to result
            current.next = node
            current = current.next
            # Add next node from the same list to heap
            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    sol.mergeKLists([[1,4,5],[2,6],[1,3,4]])
