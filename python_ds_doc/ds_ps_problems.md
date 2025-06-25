# 30 Easy Data Structures & Problem-Solving Questions

## Arrays (10 Questions)

### 1. Two Sum
**Problem**: Given an array of integers and a target sum, return indices of two numbers that add up to the target.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

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

### 2. Find Maximum Element
**Problem**: Find the maximum element in an array.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

# Test
print(find_max([3, 1, 4, 1, 5, 9]))  # Output: 9
```

### 3. Remove Duplicates from Sorted Array
**Problem**: Remove duplicates from a sorted array in-place.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    
    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index

# Test
nums = [1, 1, 2, 2, 3, 4, 4]
length = remove_duplicates(nums)
print(nums[:length])  # Output: [1, 2, 3, 4]
```

### 4. Rotate Array
**Problem**: Rotate array to the right by k steps.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

# Test
nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array(nums, 3)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
```

### 5. Contains Duplicate
**Problem**: Check if array contains any duplicates.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test
print(contains_duplicate([1, 2, 3, 1]))  # Output: True
print(contains_duplicate([1, 2, 3, 4]))  # Output: False
```

### 6. Move Zeros
**Problem**: Move all zeros to the end while maintaining relative order of non-zero elements.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def move_zeros(nums):
    write_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write_index] = nums[i]
            write_index += 1
    
    for i in range(write_index, len(nums)):
        nums[i] = 0

# Test
nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
```

### 7. Single Number
**Problem**: Find the number that appears only once (all others appear twice).

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR operation
    return result

# Test
print(single_number([2, 2, 1]))  # Output: 1
print(single_number([4, 1, 2, 1, 2]))  # Output: 4
```

### 8. Plus One
**Problem**: Add one to a number represented as array of digits.

**Time Complexity**: O(n)  
**Space Complexity**: O(1) average case

```python
def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# Test
print(plus_one([1, 2, 3]))  # Output: [1, 2, 4]
print(plus_one([9, 9, 9]))  # Output: [1, 0, 0, 0]
```

### 9. Valid Mountain Array
**Problem**: Check if array is a valid mountain (strictly increasing then strictly decreasing).

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def valid_mountain_array(arr):
    if len(arr) < 3:
        return False
    
    i = 0
    # Walk up
    while i < len(arr) - 1 and arr[i] < arr[i + 1]:
        i += 1
    
    # Peak can't be first or last element
    if i == 0 or i == len(arr) - 1:
        return False
    
    # Walk down
    while i < len(arr) - 1 and arr[i] > arr[i + 1]:
        i += 1
    
    return i == len(arr) - 1

# Test
print(valid_mountain_array([2, 1]))  # Output: False
print(valid_mountain_array([3, 5, 5]))  # Output: False
print(valid_mountain_array([0, 3, 2, 1]))  # Output: True
```

### 10. Merge Sorted Arrays
**Problem**: Merge two sorted arrays into one sorted array.

**Time Complexity**: O(m + n)  
**Space Complexity**: O(m + n)

```python
def merge_sorted_arrays(nums1, nums2):
    result = []
    i = j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    
    result.extend(nums1[i:])
    result.extend(nums2[j:])
    return result

# Test
print(merge_sorted_arrays([1, 2, 3], [2, 5, 6]))  # Output: [1, 2, 2, 3, 5, 6]
```

---

## Strings (8 Questions)

### 11. Reverse String
**Problem**: Reverse a string in-place.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Test
s = ["h", "e", "l", "l", "o"]
reverse_string(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']
```

### 12. Valid Anagram
**Problem**: Check if two strings are anagrams.

**Time Complexity**: O(n)  
**Space Complexity**: O(1) - fixed alphabet size

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    return len(char_count) == 0

# Test
print(is_anagram("anagram", "nagaram"))  # Output: True
print(is_anagram("rat", "car"))  # Output: False
```

### 13. Valid Palindrome
**Problem**: Check if a string is a palindrome (considering only alphanumeric characters).

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

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
print(is_palindrome("race a car"))  # Output: False
```

### 14. First Unique Character
**Problem**: Find the first non-repeating character in a string.

**Time Complexity**: O(n)  
**Space Complexity**: O(1) - fixed alphabet size

```python
def first_uniq_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1

# Test
print(first_uniq_char("leetcode"))  # Output: 0
print(first_uniq_char("loveleetcode"))  # Output: 2
```

### 15. String to Integer (atoi)
**Problem**: Convert string to 32-bit signed integer.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def string_to_integer(s):
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
print(string_to_integer("42"))  # Output: 42
print(string_to_integer("   -42"))  # Output: -42
```

### 16. Longest Common Prefix
**Problem**: Find the longest common prefix among array of strings.

**Time Complexity**: O(S) where S is sum of all characters  
**Space Complexity**: O(1)

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Test
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))  # Output: ""
```

### 17. Count and Say
**Problem**: Generate the nth term of count-and-say sequence.

**Time Complexity**: O(n * m) where m is length of string  
**Space Complexity**: O(m)

```python
def count_and_say(n):
    if n == 1:
        return "1"
    
    result = "1"
    for _ in range(n - 1):
        next_result = ""
        i = 0
        while i < len(result):
            count = 1
            current_char = result[i]
            while i + 1 < len(result) and result[i + 1] == current_char:
                count += 1
                i += 1
            next_result += str(count) + current_char
            i += 1
        result = next_result
    
    return result

# Test
print(count_and_say(1))  # Output: "1"
print(count_and_say(4))  # Output: "1211"
```

### 18. Valid Parentheses
**Problem**: Check if string has valid parentheses.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

```python
def is_valid_parentheses(s):
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
print(is_valid_parentheses("()"))  # Output: True
print(is_valid_parentheses("()[]{}"))  # Output: True
print(is_valid_parentheses("(]"))  # Output: False
```

---

## Linked Lists (4 Questions)

### 19. Reverse Linked List
**Problem**: Reverse a singly linked list.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

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

# Test
# Create: 1 -> 2 -> 3 -> None
head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = reverse_list(head)
# Result: 3 -> 2 -> 1 -> None
```

### 20. Delete Node in Linked List
**Problem**: Delete a node (except tail) in a singly linked list, given only access to that node.

**Time Complexity**: O(1)  
**Space Complexity**: O(1)

```python
def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next

# Test requires linked list setup
```

### 21. Remove Nth Node From End
**Problem**: Remove nth node from the end of linked list.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

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

# Test requires linked list setup
```

### 22. Merge Two Sorted Lists
**Problem**: Merge two sorted linked lists.

**Time Complexity**: O(n + m)  
**Space Complexity**: O(1)

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

# Test requires linked list setup
```

---

## Stacks and Queues (3 Questions)

### 23. Implement Stack using Queues
**Problem**: Implement stack using queue operations.

**Time Complexity**: O(n) for push, O(1) for pop  
**Space Complexity**: O(n)

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        self.queue.append(x)
        # Rotate queue to make last element first
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        return self.queue.popleft()
    
    def top(self):
        return self.queue[0]
    
    def empty(self):
        return len(self.queue) == 0

# Test
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())  # Output: 2
print(stack.pop())  # Output: 2
```

### 24. Implement Queue using Stacks
**Problem**: Implement queue using stack operations.

**Time Complexity**: O(1) amortized for all operations  
**Space Complexity**: O(n)

```python
class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []
    
    def push(self, x):
        self.input_stack.append(x)
    
    def pop(self):
        self._move_elements()
        return self.output_stack.pop()
    
    def peek(self):
        self._move_elements()
        return self.output_stack[-1]
    
    def empty(self):
        return len(self.input_stack) == 0 and len(self.output_stack) == 0
    
    def _move_elements(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

# Test
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())  # Output: 1
print(queue.pop())   # Output: 1
```

### 25. Min Stack
**Problem**: Design a stack that supports push, pop, top, and retrieving minimum element in constant time.

**Time Complexity**: O(1) for all operations  
**Space Complexity**: O(n)

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
```

---

## Hash Tables (3 Questions)

### 26. Two Sum (Hash Table)
**Problem**: Find two numbers that add up to target using hash table.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

```python
def two_sum_hash(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

# Test
print(two_sum_hash([2, 7, 11, 15], 9))  # Output: [0, 1]
```

### 27. Happy Number
**Problem**: Determine if a number is happy (sum of squares of digits eventually equals 1).

**Time Complexity**: O(log n)  
**Space Complexity**: O(log n)

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

### 28. Group Anagrams
**Problem**: Group strings that are anagrams of each other.

**Time Complexity**: O(n * k log k) where k is max length of string  
**Space Complexity**: O(n * k)

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

---

## Trees (2 Questions)

### 29. Maximum Depth of Binary Tree
**Problem**: Find the maximum depth of a binary tree.

**Time Complexity**: O(n)  
**Space Complexity**: O(h) where h is height of tree

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
# Create tree: 3
#             / \
#            9  20
#              /  \
#             15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(max_depth(root))  # Output: 3
```

### 30. Symmetric Tree
**Problem**: Check if a binary tree is symmetric around its center.

**Time Complexity**: O(n)  
**Space Complexity**: O(h)

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
# Create symmetric tree: 1
#                       / \
#                      2   2
#                     / \ / \
#                    3  4 4  3
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))
print(is_symmetric(root))  # Output: True
```

---

## Summary

This collection covers fundamental data structure problems across:
- **Arrays**: Basic operations, two pointers, sliding window
- **Strings**: Character manipulation, pattern matching
- **Linked Lists**: Node manipulation, two pointers
- **Stacks/Queues**: LIFO/FIFO operations, design problems
- **Hash Tables**: Fast lookups, counting, grouping
- **Trees**: Traversal, depth calculation, symmetry

Each problem includes:
- Clear problem statement
- Time and space complexity analysis
- Clean Python implementation
- Test cases with expected outputs

These problems form a solid foundation for understanding basic algorithms and data structures, commonly asked in coding interviews and helpful for building problem-solving skills.