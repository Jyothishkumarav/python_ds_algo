# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
#
# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
#
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.
#
# The replacement must be in place and use only constant extra memory. Sove this problem with step by step . Tsrat your solution with
#
# Step-by-step Explanation:
# Find the first decreasing element from the right (pivot):
# Traverse the array from the end, and find the first element nums[i] such that nums[i] < nums[i+1].
# Let's call this index i. This means the suffix starting from i+1 is in decreasing order.
#
# If such an index doesn't exist (array is in descending order):
# Simply reverse the entire array to get the smallest permutation (ascending order).
#
# Find the element just larger than nums[i] to its right:
# Again, start from the end, and find the first index j such that nums[j] > nums[i].
#
# Swap nums[i] and nums[j]
#
# Reverse the sub-array from i+1 to end (to make it the smallest possible order).

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """

        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the element just larger than nums[i] to the right
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the suffix starting at i+1
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    sol = Solution()
    nus = [1,2,3]
    sol.nextPermutation(nus)
