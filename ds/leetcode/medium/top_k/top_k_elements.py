# Top K Frequent Elements
# Problem Description:
# Given an integer array nums and an integer k,
# return the k most frequent elements. You may return the answer in any order.
# The problem guarantees that the answer is unique, and the follow-up suggests aiming for a time complexity better than O(n log n), where n is the array's size.
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        num_frequency = Counter(nums)
        min_heap = []
        for num, freq in num_frequency.items():
            heapq.heappush(min_heap, (freq,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        heapq.heapify(min_heap)
        top_k = [num for fre, num in min_heap]
        return top_k
    def topKFrequent_v2(self, nums: list[int], k: int):
        num_frequency = Counter(nums)
        max_heap = [(-freq, num) for num, freq in num_frequency.items()]
        heapq.heapify(max_heap)
        topk_k = [heapq.heappop(max_heap)[1] for _ in range(k)]
        return topk_k



if __name__ == '__main__':
        sol = Solution()
        nums = sol.topKFrequent_v2([1,1,1,2,2,3], 2)
        print(nums)

