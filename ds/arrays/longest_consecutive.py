# Given
# an
# unsorted
# array
# of
# integers
# nums,
# return the
# length
# of
# the
# longest
# consecutive
# elements
# sequence.
#
# You
# must
# write
# an
# algorithm
# that
# runs in O(n)
# time.
#
# Example
# 1:
#
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The
# longest
# consecutive
# elements
# sequence is [1, 2, 3, 4].Therefore
# its
# length is 4.
# Example
# 2:
#
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9
# Example
# 3:
#
# Input: nums = [1, 0, 1, 2]
# Output: 3
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only try to build sequence if num is the start
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


