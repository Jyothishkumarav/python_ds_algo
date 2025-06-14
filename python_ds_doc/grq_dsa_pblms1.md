50 Data Structures and Algorithms Interview Questions and Solutions
This document provides 50 carefully selected Data Structures and Algorithms (DSA) questions focusing on arrays, stacks, queues, hashmaps, sets, lists, and linked lists. Each question includes a problem statement, a detailed approach, time and space complexity analysis, and a Python code solution to help you prepare for software engineering interviews.

Arrays
1. Find the Second Largest Element in an Array
Problem: Given an array of integers, find the second largest element.
Approach:

Iterate through the array once, keeping track of the largest and second largest elements.
If the current element is greater than the largest, update second largest to be the current largest and largest to the current element.
If the current element is between the largest and second largest, update only the second largest.

Complexity:

Time: O(n) - single pass through the array.
Space: O(1) - only two variables are used.

def find_second_largest(arr):
    if len(arr) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None


2. Rotate an Array by k Positions
Problem: Rotate an array to the right by k steps.
Approach:

Use the reversal algorithm: 
Reverse the entire array.
Reverse the first k elements.
Reverse the remaining n-k elements.


Handle k > n by taking k = k % n.

Complexity:

Time: O(n) - three reversals.
Space: O(1) - in-place reversal.

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, k):
    if not arr:
        return
    n = len(arr)
    k = k % n
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)


3. Find the Missing Number in an Array
Problem: Given an array of n-1 integers in the range [1, n], find the missing number.
Approach:

Calculate the expected sum of numbers from 1 to n using the formula n*(n+1)/2.
Subtract the sum of the array elements from the expected sum to find the missing number.

Complexity:

Time: O(n) - single pass to compute the array sum.
Space: O(1) - constant space.

def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


4. Merge Two Sorted Arrays
Problem: Merge two sorted arrays into a single sorted array.
Approach:

Use two pointers to compare elements from both arrays and build the result array.
Append remaining elements from either array if one is exhausted.

Complexity:

Time: O(n + m) - where n and m are the lengths of the input arrays.
Space: O(n + m) - for the result array.

def merge_sorted_arrays(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


5. Find the Maximum Subarray Sum (Kadane’s Algorithm)
Problem: Find the maximum sum of a contiguous subarray.
Approach:

Use Kadane’s algorithm: maintain a current sum and a global maximum sum.
For each element, decide to start a new subarray or extend the existing one.

Complexity:

Time: O(n) - single pass through the array.
Space: O(1) - constant space.

def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


6. Find Duplicates in an Array
Problem: Given an array of integers in the range [1, n], find all duplicates.
Approach:

Use the array as a hash table by marking indices (negating values).
If an index is already negative, the corresponding number is a duplicate.

Complexity:

Time: O(n) - single pass.
Space: O(1) - modifies the array in-place.

def find_duplicates(arr):
    result = []
    for num in arr:
        index = abs(num) - 1
        if arr[index] > 0:
            arr[index] = -arr[index]
        else:
            result.append(abs(num))
    return result


7. Move Zeros to End
Problem: Move all zeros to the end of the array while maintaining the relative order of non-zero elements.
Approach:

Use a pointer to track the position for the next non-zero element.
Move all non-zero elements to the front, then fill the rest with zeros.

Complexity:

Time: O(n) - single pass.
Space: O(1) - in-place.

def move_zeros(arr):
    non_zero_pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_pos], arr[i] = arr[i], arr[non_zero_pos]
            non_zero_pos += 1


8. Find the First Non-Repeating Element
Problem: Find the first element in an array that appears only once.
Approach:

Use a hashmap to count the frequency of each element.
Iterate through the array again to find the first element with a count of 1.

Complexity:

Time: O(n) - two passes through the array.
Space: O(n) - hashmap storage.

def first_non_repeating(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for num in arr:
        if freq[num] == 1:
            return num
    return None


9. Find Pair with Given Sum
Problem: Find a pair of elements in an array that sum to a given target.
Approach:

Use a hashset to store seen elements.
For each element, check if target - element exists in the set.

Complexity:

Time: O(n) - single pass.
Space: O(n) - hashset storage.

def find_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return (num, target - num)
        seen.add(num)
    return None


10. Find the Longest Consecutive Sequence
Problem: Find the length of the longest consecutive sequence in an unsorted array.
Approach:

Use a hashset to store all elements.
For each element, check if it’s the start of a sequence (no left neighbor).
Count consecutive elements to the right.

Complexity:

Time: O(n) - each element is processed at most twice.
Space: O(n) - hashset storage.

def longest_consecutive_sequence(arr):
    nums = set(arr)
    max_length = 0
    for num in nums:
        if num - 1 not in nums:
            current = num
            current_length = 1
            while current + 1 in nums:
                current += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length


Stacks
11. Valid Parentheses
Problem: Check if a string containing parentheses is valid.
Approach:

Use a stack to track opening brackets.
For each closing bracket, check if it matches the top of the stack.

Complexity:

Time: O(n) - single pass through the string.
Space: O(n) - stack storage.

def is_valid_parentheses(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False
    return len(stack) == 0


12. Next Greater Element
Problem: Find the next greater element for each element in an array.
Approach:

Use a stack to keep track of elements waiting for their next greater element.
Iterate through the array, popping elements from the stack when a larger element is found.

Complexity:

Time: O(n) - each element is pushed and popped at most once.
Space: O(n) - stack storage.

def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result


13. Implement Stack Using Arrays
Problem: Implement a stack using an array.
Approach:

Use an array and a top pointer.
Push: increment top and add element.
Pop: return element at top and decrement top.

Complexity:

Time: O(1) for push and pop.
Space: O(n) - array storage.

class Stack:
    def __init__(self, size):
        self.arr = [0] * size
        self.top = -1
        self.size = size
    
    def push(self, val):
        if self.top >= self.size - 1:
            raise Exception("Stack Overflow")
        self.top += 1
        self.arr[self.top] = val
    
    def pop(self):
        if self.top < 0:
            raise Exception("Stack Underflow")
        val = self.arr[self.top]
        self.top -= 1
        return val


14. Min Stack
Problem: Design a stack that supports getMin() in O(1) time.
Approach:

Use two stacks: one for values, one for tracking minimums.
When pushing, update the min stack if the new value is less than or equal to the current minimum.

Complexity:

Time: O(1) for push, pop, and getMin.
Space: O(n) - two stacks.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if not self.stack:
            raise Exception("Stack Underflow")
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val
    
    def getMin(self):
        if not self.min_stack:
            raise Exception("Stack Empty")
        return self.min_stack[-1]


15. Evaluate Postfix Expression
Problem: Evaluate a postfix expression (e.g., "2 3 +").
Approach:

Use a stack to store operands.
For each operator, pop two operands, compute the result, and push it back.

Complexity:

Time: O(n) - single pass through the expression.
Space: O(n) - stack storage.

def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
        else:
            stack.append(int(token))
    return stack[0]


Queues
16. Implement Queue Using Arrays
Problem: Implement a queue using an array.
Approach:

Use an array with front and rear pointers.
Enqueue: add at rear and increment rear.
Dequeue: remove from front and increment front.

Complexity:

Time: O(1) for enqueue and dequeue (amortized for dynamic arrays).
Space: O(n) - array storage.

class Queue:
    def __init__(self, size):
        self.arr = [0] * size
        self.front = self.rear = -1
        self.size = size
    
    def enqueue(self, val):
        if self.rear >= self.size - 1:
            raise Exception("Queue Overflow")
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.arr[self.rear] = val
    
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            raise Exception("Queue Underflow")
        val = self.arr[self.front]
        self.front += 1
        return val


17. Implement Queue Using Two Stacks
Problem: Implement a queue using two stacks.
Approach:

Use one stack for enqueue (stack1) and another for dequeue (stack2).
Enqueue: push to stack1.
Dequeue: if stack2 is empty, pop all from stack1 to stack2, then pop from stack2.

Complexity:

Time: O(1) for enqueue, O(n) for dequeue (amortized O(1)).
Space: O(n) - two stacks.

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, val):
        self.stack1.append(val)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise Exception("Queue Underflow")
        return self.stack2.pop()


18. Implement Circular Queue
Problem: Implement a circular queue using an array.
Approach:

Use an array with front and rear pointers.
Wrap around indices using modulo to reuse space.
Track size to handle full/empty conditions.

Complexity:

Time: O(1) for enqueue and dequeue.
Space: O(n) - array storage.

class CircularQueue:
    def __init__(self, size):
        self.arr = [0] * size
        self.front = self.rear = -1
        self.size = size
        self.count = 0
    
    def enqueue(self, val):
        if self.count == self.size:
            raise Exception("Queue Overflow")
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = val
        self.count += 1
    
    def dequeue(self):
        if self.count == 0:
            raise Exception("Queue Underflow")
        val = self.arr[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        if self.count == 0:
            self.front = self.rear = -1
        return val


19. Sliding Window Maximum
Problem: Find the maximum element in each sliding window of size k in an array.
Approach:

Use a deque to store indices of potential maximums.
Maintain a deque of decreasing order elements.
For each window, remove out-of-window indices and smaller elements, then add the current index.

Complexity:

Time: O(n) - each element is pushed and popped at most once.
Space: O(k) - deque size.

from collections import deque

def max_sliding_window(arr, k):
    result = []
    dq = deque()
    for i in range(len(arr)):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result


20. Implement Priority Queue
Problem: Implement a priority queue using a heap.
Approach:

Use Python’s heapq module for a min-heap.
Push: add element to heap.
Pop: remove and return the smallest element.

Complexity:

Time: O(log n) for push and pop, O(1) for peek.
Space: O(n) - heap storage.

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        heapq.heappush(self.heap, val)
    
    def pop(self):
        if not self.heap:
            raise Exception("Queue Empty")
        return heapq.heappop(self.heap)
    
    def peek(self):
        if not self.heap:
            raise Exception("Queue Empty")
        return self.heap[0]


Hashmaps
21. Two Sum
Problem: Find indices of two numbers in an array that add up to a target.
Approach:

Use a hashmap to store value-to-index mappings.
For each element, check if target - element exists in the hashmap.

Complexity:

Time: O(n) - single pass.
Space: O(n) - hashmap storage.

def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []


22. Group Anagrams
Problem: Group all anagrams together from a list of strings.
Approach:

Use a hashmap where the key is the sorted string and the value is a list of anagrams.
Sort each string and use it as a key to group anagrams.

Complexity:

Time: O(n * k * log k) - where n is the number of strings, k is the max string length.
Space: O(n * k) - hashmap storage.

def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagrams.setdefault(sorted_s, []).append(s)
    return list(anagrams.values())


23. LRU Cache
Problem: Implement an LRU (Least Recently Used) cache with get and put operations.
Approach:

Use a hashmap for O(1) key-value lookups and a doubly linked list for O(1) updates.
Move recently used items to the front and remove from the tail when capacity is exceeded.

Complexity:

Time: O(1) for get and put.
Space: O(capacity) - hashmap and linked list.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


24. Find All Anagrams in a String
Problem: Find all starting indices of anagrams of a pattern in a string.
Approach:

Use a sliding window with two hashmaps (or arrays) to compare character frequencies.
Slide the window and check if frequencies match.

Complexity:

Time: O(n) - single pass through the string.
Space: O(1) - fixed-size frequency arrays (assuming ASCII).

from collections import Counter

def find_anagrams(s, p):
    if len(p) > len(s):
        return []
    p_count = Counter(p)
    s_count = Counter(s[:len(p)])
    result = [0] if s_count == p_count else []
    for i in range(len(p), len(s)):
        s_count[s[i - len(p)]] -= 1
        if s_count[s[i - len(p)]] == 0:
            del s_count[s[i - len(p)]]
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        if s_count == p_count:
            result.append(i - len(p) + 1)
    return result


25. Subarray Sum Equals K
Problem: Find the number of subarrays with a sum equal to k.
Approach:

Use a hashmap to store the cumulative sum and its frequency.
For each index, check if sum - k exists in the hashmap to count valid subarrays.

Complexity:

Time: O(n) - single pass.
Space: O(n) - hashmap storage.

def subarray_sum(arr, k):
    count = 0
    curr_sum = 0
    sum_freq = {0: 1}
    for num in arr:
        curr_sum += num
        count += sum_freq.get(curr_sum - k, 0)
        sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1
    return count


Sets
26. Intersection of Two Arrays
Problem: Find the intersection of two arrays (return unique elements).
Approach:

Convert the first array to a set.
Check each element of the second array against the set and add to the result set.

Complexity:

Time: O(n + m) - where n and m are array lengths.
Space: O(n) - set storage.

def intersection(arr1, arr2):
    set1 = set(arr1)
    result = set()
    for num in arr2:
        if num in set1:
            result.add(num)
    return list(result)


27. Contains Duplicate
Problem: Check if an array contains any duplicates.
Approach:

Convert the array to a set and compare its length with the array’s length.
If lengths differ, duplicates exist.

Complexity:

Time: O(n) - set conversion.
Space: O(n) - set storage.

def contains_duplicate(arr):
    return len(arr) != len(set(arr))


28. Single Number
Problem: Find the element that appears exactly once in an array where every other element appears twice.
Approach:

Use XOR: XOR of all elements gives the single number (since a XOR a = 0 and a XOR 0 = a).

Complexity:

Time: O(n) - single pass.
Space: O(1) - constant space.

def single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result


29. Happy Number
Problem: Determine if a number is happy (sum of squares of digits eventually reaches 1).
Approach:

Use a set to track seen sums.
Repeatedly compute the sum of squares of digits until 1 is reached or a cycle is detected.

Complexity:

Time: O(log n) - number of digits reduces logarithmically.
Space: O(log n) - set storage.

def is_happy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return True


30. Longest Substring Without Repeating Characters
Problem: Find the length of the longest substring without repeating characters.
Approach:

Use a sliding window with a set to track characters.
Expand the window until a repeat is found, then shrink from the left.

Complexity:

Time: O(n) - each character is added and removed at most once.
Space: O(min(m, n)) - set size, where m is the charset size.

def length_of_longest_substring(s):
    seen = set()
    max_length = 0
    left = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length


Lists
31. Merge Intervals
Problem: Merge overlapping intervals in a list of intervals.
Approach:

Sort intervals by start time.
Iterate and merge overlapping intervals by updating the end time.

Complexity:

Time: O(n log n) - due to sorting.
Space: O(1) - excluding output space.

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for curr in intervals[1:]:
        if curr[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], curr[1])
        else:
            result.append(curr)
    return result


32. Remove Duplicates from Sorted List
Problem: Remove duplicates from a sorted list in-place.
Approach:

Use two pointers: one for the current unique element position, one for scanning.
Move unique elements to the front.

Complexity:

Time: O(n) - single pass.
Space: O(1) - in-place.

def remove_duplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


33. Reverse a List
Problem: Reverse a list in-place.
Approach:

Use two pointers (left and right) and swap elements until they meet.

Complexity:

Time: O(n) - single pass.
Space: O(1) - in-place.

def reverse_list(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


34. Find Kth Largest Element
Problem: Find the kth largest element in an unsorted list.
Approach:

Use a min-heap of size k.
Push elements to the heap; if size exceeds k, pop the smallest.

Complexity:

Time: O(n log k) - heap operations.
Space: O(k) - heap storage.

import heapq

def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


35. Partition List Around a Value
Problem: Partition a list around a value x such that all elements less than x come before those greater than or equal to x.
Approach:

Create two lists: one for elements < x, one for elements >= x.
Concatenate the lists.

Complexity:

Time: O(n) - single pass.
Space: O(n) - additional lists.

def partition_list(arr, x):
    less, greater = [], []
    for num in arr:
        if num < x:
            less.append(num)
        else:
            greater.append(num)
    return less + greater


Linked Lists
36. Reverse a Linked List
Problem: Reverse a singly linked list.
Approach:

Use three pointers: prev, curr, and next.
Reverse the links iteratively.

Complexity:

Time: O(n) - single pass.
Space: O(1) - in-place.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


37. Merge Two Sorted Linked Lists
Problem: Merge two sorted linked lists into one sorted linked list.
Approach:

Use a dummy node to simplify merging.
Compare nodes and link the smaller one to the result.

Complexity:

Time: O(n + m) - where n and m are list lengths.
Space: O(1) - excluding output space.

def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next


38. Detect Cycle in a Linked List
Problem: Determine if a linked list has a cycle.
Approach:

Use Floyd’s cycle detection algorithm (tortoise and hare).
If fast and slow pointers meet, a cycle exists.

Complexity:

Time: O(n) - linear traversal.
Space: O(1) - constant space.

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


39. Find the Middle of a Linked List
Problem: Find the middle node of a linked list.
Approach:

Use two pointers: slow moves one step, fast moves two steps.
When fast reaches the end, slow is at the middle.

Complexity:

Time: O(n) - single pass.
Space: O(1) - constant space.

def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


40. Remove Nth Node from End
Problem: Remove the nth node from the end of a linked list.
Approach:

Use two pointers with a gap of n nodes.
When the fast pointer reaches the end, the slow pointer is at the node before the target.

Complexity:

Time: O(n) - single pass.
Space: O(1) - constant space.

def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next


41. Add Two Numbers
Problem: Add two numbers represented as linked lists (digits in reverse order).
Approach:

Traverse both lists, adding digits and carrying over any overflow.
Create a new linked list with the result.

Complexity:

Time: O(max(n, m)) - where n and m are list lengths.
Space: O(max(n, m)) - result list.

def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        total = x + y + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next


42. Intersection of Two Linked Lists
Problem: Find the intersection point of two linked lists.
Approach:

Traverse both lists to find their lengths.
Move the longer list’s pointer by the difference in lengths.
Traverse both lists together until the pointers meet.

Complexity:

Time: O(n + m) - where n and m are list lengths.
Space: O(1) - constant space.

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a


43. Palindrome Linked List
Problem: Check if a linked list is a palindrome.
Approach:

Find the middle using slow and fast pointers.
Reverse the second half.
Compare the first and second halves.

Complexity:

Time: O(n) - three passes (find middle, reverse, compare).
Space: O(1) - in-place.

def is_palindrome(head):
    if not head or not head.next:
        return True
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second_half = reverse_linked_list(slow.next)
    while second_half:
        if head.val != second_half.val:
            return False
        head = head.next
        second_half = second_half.next
    return True


44. Swap Nodes in Pairs
Problem: Swap every two adjacent nodes in a linked list.
Approach:

Use a recursive or iterative approach to swap pairs.
Iteratively: adjust pointers to swap nodes and link to the next pair.

Complexity:

Time: O(n) - single pass.
Space: O(1) - in-place.

def swap_pairs(head):
    if not head or not head.next:
        return head
    dummy = ListNode(0, head)
    prev = dummy
    while head and head.next:
        next_node = head.next
        prev.next = next_node
        head.next = next_node.next
        next_node.next = head
        prev = head
        head = head.next
    return dummy.next


45. Rotate List
Problem: Rotate a linked list to the right by k places.
Approach:

Find the length and connect the tail to the head to form a cycle.
Move to the new tail (length - k % length) and break the cycle.

Complexity:

Time: O(n) - two passes.
Space: O(1) - constant space.

def rotate_right(head, k):
    if not head or not head.next:
        return head
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    k = k % length
    if k == 0:
        return head
    tail.next = head
    for _ in range(length - k):
        tail = tail.next
    new_head = tail.next
    tail.next = None
    return new_head


Mixed Questions
46. Implement Stack Using Queues
Problem: Implement a stack using two queues.
Approach:

Use two queues, making push operation costly.
Push: enqueue to q2, move all elements from q1 to q2, swap q1 and q2.
Pop: dequeue from q1.

Complexity:

Time: O(n) for push, O(1) for pop.
Space: O(n) - two queues.

from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, val):
        self.q2.append(val)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        if not self.q1:
            raise Exception("Stack Underflow")
        return self.q1.popleft()


47. Design a HashMap
Problem: Implement a hashmap with put, get, and remove operations.
Approach:

Use an array of linked lists (chaining) to handle collisions.
Hash function: key % size.
Traverse the linked list at the hashed index for operations.

Complexity:

Time: O(1) average, O(n) worst case for collisions.
Space: O(n) - array and linked lists.

class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class HashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size
    
    def _hash(self, key):
        return key % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key, value)
        else:
            curr = self.buckets[index]
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                if not curr.next:
                    break
                curr = curr.next
            curr.next = ListNode(key, value)
    
    def get(self, key):
        index = self._hash(key)
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1
    
    def remove(self, key):
        index = self._hash(key)
        curr = self.buckets[index]
        if not curr:
            return
        if curr.key == key:
            self.buckets[index] = curr.next
            return
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


48. Find First Unique Character in a String
Problem: Find the index of the first non-repeating character in a string.
Approach:

Use a hashmap to count character frequencies.
Iterate through the string to find the first character with a count of 1.

Complexity:

Time: O(n) - two passes.
Space: O(1) - fixed-size hashmap (assuming ASCII).

def first_unique_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1


49. Top K Frequent Elements
Problem: Find the k most frequent elements in an array.
Approach:

Use a hashmap to count frequencies.
Use a min-heap of size k to keep track of the top k elements.

Complexity:

Time: O(n log k) - heap operations.
Space: O(n) - hashmap and heap.

import heapq
from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]


50. Implement a Deque
Problem: Implement a double-ended queue (deque) supporting operations from both ends.
Approach:

Use Python’s collections.deque for efficient append and pop from both ends.
Alternatively, implement using a doubly linked list for O(1) operations.

Complexity:

Time: O(1) for append and pop operations.
Space: O(n) - storage for elements.

from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()
    
    def append(self, val):
        self.deque.append(val)
    
    def appendleft(self, val):
        self.deque.appendleft(val)
    
    def pop(self):
        if not self.deque:
            raise Exception("Deque Empty")
        return self.deque.pop()
    
    def popleft(self):
        if not self.deque:
            raise Exception("Deque Empty")
        return self.deque.popleft()


Conclusion
These 50 questions cover a wide range of problems on arrays, stacks, queues, hashmaps, sets, lists, and linked lists, with clear explanations, complexity analyses, and Python code solutions. Practice these to build a strong foundation for your DSA interviews. For further exploration, consider resources like GeeksforGeeks, LeetCode, or InterviewBit, which offer additional problems and solutions.
