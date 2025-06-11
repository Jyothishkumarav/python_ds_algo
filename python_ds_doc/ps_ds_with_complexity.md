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

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)
    
    return merged

# Test
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
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

```python
def longest_consecutive(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        if num - 1 not in num_set:  # Start of sequence
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            longest = max(longest, current_length)
    
    return longest

# Test
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
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

```python
def next_permutation(nums):
    # Find the largest index i such that nums[i] < nums[i + 1]
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        # Find the largest index j such that nums[i] < nums[j]
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
    # Reverse the suffix starting at nums[i + 1]
    nums[i + 1:] = reversed(nums[i + 1:])

# Test
nums = [1, 2, 3]
next_permutation(nums)
print(nums)  # Output: [1, 3, 2]
```

### 12. Subarray Sum Equals K
**Problem**: Count number of continuous subarrays whose sum equals k.

**Time Complexity**: O(n)
**Space Complexity**: O(n)
**Analysis**: Single pass with hash map to store prefix sums.

```python
def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # Handle subarrays starting from index 0
    
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count

# Test
print(subarray_sum([1, 1, 1], 2))  # Output: 2
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