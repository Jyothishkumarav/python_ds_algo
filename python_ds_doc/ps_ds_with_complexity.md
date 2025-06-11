# 50 Comprehensive Data Structure Problems with Time Complexity Analysis

## Time Complexity Analysis Guide

### How to Calculate Time Complexity:
1. **Count the operations**: Look at loops, recursive calls, and basic operations
2. **Identify the input size**: Usually denoted as 'n' 
3. **Find the dominant term**: The term that grows fastest as n increases
4. **Drop constants and lower-order terms**: O(2n + 3) becomes O(n)

### Common Time Complexities:
- **O(1)**: Constant - accessing array element, hash table lookup
- **O(log n)**: Logarithmic - binary search, balanced tree operations
- **O(n)**: Linear - single loop through array, linear search
- **O(n log n)**: Linearithmic - efficient sorting algorithms (merge sort, heap sort)
- **O(n²)**: Quadratic - nested loops, bubble sort
- **O(2^n)**: Exponential - recursive fibonacci without memoization

---

## Arrays (12 Problems)

### 1. Two Sum
**Problem**: Find two numbers in array that add up to target sum.

**Time Complexity**: O(n)
**Space Complexity**: O(n)
**Analysis**: Single pass through array (O(n)), hash table operations are O(1) average case.

```python
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Test
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
```

### 2. Maximum Subarray (Kadane's Algorithm)
**Problem**: Find the contiguous subarray with the largest sum.

**Time Complexity**: O(n)
**Space Complexity**: O(1)
**Analysis**: Single pass through array, constant space for variables.

```python
def max_subarray(nums):
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)
    
    return max_global

# Test
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
```

### 3. Merge Intervals
**Problem**: Merge overlapping intervals.

**Time Complexity**: O(n log n)
**Space Complexity**: O(n)
**Analysis**: O(n log n) for sorting, O(n) for merging process.


**Approach**

Sort the intervals: Sorting by start time ensures we process intervals in order, making it easier to check for overlaps. If start times are equal, sort by end time to avoid edge cases.

**Iterate and merge:**

Keep track of the current interval (initially the first one).
For each next interval, check if it overlaps with the current one (i.e., the next interval’s start is less than or equal to the current interval’s end).
If they overlap, merge by updating the current interval’s end to the maximum of both ends.
If they don’t overlap, add the current interval to the result and update the current interval to the next one.
Add the last interval: After the loop, append the final current interval to the result.

```python
def merge_intervals(intervals):
    # If the list is empty, return empty list
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: (x[0], x[1]))
    
    # Initialize result list with the first interval
    result = []
    current_interval = intervals[0]
    
    # Iterate through the sorted intervals
    for next_interval in intervals[1:]:
        # If current interval overlaps with next interval
        if current_interval[1] >= next_interval[0]:
            # Merge by updating the end time
            current_interval[1] = max(current_interval[1], next_interval[1])
        else:
            # No overlap, append current interval and update to next
            result.append(current_interval)
            current_interval = next_interval
    
    # Append the last interval
    result.append(current_interval)
    
    return result

# Test the function
intervals = [[1,3], [2,6], [8,10], [15,18]]
print(merge_intervals(intervals))  # Output: [[1,6], [8,10], [15,18]]  # Output: [[1,6],[8,10],[15,18]]
```

### 4. Product of Array Except Self
**Problem**: Return array where each element is product of all elements except itself.

**Time Complexity**: O(n)
**Space Complexity**: O(1) excluding output array
**Analysis**: Two passes through array, constant extra space.

```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    # Forward pass: left products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Backward pass: multiply by right products
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# Test
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
```

### 5. Find Peak Element
**Problem**: Find any peak element in array (element greater than its neighbors).

**Time Complexity**: O(log n)
**Space Complexity**: O(1)
**Analysis**: Binary search approach, dividing search space by half each iteration.

**Problem Understanding**

Input: An array of integers, e.g., [1, 2, 3, 1].
Output: The index of any peak element (an element greater than both its neighbors, or at the edges, greater than the single neighbor).

**Constraints:**

If the array has at least one element, a peak always exists (e.g., at the edges or a local maximum).
For edge elements (first or last), we only compare with one neighbor.
We need to find any peak, not all peaks.


Example:
Input: [1, 2, 3, 1] → Output: 2 (since nums[2] = 3 is greater than nums[1] = 2 and nums[3] = 1).
Input: [1, 2, 1, 3, 5, 6, 4] → Output: 1 or 5 (since nums[1] = 2 is greater than 1 and 1, or nums[5] = 6 is greater than 5 and 4).

**Approach**


A peak element is guaranteed to exist because the array can be thought of as having imaginary elements of negative infinity at both ends (-∞, nums[0], ..., nums[n-1], -∞). A simple linear scan could work by checking each element against its neighbors, but this takes O(n) time. Since the problem often hints at a more efficient solution (e.g., in LeetCode’s “Find Peak Element”), we’ll use a binary search approach to achieve O(log n) time complexity.

**Binary Search Idea :**
A peak is an element greater than its neighbors, so the array must have at least one “hill” where values increase and then decrease.
At any point, compare the middle element with its neighbor (e.g., the right neighbor):
If nums[mid] > nums[mid+1], the middle element is greater than the right neighbor, so a peak must exist in the left half (including mid).
If nums[mid] < nums[mid+1], the values are increasing, so a peak must exist in the right half (excluding mid).
Adjust the search range accordingly and repeat until we find a peak.
Handle edge cases (e.g., array length 1 or elements at boundaries).
```python
def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

# Test
print(find_peak_element([1, 2, 3, 1]))  # Output: 2
```

### 6. Container With Most Water
**Problem**: Find two lines that form container holding most water.

**Time Complexity**: O(n)
**Space Complexity**: O(1)
**Analysis**: Two pointers approach, single pass through array.

**Problem Understanding**

**Input:** An array of integers height, where height[i] is the height of a vertical line at index i. For example, [1,8,6,2,5,4,8,3,7].
**Output:** The maximum area of water the container can hold, calculated as the area between two lines. The area is determined by the distance between the lines (width) and the minimum height of the two lines (height).
**Area Formula: ** For lines at indices i and j (where i < j), the area is:

**Area = min(text{height}[i], text{height}[j]) * times (j - i)**

Goal: Find the pair of indices i and j that maximizes this area.
Constraints:

The array has at least 2 elements.
Heights are non-negative integers.
We can’t slant the container; lines are vertical.


Example:

Input: [1,8,6,2,5,4,8,3,7] → Output: 49 (lines at indices 1 and 8 with heights 8 and 7, width = 8 - 1 = 7, area = min(8,7) × 7 = 49).
Input: [1,1] → Output: 1 (area = min(1,1) × 1 = 1).



Approach
A naive solution would be to try every pair of indices (i, j) and compute the area, but this takes O(n²) time. Instead, we’ll use a two-pointer technique to achieve O(n) time complexity, which is more efficient.
Two-Pointer Idea

Initialize two pointers: left at the start (index 0) and right at the end (index n-1).
Compute the area between the lines at left and right:

Width = right - left.
Height = min(height[left], height[right]).
Area = Width × Height.


Update the maximum area seen so far.
Move the pointer pointing to the shorter line inward:

If height[left] <= height[right], increment left.
Otherwise, decrement right.


Repeat until left meets right.
Why move the shorter line?

The area is limited by the shorter height. Moving the taller line inward would reduce the width and keep the height the same or smaller (since the height is still limited by the shorter line or the new line’s height), so it can’t increase the area.
Moving the shorter line gives a chance to find a taller line that might increase the area, despite the reduced width.

```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        current_water = width * min(height[left], height[right])
        max_water = max(max_water, current_water)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# Test
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
```

### 7. 3Sum
**Problem**: Find all unique triplets that sum to zero.

**Time Complexity**: O(n²)
**Space Complexity**: O(1) excluding output
**Analysis**: O(n log n) for sorting, O(n²) for nested loops with two pointers.


**Problem Understanding**

Input: An array of integers nums, e.g., [-1, 0, 1, 2, -1, -4].

Output: A list of unique triplets [nums[i], nums[j], nums[k]] where i != j != k and nums[i] + nums[j] + nums[k] = 0.

Constraints:
T
he array has at least 3 elements.
Triplets must be unique (no duplicate triplets in the output).
The order of numbers in a triplet doesn’t matter, but we typically return them sorted for consistency.
Example:
Input: [-1, 0, 1, 2, -1, -4] → Output: [[-1, -1, 2], [-1, 0, 1]].
Input: [0, 0, 0] → Output: [[0, 0, 0]].
Input: [1, 2, 3] → Output: [] (no triplets sum to zero).
# 3Sum Problem: Approach in Two-Pointer Technique

The **3Sum** problem requires finding all unique triplets in an array of integers that sum to zero. Below is a step-by-step explanation of the efficient two-pointer approach to solve this problem.

## Problem Statement
- **Input**: An array of integers `nums` (e.g., `[-1, 0, 1, 2, -1, -4]`).
- **Output**: A list of unique triplets `[nums[i], nums[j], nums[k]]` where `i != j != k` and `nums[i] + nums[j] + nums[k] = 0`.
- **Goal**: Return all such triplets without duplicates (e.g., `[[-1, -1, 2], [-1, 0, 1]]`).

## Approach: Two-Pointer Technique

This approach achieves O(n²) time complexity by sorting the array and using two pointers to find pairs that sum to a target value for each fixed element.

### Step-by-Step Approach

1. **Check Input Size**:
   - If the array has fewer than 3 elements, no triplets are possible.
   - Return an empty list.

2. **Sort the Array**:
   - Sort the input array in ascending order (O(n log n)).
   - Sorting helps:
     - Use two pointers efficiently.
     - Skip duplicates to ensure unique triplets.
   - Example: `[-1, 0, 1, 2, -1, -4]` becomes `[-4, -1, -1, 0, 1, 2]`.

3. **Iterate Over the First Element**:
   - For each index `i` from 0 to `n-3` (where `n` is the array length):
     - Use `nums[i]` as the first number of the triplet.
     - Skip if `nums[i] == nums[i-1]` (for `i > 0`) to avoid duplicate triplets starting with the same number.
     - Set `target = -nums[i]` (we need `nums[left] + nums[right] = -nums[i]`).

4. **Two-Pointer Search for Remaining Two Numbers**:
   - Initialize two pointers:
     - `left = i + 1` (start of the subarray after `i`).
     - `right = n - 1` (end of the array).
   - While `left < right`:
     - Compute `current_sum = nums[left] + nums[right]`.
     - If `current_sum == target`:
       - Add the triplet `[nums[i], nums[left], nums[right]]` to the result.
       - Skip duplicates:
         - Increment `left` while `nums[left] == nums[left + 1]` to avoid duplicate second numbers.
         - Decrement `right` while `nums[right] == nums[right - 1]` to avoid duplicate third numbers.
       - Move `left += 1` and `right -= 1` to continue searching.
     - If `current_sum < target`:
       - Increment `left` to increase the sum (since array is sorted).
     - If `current_sum > target`:
       - Decrement `right` to decrease the sum.

5. **Return the Result**:
   - The result contains all unique triplets that sum to zero.

### Example Walkthrough
- **Input**: `[-1, 0, 1, 2, -1, -4]`
- **Sorted**: `[-4, -1, -1, 0, 1, 2]`
- **Steps**:
  - For `i = 0` (`nums[i] = -4`, `target = 4`):
    - `left = 1`, `right = 5`: `-1 + 2 = 1 < 4` → `left += 1`.
    - Continue; no triplets found.
  - For `i = 1` (`nums[i] = -1`, `target = 1`):
    - `left = 2`, `right = 5`: `-1 + 2 = 1` → Add `[-1, -1, 2]`, skip duplicate `left`, move pointers.
    - `left = 3`, `right = 4`: `0 + 1 = 1` → Add `[-1, 0, 1]`, move pointers.
  - For `i = 2`: Skip since `nums[2] = -1` duplicates `nums[1]`.
  - Continue until `i = n-3`.
- **Output**: `[[-1, -1, 2], [-1, 0, 1]]`.

### Why It Works
- **Sorting**: Enables efficient two-pointer search and duplicate handling.
- **Two Pointers**: Reduces the O(n³) brute-force approach to O(n²) by fixing one element and searching for two others.
- **Duplicate Handling**: Skipping identical values at `i`, `left`, and `right` ensures unique triplets.
- **Correctness**: All possible triplets are considered by iterating `i` and scanning the remaining array.

### Complexity
- **Time Complexity**: O(n²)
  - Sorting: O(n log n).
  - For each `i` (O(n)), two-pointer search is O(n).
- **Space Complexity**: O(1) or O(n) (depending on sorting implementation), excluding the output.

### Edge Cases
- **Empty or < 3 elements**: Return `[]`.
- **All zeros**: `[[0, 0, 0]]` (e.g., `[0, 0, 0]`).
- **No solution**: Return `[]` (e.g., `[1, 2, 3]`).
- **Duplicates**: Handled by skipping identical values.

This approach is efficient and ensures all unique zero-sum triplets are found.

```python
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    
    return result

# Test
print(three_sum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
```

### 8. Search in Rotated Sorted Array
**Problem**: Search target in rotated sorted array.

**Time Complexity**: O(log n)
**Space Complexity**: O(1)
**Analysis**: Modified binary search, still divides search space by half.

```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Test
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
```

### 9. Longest Consecutive Sequence
**Problem**: Find length of longest consecutive elements sequence.

**Time Complexity**: O(n)
**Space Complexity**: O(n)
**Analysis**: Convert to set (O(n)), then iterate checking sequences (O(n) total).

The Longest Consecutive Sequence problem requires finding the length of the longest sequence of consecutive integers in an unsorted array. Below is a step-by-step explanation of an efficient O(n) approach using a hash set, followed by the Python code.

Problem Statement





Input: An unsorted array of integers nums (e.g., [100, 4, 200, 1, 3, 2]).



Output: The length of the longest sequence of consecutive integers (e.g., [1, 2, 3, 4] has length 4).



Goal: Return the length of the longest consecutive sequence, handling duplicates and ensuring O(n) time complexity.

Approach: Hash Set Technique

This approach uses a hash set to achieve O(n) time complexity by enabling O(1) lookups to check for consecutive numbers. We only count sequences starting from numbers without a predecessor to avoid redundant work.

Step-by-Step Approach





Handle Empty Input:





If the array is empty, return 0, as no sequence exists.



Convert Array to Hash Set:





Create a hash set from the input array to:





Remove duplicates (duplicates don’t affect sequence length).



Enable O(1) lookups for checking consecutive numbers.



Example: [100, 4, 200, 1, 3, 2] becomes {1, 2, 3, 4, 100, 200}.



Iterate Through Each Number:





For each number num in the set:





Check if num is the start of a sequence by verifying that num-1 is not in the set.



This ensures we process each sequence only from its smallest number.



Count Sequence Length:





If num-1 is not in the set, num is a sequence start.



Initialize current_length = 1 and current_num = num.



While current_num + 1 exists in the set:





Increment current_num and current_length.



Update the maximum sequence length if current_length is larger.



Return the Maximum Length:





Return the longest sequence length found after checking all potential starts.

Example Walkthrough





Input: [100, 4, 200, 1, 3, 2]



Step 1: Create Set:





num_set = {1, 2, 3, 4, 100, 200}



Step 2: Iterate and Check Sequences:





For num = 1: 0 not in set → Start sequence.





Check 2 (in set, length = 2), 3 (in set, length = 3), 4 (in set, length = 4), 5 (not in set).



Sequence: [1, 2, 3, 4], length = 4. Update max_length = 4.



For num = 2: 1 in set → Not a start, skip.



For num = 3: 2 in set → Skip.



For num = 4: 3 in set → Skip.



For num = 100: 99 not in set → Start sequence.





Check 101 (not in set). Sequence: [100], length = 1. max_length stays 4.



For num = 200: 199 not in set → Start sequence.





Check 201 (not in set). Sequence: [200], length = 1. max_length stays 4.



Output: 4 (from sequence [1, 2, 3, 4]).

Why It Works





Hash Set: Provides O(1) lookups to check for num-1 and consecutive numbers.



Sequence Start Check: Only starting from numbers without a predecessor ensures each sequence is counted once.



Duplicate Handling: The set removes duplicates, so they don’t affect the result.



Correctness: All possible sequences are considered by checking each potential start.

Complexity





Time Complexity: O(n)





Creating the set: O(n).



Iterating through the set: O(n).



Each number is checked at most twice (once in the loop, once in sequence counting), ensuring O(n) total lookups.



Space Complexity: O(n) for the hash set, excluding the output.

Edge Cases





Empty array: Return 0.



Single element: Return 1 (e.g., [5] → sequence [5]).



No consecutive numbers: Return 1 (e.g., [1, 3, 5] → longest sequence is [1], [3], or [5]).



Duplicates: Handled by the set (e.g., [1, 1, 1, 2, 3] → sequence [1, 2, 3]).



Large sequences: Works efficiently due to O(n) lookups.


```python
def longestConsecutive(nums):
    # Handle empty input
    if not nums:
        return 0
    
    # Convert array to set for O(1) lookups
    num_set = set(nums)
    max_length = 0
    
    # Check each number as a potential sequence start
    for num in num_set:
        # Only start sequence if num-1 is not in set
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            # Update max length
            max_length = max(max_length, current_length)
    
    return max_length

# Test cases
print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9
print(longestConsecutive([]))  # Output: 0
print(longestConsecutive([1, 1, 1]))  # Output: 1

# Test
```

### 10. Best Time to Buy and Sell Stock
**Problem**: Find maximum profit from buying and selling stock once.

**Time Complexity**: O(n)
**Space Complexity**: O(1)
**Analysis**: Single pass tracking minimum price and maximum profit.

```python
def max_profit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

# Test
print(max_profit([7, 1, 5, 3, 6, 4]))  # Output: 5
```

### 11. Next Permutation
**Problem**: Find next lexicographically greater permutation.

**Time Complexity**: O(n)
**Space Complexity**: O(1)
**Analysis**: Three passes through array with constant operations.

The Next Permutation problem requires rearranging an array of integers into the next lexicographically greater permutation. If no such permutation exists, the array is rearranged to the first permutation (ascending order). Below is a step-by-step explanation of an efficient O(n) approach, followed by the Python code.

Problem Statement





Input: An array of integers nums (e.g., [1, 2, 3]).



Output: Modify nums in-place to the next lexicographically greater permutation (e.g., [1, 3, 2]). If the array is the last permutation (e.g., [3, 2, 1]), rearrange to the first permutation ([1, 2, 3]).



Goal: Perform the transformation in-place with O(n) time complexity.

Approach: In-Place Rearrangement

This approach finds the next permutation by identifying a decreasing point, swapping with the smallest greater element, and reversing the remaining subarray to minimize the increase.

Step-by-Step Approach





Find the First Decreasing Element:





Traverse the array from right to left (from index n-2 to 0).



Find the first index i where nums[i] < nums[i+1].



This indicates that the subarray from i+1 to the end is in descending order, and nums[i] is the element to replace.



If no such i exists, the array is in descending order (last permutation).



Find the Smallest Element Greater than nums[i]:





If i is found, traverse from the end to i+1 to find the smallest index j where nums[j] > nums[i].



This ensures the smallest possible increase in the permutation.



Swap Elements:





Swap nums[i] and nums[j] to form the next permutation’s prefix.



Reverse the Subarray After i:





The subarray from i+1 to the end is in descending order.



Reverse it to ascending order to make it the smallest possible subarray.



Handle Last Permutation:





If no i is found (array is descending), reverse the entire array to get the first permutation.

Example Walkthrough





Input: [1, 2, 3]



Step 1: Find Decreasing Element:





From right: nums[1] = 2 < nums[2] = 3, so i = 1.



Step 2: Find Smallest Greater Element:





From end, find j where nums[j] > nums[1] = 2: nums[2] = 3 > 2, so j = 2.



Step 3: Swap:





Swap nums[1] = 2 and nums[2] = 3: Array becomes [1, 3, 2].



Step 4: Reverse Subarray:





Subarray after i=1 is [2], already sorted (single element).



Output: [1, 3, 2].



Input: [3, 2, 1]



Step 1: No i where nums[i] < nums[i+1] (array is descending).



Step 2: Reverse entire array: [1, 2, 3].



Output: [1, 2, 3].

Why It Works





Lexicographical Order: Swapping nums[i] with the smallest nums[j] > nums[i] ensures a minimal increase.



Subarray Minimization: Reversing the subarray after i makes it ascending, ensuring the smallest possible tail.



Correctness: All permutations are ordered lexicographically, and this algorithm finds the immediate next one.



In-Place: Modifications are done without extra space.

Complexity





Time Complexity: O(n)





Finding i: O(n).



Finding j: O(n).



Reversing subarray: O(n).



Space Complexity: O(1), as all operations are in-place.

Edge Cases





Single element: [1] → No change (only one permutation).



Two elements: [1, 2] → [2, 1], [2, 1] → [1, 2].



Descending order: [3, 2, 1] → [1, 2, 3] (first permutation).



Duplicates: Handled correctly (e.g., [1, 1, 5] → [1, 5, 1]).

```python
def nextPermutation(nums):
    # Step 1: Find first decreasing element from right
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    # Step 2: If i exists, find smallest j where nums[j] > nums[i]
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse subarray from i+1 to end
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Test cases (call modifies nums in-place)
nums1 = [1, 2, 3]
nextPermutation(nums1)
print(nums1)  # Output: [1, 3, 2]

nums2 = [3, 2, 1]
nextPermutation(nums2)
print(nums2)  # Output: [1, 2, 3]

nums3 = [1, 1, 5]
nextPermutation(nums3)
print(nums3)  # Output: [1, 5, 1]

nums4 = [1]
nextPermutation(nums4)
print(nums4)  # Output: [1]
```

### 12. Subarray Sum Equals K
**Problem**: Count number of continuous subarrays whose sum equals k.

**Time Complexity**: O(n)
**Space Complexity**: O(n)
**Analysis**: Single pass with hash map to store prefix sums.

Subarray Sum Equals K: Hash Map Approach and Code

The Subarray Sum Equals K problem requires finding the number of continuous subarrays in an array of integers that sum to a given target k. Below is a step-by-step explanation of an efficient O(n) approach using a hash map with cumulative sums, followed by the Python code.

Problem Statement





Input: An array of integers nums and an integer k (e.g., nums = [1, 1, 1], k = 2).



Output: The number of continuous subarrays whose elements sum to k (e.g., 2 for subarrays [1, 1]).



Goal: Count all valid subarrays efficiently, handling positive and negative integers.

Approach: Hash Map with Cumulative Sum

This approach uses a hash map to track cumulative sums, achieving O(n) time complexity by leveraging the relationship between subarray sums and prefix sums.

Step-by-Step Approach





Initialize Data Structures:





Create a hash map sum_freq to store the frequency of cumulative sums.



Initialize sum_freq[0] = 1 to account for subarrays starting from index 0 that sum to k.



Initialize curr_sum = 0 (running cumulative sum) and count = 0 (number of valid subarrays).



Iterate Through the Array:





For each element nums[i]:





Update curr_sum += nums[i] to include the current element.



Check if curr_sum - k exists in sum_freq. If so, add its frequency to count (each occurrence represents a subarray ending at i with sum k).



Increment the frequency of curr_sum in sum_freq.



Return the Result:





After the loop, return count, the total number of subarrays summing to k.

Example Walkthrough





Input: nums = [1, 1, 1], k = 2



Initialization: sum_freq = {0: 1}, curr_sum = 0, count = 0



Step-by-Step:





Index 0: curr_sum = 0 + 1 = 1





Check curr_sum - k = 1 - 2 = -1 → Not in sum_freq.



Update sum_freq[1] = 1 → sum_freq = {0: 1, 1: 1}



Index 1: curr_sum = 1 + 1 = 2





Check curr_sum - k = 2 - 2 = 0 → sum_freq[0] = 1, so count += 1 (subarray [1, 1]).



Update sum_freq[2] = 1 → sum_freq = {0: 1, 1: 1, 2: 1}



Index 2: curr_sum = 2 + 1 = 3





Check curr_sum - k = 3 - 2 = 1 → sum_freq[1] = 1, so count += 1 (subarray [1, 1]).



Update sum_freq[3] = 1 → sum_freq = {0: 1, 1: 1, 2: 1, 3: 1}



Output: count = 2 (subarrays [1, 1] at indices [0,1] and [1,2]).

Why It Works





Cumulative Sum: A subarray from i to j sums to k if sum[j] - sum[i-1] = k. Thus, we look for sum[j] - k in previous sums.



Hash Map: Stores frequencies of cumulative sums, allowing O(1) lookups to count valid subarrays.



Correctness: All continuous subarrays are considered by tracking cumulative sums and their differences.



Efficiency: Each element is processed once with O(1) hash map operations.

Complexity





Time Complexity: O(n)





Iterate through the array once: O(n).



Hash map operations (lookup and update) are O(1) on average.



Space Complexity: O(n) for the hash map to store cumulative sums.

Edge Cases





Empty array: Return 0 (no subarrays).



Single element: If nums[0] == k, return 1; else 0.



Negative numbers: Handled by cumulative sum (e.g., [1, -1, 1], k = 0 → finds [1, -1]).



Duplicates: Handled correctly by frequency counting.



k = 0: Handled by checking for same cumulative sum (e.g., [1, -1]).



```python
def subarraySum(nums, k):
    # Initialize hash map, cumulative sum, and count
    sum_freq = {0: 1}  # Initialize with 0 sum for subarrays starting at index 0
    curr_sum = 0
    count = 0
    
    # Iterate through the array
    for num in nums:
        curr_sum += num  # Update cumulative sum
        # Check if curr_sum - k exists in sum_freq
        if curr_sum - k in sum_freq:
            count += sum_freq[curr_sum - k]
        # Update frequency of current sum
        sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1
    
    return count

# Test cases
print(subarraySum([1, 1, 1], 2))  # Output: 2
print(subarraySum([1, 2, 3], 3))  # Output: 2
print(subarraySum([1], 0))  # Output: 0
print(subarraySum([1, -1, 1], 0))  # Output: 1
```

---

## Strings (8 Problems)

### 13. Longest Substring Without Repeating Characters
**Problem**: Find length of longest substring without repeating characters.

**Time Complexity**: O(n)
**Space Complexity**: O(min(m, n)) where m is character set size
**Analysis**: Sliding window with hash set, each character visited at most twice.

```python
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test
print(length_of_longest_substring("abcabcbb"))  # Output: 3
```

### 14. Valid Palindrome
**Problem**: Check if string is palindrome (ignoring non-alphanumeric characters).

**Time Complexity**: O(n)
**Space Complexity**: O(1)
**Analysis**: Two pointers from both ends, single pass through string.

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Test
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
```

### 15. Group Anagrams
**Problem**: Group strings that are anagrams of each other.

**Time Complexity**: O(n * k log k) where k is max string length
**Space Complexity**: O(n * k)
**Analysis**: For each string, sorting takes O(k log k), done for n strings.
The Group Anagrams problem requires grouping strings that are anagrams of each other into sublists. Below is a step-by-step explanation of an efficient approach using sorting and a hash map, achieving O(n * k log k) time complexity, followed by the Python code and a clarification on why sorted(s) cannot be used directly as a hash map key.

Problem Statement





Input: An array of strings strs (e.g., ["eat", "tea", "tan", "ate", "nat", "bat"]).



Output: A list of lists, where each sublist contains strings that are anagrams (e.g., [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]).



Goal: Group all anagrams together efficiently, handling empty inputs and duplicates.

Approach: Sorting with Hash Map

This approach sorts each string’s characters to create a key and uses a hash map to group anagrams, matching the specified O(n * k log k) time complexity, where n is the number of strings and k is the maximum string length.

Step-by-Step Approach





Initialize a Hash Map:





Create a hash map anagram_groups where:





Key: The sorted string (characters sorted in ascending order, joined into a string).



Value: A list of strings that share the same sorted characters (anagrams).



Process Each String:





For each string s in strs:





Sort its characters using sorted(s) to get a list of characters (e.g., "eat" → ['a', 'e', 't']).



Join the sorted characters into a string with ''.join(sorted(s)) to create a hashable key (e.g., "aet").



Add the original string to the list associated with this key in the hash map.



Why Not Use sorted(s) Directly?:





sorted(s) returns a list, which is unhashable (mutable) and cannot be a dictionary key.



We need a hashable type like a string (via ''.join(sorted(s))) or tuple (via tuple(sorted(s))) to use as a key.



Return the Result:





Return the values of the hash map as a list of lists, containing all anagram groups.

Example Walkthrough





Input: ["eat", "tea", "tan", "ate", "nat", "bat"]



Step 1: Initialize:





anagram_groups = {}



Step 2: Process Strings:





"eat": sorted("eat") = ['a', 'e', 't'], ''.join(sorted("eat")) = "aet". Add to anagram_groups["aet"] = ["eat"].



"tea": sorted("tea") = ['a', 'e', 't'], ''.join = "aet". Add to anagram_groups["aet"] = ["eat", "tea"].



"tan": sorted("tan") = ['a', 'n', 't'], ''.join = "ant". Add to anagram_groups["ant"] = ["tan"].



"ate": sorted("ate") = ['a', 'e', 't'], ''.join = "aet". Add to anagram_groups["aet"] = ["eat", "tea", "ate"].



"nat": sorted("nat") = ['a', 'n', 't'], ''.join = "ant". Add to anagram_groups["ant"] = ["tan", "nat"].



"bat": sorted("bat") = ['a', 'b', 't'], ''.join = "abt". Add to anagram_groups["abt"] = ["bat"].



Step 3: Return Values:





Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Doubt Clarification: Why Not Use sorted(s) Directly?





Problem with sorted(s):





sorted(s) returns a list of characters (e.g., "eat" → ['a', 'e', 't']).



Lists are mutable and unhashable, so they cannot be used as dictionary keys. Attempting to use anagram_groups[sorted(s)] raises TypeError: unhashable type: 'list'.



Need for Hashable Key:





Dictionary keys must be immutable and hashable (implement __hash__).



Strings and tuples are hashable; lists are not.



''.join(sorted(s)) converts the sorted list to a string (e.g., "aet"), which is hashable and identical for all anagrams.



Alternative: Tuple:





Using tuple(sorted(s)) (e.g., ('a', 'e', 't')) is possible, as tuples are hashable.



However, strings are more concise, memory-efficient, and readable, so ''.join(sorted(s)) is preferred.



Why Convert to String:





Ensures a consistent, hashable key for grouping anagrams.



Example: "eat", "tea", and "ate" all map to "aet", allowing them to be grouped together.

Why It Works





Sorting: Anagrams have identical sorted characters, so sorting provides a unique key for each anagram group.



Hash Map: Groups strings with the same sorted key efficiently.



Correctness: All strings are processed, and anagrams are grouped based on their sorted form.



Uniqueness: The hash map ensures each group contains only anagrams.

Complexity





Time Complexity: O(n * k log k)





Sorting each string of length k: O(k log k).



Processing n strings: O(n * k log k).



Hash map operations are O(1) on average.



Space Complexity: O(n * k)





Hash map stores n strings, each up to k characters.



Additional space for sorted keys is proportional to n * k.

Edge Cases





Empty array: Return [].



Single string: Return [[string]] (e.g., ["a"] → [["a"]]).



Empty strings: Return [[""]] for [""].



Identical strings: Group together (e.g., ["a", "a"] → [["a", "a"]]).



No anagrams: Each string in its own group (e.g., ["a", "b"] → [["a"], ["b"]]).

```python
def group_anagrams(strs):
    anagram_map = {}
    
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagram_map:
            anagram_map[sorted_s] = []
        anagram_map[sorted_s].append(s)
    
    return list(anagram_map.values())

# Test
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

### 16. Longest Palindromic Substring
**Problem**: Find the longest palindromic substring.

**Time Complexity**: O(n²)
**Space Complexity**: O(1)
**Analysis**: For each center, expand palindrome check takes O(n), done for 2n-1 centers.

The Longest Palindromic Substring problem requires finding the longest substring in a string that is a palindrome. Below is a step-by-step explanation of a simple O(n²) expand-around-center approach, followed by the Python code. A brief overview of the O(n) Manacher’s Algorithm is included for reference.

Problem Statement





Input: A string s (e.g., "babad").



Output: The longest substring of s that is a palindrome (e.g., "bab" or "aba").



Goal: Find the longest palindromic substring efficiently, handling single characters, empty strings, and various input types.

Approach: Expand-Around-Center

This approach treats each character and gap between characters as a potential palindrome center, expanding outward to find the longest palindrome. It’s simple and intuitive, with O(n²) time complexity.

Step-by-Step Approach





Initialize Tracking Variables:





Keep track of the start index (start) and maximum length (max_len) of the longest palindrome found.



Iterate Through Centers:





For each index i from 0 to len(s) - 1:





Check for an odd-length palindrome centered at i (e.g., "aba").



Check for an even-length palindrome centered between i and i+1 (e.g., "bb").



Expand Around Center:





For a center (odd or even), expand outward by comparing characters on both sides (left and right) while:





left >= 0 and right < len(s).



s[left] == s[right].



Compute the length of the palindrome: right - left - 1.



Update start and max_len if the current palindrome is longer.



Return the Substring:





Use start and max_len to extract the substring s[start:start + max_len].

Example Walkthrough





Input: "babad"



Step 1: Initialize:





start = 0, max_len = 0



Step 2: Iterate Centers:





i = 0: Center at b (odd): Expand → "b", length = 1. Update start = 0, max_len = 1.



i = 0-1: Gap between b and a (even): No palindrome (no matching characters). Length = 0.



i = 1: Center at a (odd): Expand → "a", length = 1. No update (max_len = 1).



i = 1-2: Gap between a and b: Expand → "aba", length = 3. Update start = 1, max_len = 3.



i = 2: Center at b: Expand → "bab", length = 3. No update (same length, keep first found).



i = 2-3: Gap between b and a: No palindrome. Length = 0.



i = 3: Center at a: Expand → "a", length = 1. No update.



i = 3-4: Gap between a and d: No palindrome. Length = 0.



i = 4: Center at d: Expand → "d", length = 1. No update.



Step 3: Return:





start = 1, max_len = 3 → s[1:4] = "aba"



Output: "aba" (or "bab" if we kept a later palindrome of equal length).

```python
def longest_palindrome(s):
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        # Odd length palindromes
        len1 = expand_around_center(i, i)
        # Even length palindromes
        len2 = expand_around_center(i, i + 1)
        
        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]

# Test
print(longest_palindrome("babad"))  # Output: "bab" or "aba"
```

### 17. String to Integer (atoi)
**Problem**: Convert string to 32-bit signed integer.

**Time Complexity**: O(n)
**Space Complexity**: O(1)
**Analysis**: Single pass through string with constant space operations.

```python
def my_atoi(s):
    s = s.strip()
    if not s:
        return 0
    
    sign = 1
    index = 0
    
    if s[0] == '-':
        sign = -1
        index = 1
    elif s[0] == '+':
        index = 1
    
    result = 0
    while index < len(s) and s[index].isdigit():
        result = result * 10 + int(s[index])
        index += 1
    
    result *= sign
    return max(-2**31, min(2**31 - 1, result))

# Test
print(my_atoi("42"))  # Output: 42
print(my_atoi("   -42"))  # Output: -42
```

### 18. Implement strStr()
**Problem**: Find first occurrence of needle in haystack.

**Time Complexity**: O(n * m) naive, O(n + m) KMP
**Space Complexity**: O(1) naive, O(m) KMP
**Analysis**: Naive approach checks each position. KMP uses failure function for optimization.

```python
def str_str(haystack, needle):
    if not needle:
        return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    
    return -1

# Test
print(str_str("hello", "ll"))  # Output: 2
print(str_str("aaaaa", "bba"))  # Output: -1
```

### 19. Minimum Window Substring
**Problem**: Find minimum window substring containing all characters of t.

**Time Complexity**: O(n + m)
**Space Complexity**: O(n + m)
**Analysis**: Sliding window with character frequency maps, each character processed at most twice.

The Minimum Window Substring problem requires finding the smallest substring in string s that contains all characters of string t (including duplicates). Below is a step-by-step explanation of an efficient O(n + m) sliding window approach using hash maps, followed by the Python code.

Problem Statement





Input: Two strings s and t (e.g., s = "ADOBECODEBANC", t = "ABC").



Output: The smallest substring of s containing all characters of t with their required frequencies (e.g., "BANC"). If no such substring exists, return "".



Goal: Find the minimum window efficiently, handling case sensitivity and duplicates.

Approach: Sliding Window with Hash Map

This approach uses a sliding window with two hash maps to track character frequencies, achieving O(n + m) time complexity, where n = len(s) and m = len(t). Each character is processed at most twice (when added and removed from the window).

Step-by-Step Approach





Handle Edge Cases:





If len(s) < len(t), return "" (no possible window).



If t is empty, return "".



Build Frequency Map for t:





Create a hash map t_freq to store the frequency of each character in t.



Track the number of unique characters in t (required).



Initialize Sliding Window:





Create a hash map window_freq for the current window’s character frequencies.



Initialize pointers left and right to 0.



Track matched (number of characters in the window matching t’s required frequency).



Track the minimum window’s start index (min_start) and length (min_len).



Expand the Window:





Move right to include characters in the window.



Update window_freq for each character.



If the character is in t_freq and its frequency in the window meets or exceeds t_freq, increment matched.



Shrink the Window:





When matched == required (window contains all characters of t):





Shrink the window by moving left while maintaining validity.



Update window_freq and matched as characters are removed.



If the current window is smaller than min_len, update min_start and min_len.



Return the Result:





If min_len is infinity (no valid window found), return "".



Otherwise, return s[min_start:min_start + min_len].

Example Walkthrough





Input: s = "ADOBECODEBANC", t = "ABC"



Step 1: Initialize:





t_freq = {'A': 1, 'B': 1, 'C': 1}, required = 3



window_freq = {}, matched = 0, left = 0, right = 0



min_start = 0, min_len = float('inf')



Step 2: Slide Window:





right = 0: s[0] = A, window_freq = {'A': 1}, matched = 1 (A matches).



right = 1: s[1] = D, window_freq = {'A': 1, 'D': 1}, no change in matched.



right = 2: s[2] = O, window_freq = {'A': 1, 'D': 1, 'O': 1}.



right = 3: s[3] = B, window_freq = {'A': 1, 'D': 1, 'O': 1, 'B': 1}, matched = 2 (B matches).



right = 4: s[4] = E, window_freq = {'A': 1, 'D': 1, 'O': 1, 'B': 1, 'E': 1}.



right = 5: s[5] = C, window_freq = {'A': 1, 'D': 1, 'O': 1, 'B': 1, 'E': 1, 'C': 1}, matched = 3 (C matches).



Valid window (matched == required): Window = "ADOBEC", length = 6. Update min_start = 0, min_len = 6.



Shrink: Move left:





left = 0: Remove A, window_freq['A'] = 0, matched = 2 (A no longer matches). Window invalid.



right = 6: s[6] = O, window_freq['O'] = 2.



Continue until right = 10: s[10] = B, window_freq = {'A': 1, 'D': 1, 'O': 2, 'B': 2, 'E': 1, 'C': 1, 'N': 1}, matched = 3.



Valid window: "DOBECODEBANC", length = 12. No update (larger than 6).



Shrink: Move left until left = 9 (remove D, O, B, E, C, O, D, E, B):





Window = "BANC", window_freq = {'A': 1, 'N': 1, 'C': 1, 'B': 1}, matched = 3, length = 4.



Update min_start = 9, min_len = 4.



Continue until right reaches end, no smaller window found.



Output: s[9:13] = "BANC"

Why It Works





Sliding Window: Ensures all valid substrings are considered by expanding until valid and shrinking to minimize.



Hash Maps: Track required and current frequencies efficiently, allowing O(1) checks for validity.



Correctness: The matched counter ensures the window contains all characters of t with correct frequencies.



Minimality: Shrinking the window whenever valid ensures the smallest window is found.

Complexity





Time Complexity: O(n + m)





Building t_freq: O(m).



Sliding window: Each character in s is added (right moves) and removed (left moves) at most once, so O(n).



Hash map operations: O(1) on average.



Space Complexity: O(n + m)





t_freq: O(m) for characters in t.



window_freq: O(n) for characters in the window (worst case, all unique).



Additional variables: O(1).

Edge Cases





Empty t: Return "".



Empty s or len(s) < len(t): Return "".



Single character: If s = "a", t = "a", return "a"; if t = "aa", return "".



No valid window: Return "" (e.g., s = "ab", t = "A").



Duplicates in t: Handled by frequency counts (e.g., s = "aaa", t = "aa" → "aa").


```python
def min_window(s, t):
    if not s or not t:
        return ""
    
    # Character frequency in t
    t_count = {}
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1
    
    required = len(t_count)
    formed = 0
    window_counts = {}
    
    left, right = 0, 0
    ans = float("inf"), None, None
    
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1
        
        while left <= right and formed == required:
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            char = s[left]
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

# Test
print(min_window("ADOBECODEBANC", "ABC"))  # Output: "BANC"
```

### 20. Regular Expression Matching
**Problem**: Implement regular expression matching with '.' and '*'.

**Time Complexity**: O(n * m)
**Space Complexity**: O(n * m)
**Analysis**: Dynamic programming with 2D table, each cell computed once.

```python
def is_match(s, p):
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, a*b*c*
    for j in range(2, len(p) + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-2]  # Zero occurrences
                if p[j-2] == s[i-1] or p[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]  # One or more
            elif p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
    
    return dp[len(s)][len(p)]

# Test
print(is_match("aa", "a"))  # Output: False
print(is_match("aa", "a*"))  # Output: True
```

---

## Linked Lists (6 Problems)

### 21. Reverse Linked List
**Problem**: Reverse a singly linked list.

**Time Complexity**: O(n)
**Space Complexity**: O(1) iterative, O(n) recursive
**Analysis**: Visit each node once, constant space for pointers.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# Test helper function
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = reverse_list(head)
print(print_list(reversed_head))  # Output: [5, 4, 3, 2, 1]
```

### 22. Merge Two Sorted Lists
**Problem**: Merge two sorted linked lists.

**Time Complexity**: O(n + m)
**Space Complexity**: O(1)
**Analysis**: Visit each node once from both lists, constant extra space.

```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 or l2
    return dummy.next

# Test
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
merged = merge_two_lists(l1, l2)
print(print_list(merged))  # Output: [1, 1, 2, 3, 4, 4]
```

### 23. Add Two Numbers
**Problem**: Add two numbers represented as linked lists.

**Time Complexity**: O(max(n, m))
**Space Complexity**: O(max(n, m))
**Analysis**: Process each digit once, space for result list.

```python
def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        current.next = ListNode(digit)
        current = current.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next

# Test
l1 = ListNode(2, ListNode(4, ListNode(3)))  # 342
l2 = ListNode(5, ListNode(6, ListNode(4)))  # 465
result = add_two_numbers(l1, l2)
print(print_list(result))  # Output: [7, 0, 8] (807)
```

### 24. Remove Nth Node From End
**Problem**: Remove nth node from end of linked list.

**Time Complexity**: O(n)
**Space Complexity**: O(1)
**Analysis**: Two-pointer technique, single pass through list.

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    
    # Move first n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    return dummy.next

# Test
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = remove_nth_from_end(head, 2)
print(print_list(result))  # Output: [1, 2, 3, 5]
```

### 25. Linked List Cycle
**Problem**: Detect if linked list has a cycle.

**Time Complexity**: O(n)
**Space Complexity**: O(1)
**Analysis**: Floyd's cycle detection (tortoise and hare), each node visited at most twice.

```python
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False

# Test (creating cycle manually)
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Create cycle
print(has_cycle(head))  # Output: True
```

### 26. Intersection of Two Linked Lists
**Problem**: Find the intersection node of two linked lists.

**Time Complexity**: O(n + m)
**Space Complexity**: O(1)
**Analysis**: Two pointers traverse both lists, alignment achieved after one full traversal.

```python
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    
    pointerA = headA
    pointerB = headB
    
    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA
    
    return pointerA

# Test requires setting up intersection manually
```

---

## Stacks (4 Problems)

### 27. Valid Parentheses
**Problem**: Check if string has valid parentheses.

**Time Complexity**: O(n)
**Space Complexity**: O(n)
**Analysis**: Single pass through string, stack size at most n/2.

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack

# Test
print(is_valid("()"))  # Output: True
print(is_valid("()[]{}"))  # Output: True
print(is_valid("(]"))  # Output: False
```

### 28. Min Stack
**Problem**: Design stack supporting push, pop, top, and getMin in O(1).

**Time Complexity**: O(1) for all operations
**Space Complexity**: O(n)
**Analysis**: Each operation performs constant work, auxiliary stack tracks minimums.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

# Test
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())  # Output: -3
min_stack.pop()
print(min_stack.top())      # Output: 0
print(min_stack.get_min())  # Output: -2
```

### 29. Evaluate Reverse Polish Notation
**Problem**: Evaluate arithmetic expression in postfix notation.

**Time Complexity**: O(n)
**Space Complexity**: O(n)
**Analysis**: Single pass through tokens, stack operations are O(1).

```python
def eval_rpn(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # token == '/'
                result = int(a / b)  # Truncate towards zero
            
            stack.append(result)
        else:
            stack.append(int(token))
    
    return stack[0]

# Test
print(eval_rpn(["2", "1", "+", "3", "*"]))  # Output: 9
print(eval_rpn(["4", "13", "5", "/", "+"]))  # Output: 6
```

### 30. Largest Rectangle in Histogram
**Problem**: Find area of largest rectangle in histogram.

**Time Complexity**: O(n)
**Space Complexity**: O(n)
**Analysis**: Each bar pushed and popped at most once from stack.

```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    while stack:
        h = heights[stack.pop()]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)
    
    return max_area

# Test
print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # Output: 10

---

## Queues (3 Problems)

### 31. Implement Queue using Stacks
**Problem**: Implement queue using stack operations.

**Time Complexity**: O(1) amortized for all operations
**Space Complexity**: O(n)
**Analysis**: Each element moved at most twice between stacks, amortized O(1).

```python
class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []
    
    def push(self, x):
        self.input_stack.append(x)
    
    def pop(self):
        self._move_to_output()
        return self.output_stack.pop()
    
    def peek(self):
        self._move_to_output()
        return self.output_stack[-1]
    
    def empty(self):
        return len(self.input_stack) == 0 and len(self.output_stack) == 0
    
    def _move_to_output(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

# Test
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())  # Output: 1
print(queue.pop())   # Output: 1
print(queue.empty()) # Output: False
```

### 32. Sliding Window Maximum
**Problem**: Find maximum in each sliding window of size k.

**Time Complexity**: O(n)
**Space Complexity**: O(k)
**Analysis**: Each element added and removed from deque at most once.

```python
from collections import deque

def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []
    
    dq = deque()  # Store indices
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add maximum to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# Test
print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3, 3, 5, 5, 6, 7]
```

### 33. Design Circular Queue
**Problem**: Design a circular queue with fixed size.

**Time Complexity**: O(1) for all operations
**Space Complexity**: O(k)
**Analysis**: All operations use array indexing, constant time.

```python
class MyCircularQueue:
    def __init__(self, k):
        self.queue = [0] * k
        self.head = 0
        self.count = 0
        self.capacity = k
    
    def enqueue(self, value):
        if self.is_full():
            return False
        self.queue[(self.head + self.count) % self.capacity] = value
        self.count += 1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True
    
    def front(self):
        if self.is_empty():
            return -1
        return self.queue[self.head]
    
    def rear(self):
        if self.is_empty():
            return -1
        return self.queue[(self.head + self.count - 1) % self.capacity]
    
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.capacity

# Test
cq = MyCircularQueue(3)
print(cq.enqueue(1))  # Output: True
print(cq.enqueue(2))  # Output: True
print(cq.enqueue(3))  # Output: True
print(cq.enqueue(4))  # Output: False
print(cq.rear())      # Output: 3
```

---

## Hash Tables/Hash Maps (5 Problems)

### 34. Two Sum
**Problem**: Find indices of two numbers that add up to target.

**Time Complexity**: O(n)
**Space Complexity**: O(n)
**Analysis**: Hash table lookup and insertion are O(1) average case.

```python
def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

# Test
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
```

### 35. Top K Frequent Elements
**Problem**: Find k most frequent elements.

**Time Complexity**: O(n log k)
**Space Complexity**: O(n + k)
**Analysis**: Count frequencies O(n), heap operations O(n log k).

```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# Alternative bucket sort approach: O(n) time
def top_k_frequent_bucket(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in count.items():
        buckets[freq].append(num)
    
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result

# Test
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # Output: [1, 2]
```

### 36. Happy Number
**Problem**: Determine if number eventually reaches 1 through sum of squares.

**Time Complexity**: O(log n)
**Space Complexity**: O(log n)
**Analysis**: Cycle detection using hash set, numbers get smaller quickly.

```python
def is_happy(n):
    def get_sum_of_squares(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_sum_of_squares(n)
    
    return n == 1

# Test
print(is_happy(19))  # Output: True
print(is_happy(2))   # Output: False
```

### 37. Isomorphic Strings
**Problem**: Check if two strings are isomorphic.

**Time Complexity**: O(n)
**Space Complexity**: O(1) - at most 256 characters
**Analysis**: Single pass with two hash maps for bidirectional mapping.

```python
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for i in range(len(s)):
        char_s, char_t = s[i], t[i]
        
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True

# Test
print(is_isomorphic("egg", "add"))  # Output: True
print(is_isomorphic("foo", "bar"))  # Output: False
```

### 38. Word Pattern
**Problem**: Check if string follows the same pattern.

**Time Complexity**: O(n)
**Space Complexity**: O(n)
**Analysis**: Single pass with hash maps for bidirectional mapping.

```python
def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    pattern_to_word = {}
    word_to_pattern = {}
    
    for i in range(len(pattern)):
        char, word = pattern[i], words[i]
        
        if char in pattern_to_word:
            if pattern_to_word[char] != word:
                return False
        else:
            pattern_to_word[char] = word
        
        if word in word_to_pattern:
            if word_to_pattern[word] != char:
                return False
        else:
            word_to_pattern[word] = char
    
    return True

# Test
print(word_pattern("abba", "dog cat cat dog"))  # Output: True
print(word_pattern("abba", "dog cat cat fish")) # Output: False
```

---

## Binary Trees (8 Problems)

### 39. Maximum Depth of Binary Tree
**Problem**: Find maximum depth of binary tree.

**Time Complexity**: O(n)
**Space Complexity**: O(h) where h is height
**Analysis**: Visit each node once, recursion stack depth equals tree height.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1

# Test
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(max_depth(root))  # Output: 3
```

### 40. Validate Binary Search Tree
**Problem**: Check if tree is valid BST.

**Time Complexity**: O(n)
**Space Complexity**: O(h)
**Analysis**: Visit each node once with bounds checking.

```python
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

# Test
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(is_valid_bst(root))  # Output: True
```

### 41. Binary Tree Level Order Traversal
**Problem**: Return level order traversal of binary tree.

**Time Complexity**: O(n)
**Space Complexity**: O(w) where w is maximum width
**Analysis**: BFS traversal, queue size at most width of tree.

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Test
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(level_order(root))  # Output: [[3], [9, 20], [15, 7]]
```

### 42. Symmetric Tree
**Problem**: Check if tree is symmetric around center.

**Time Complexity**: O(n)
**Space Complexity**: O(h)
**Analysis**: Compare corresponding nodes, recursion depth equals height.

```python
def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    return not root or is_mirror(root.left, root.right)

# Test
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))
print(is_symmetric(root))  # Output: True
```

### 43. Binary Tree Inorder Traversal
**Problem**: Return inorder traversal of binary tree.

**Time Complexity**: O(n)
**Space Complexity**: O(h) recursive, O(n) iterative
**Analysis**: Visit each node once, stack/recursion for tree traversal.

```python
def inorder_traversal(root):
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result

# Iterative approach
def inorder_traversal_iterative(root):
    result = []
    stack = []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result

# Test
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(inorder_traversal(root))  # Output: [1, 3, 2]
```

### 44. Path Sum
**Problem**: Check if tree has root-to-leaf path with given sum.

**Time Complexity**: O(n)
**Space Complexity**: O(h)
**Analysis**: DFS traversal, visit each node once.

```python
def has_path_sum(root, target_sum):
    if not root:
        return False
    
    if not root.left and not root.right:  # Leaf node
        return root.val == target_sum
    
    remaining_sum = target_sum - root.val
    return (has_path_sum(root.left, remaining_sum) or 
            has_path_sum(root.right, remaining_sum))

# Test
root = TreeNode(5)
root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None)
root.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
print(has_path_sum(root, 22))  # Output: True
```

### 45. Lowest Common Ancestor
**Problem**: Find lowest common ancestor in BST.

**Time Complexity**: O(h)
**Space Complexity**: O(1) iterative, O(h) recursive
**Analysis**: Binary search tree property allows efficient navigation.

```python
def lowest_common_ancestor(root, p, q):
    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right
        elif p.val < root.val and q.val < root.val:
            root = root.left
        else:
            return root
    return None

# Test requires creating nodes p and q
```

### 46. Convert Sorted Array to BST
**Problem**: Convert sorted array to height-balanced BST.

**Time Complexity**: O(n)
**Space Complexity**: O(log n) for recursion
**Analysis**: Each element used once, balanced tree construction.

```python
def sorted_array_to_bst(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])
    
    return root

# Test
nums = [-10, -3, 0, 5, 9]
root = sorted_array_to_bst(nums)
print(level_order(root))  # Output: [[0], [-3, 9], [-10, None, 5]]
```

---

## Heaps (3 Problems)

### 47. Kth Largest Element in Array
**Problem**: Find kth largest element in unsorted array.

**Time Complexity**: O(n log k)
**Space Complexity**: O(k)
**Analysis**: Maintain min-heap of size k, each operation O(log k).

```python
import heapq

def find_kth_largest(nums, k):
    # Min heap of size k
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]

# Alternative: Quick Select O(n) average case
def find_kth_largest_quickselect(nums, k):
    def quickselect(left, right, k_smallest):
        if left == right:
            return nums[left]
        
        pivot_index = partition(left, right)
        
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)
    
    def partition(left, right):
        pivot = nums[right]
        i = left
        
        for j in range(left, right):
            if nums[j] >= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        nums[i], nums[right] = nums[right], nums[i]
        return i
    
    return quickselect(0, len(nums) - 1, k - 1)

# Test
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
```

### 48. Merge k Sorted Lists
**Problem**: Merge k sorted linked lists.

**Time Complexity**: O(n log k) where n is total nodes
**Space Complexity**: O(k) for heap
**Analysis**: Heap operations O(log k), performed for each of n nodes.

```python
import heapq

def merge_k_lists(lists):
    heap = []
    
    # Initialize heap with first node from each list
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# Test requires creating multiple linked lists
```

### 49. Find Median from Data Stream
**Problem**: Design data structure to find median from stream.

**Time Complexity**: O(log n) for add, O(1) for find
**Space Complexity**: O(n)
**Analysis**: Two heaps balanced, heap operations O(log n).

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # Lower half (negated for max heap)
        self.min_heap = []  # Upper half
    
    def add_num(self, num):
        # Add to max_heap first
        heapq.heappush(self.max_heap, -num)
        
        # Balance: move largest from max_heap to min_heap
        if self.max_heap:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # Keep max_heap size >= min_heap size
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

# Test
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
print(mf.find_median())  # Output: 1.5
mf.add_num(3)
print(mf.find_median())  # Output: 2.0
```

---

## Graphs (3 Problems)

### 50. Number of Islands
**Problem**: Count number of islands in 2D grid.

**Time Complexity**: O(m × n)
**Space Complexity**: O(m × n) worst case for recursion
**Analysis**: DFS/BFS visits each cell at most once.

```python
def num_islands(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            grid[r][c] != '1'):
            return
        
        grid[r][c] = '0'  # Mark as visited
        
        # Visit all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
    
    return islands

# Test
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(num_islands(grid))  # Output: 1
```

## Summary

This comprehensive collection covers all major data structures:

- **Arrays (12)**: Fundamental operations, two pointers, sliding window, binary search
- **Strings (8)**: Pattern matching, palindromes, sliding window, dynamic programming  
- **Linked Lists (6)**: Pointer manipulation, cycle detection, merging
- **Stacks (4)**: LIFO operations, monotonic stack, expression evaluation
- **Queues (3)**: FIFO operations, sliding window, circular implementation
- **Hash Tables (5)**: Fast lookups, frequency counting, pattern matching
- **Binary Trees (8)**: Traversals, validation, path problems, construction
- **Heaps (3)**: Priority queues, k-largest problems, data streams
- **Graphs (1)**: DFS/BFS traversal, connectivity problems

### Key Time Complexity Patterns:
- **O(1)**: Hash table access, array indexing, heap top
- **O(log n)**: Binary search, balanced tree operations, heap operations  
- **O(n)**: Linear search, tree traversal, single pass algorithms
- **O(n log n)**: Sorting, heap construction, divide and conquer
- **O(n²)**: Nested loops, some dynamic programming solutions

Each problem includes detailed complexity analysis explaining why the algorithm achieves its time and space bounds, helping you understand the underlying principles for solving similar problems.