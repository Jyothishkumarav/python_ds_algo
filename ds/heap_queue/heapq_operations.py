import heapq
class Solution:
    def top_k_largest(self, nums, k):
        if k <= 0 or not nums or len(nums) < k :
            return []
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heapreplace(heap, num)

        return heap
    def top_k_smallest(self, nums, k):
        if k <= 0 or not nums or len(nums) < k:
            return []
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, -num)
            else:
                if -num > heap[0]:
                    heapq.heapreplace(heap,-num)
        return sorted([-x for x in heap])

if __name__ == "__main__":
    sol = Solution()
    heap = sol.top_k_smallest([3, 1, 5, 1, 9, 2, 6, 8, 3, 5], 4)
    print(heap)
