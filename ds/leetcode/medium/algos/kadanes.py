# This is a classic problem known as Maximum Subarray Sum and is efficiently solved using Kadane’s Algorithm. The idea is to iterate through the array while maintaining:
#
# current_sum: the maximum sum ending at the current index
#
# max_sum: the overall maximum sum found so far
# Given an integer array nums,
# find the subarray with the largest sum, and return its sum.
# Example 1: Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
#

class Solution:
    def maxSubArray(self, nums: list[int]):
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return max_sum

if __name__ == '__main__':
    sol = Solution()
    max = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(max)
