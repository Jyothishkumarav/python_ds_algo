50 Data Structures and Algorithms Interview Questions with Solutions
This document provides 50 Data Structures and Algorithms (DSA) questions, updated with detailed approaches, sample inputs/outputs, and solutions in Python. The questions focus on arrays, stacks, queues, hashmaps, sets, lists, and linked lists, ideal for technical interview preparation.

Arrays
1. Find the Second Largest Element in an Array
Problem: Given an array of integers, find the second largest element.
Detailed Approach:

Initialize two variables, largest and second_largest, to negative infinity.
Iterate through the array:
If the current element is greater than largest, update second_largest to largest and largest to the current element.
If the current element is between largest and second_largest and not equal to largest, update second_largest.


Handle edge cases: return None if the array has fewer than 2 elements or no valid second largest exists.
This approach ensures a single pass with constant space, avoiding sorting or multiple passes.

Complexity:

Time: O(n) - single pass through the array.
Space: O(1) - uses only two variables.

Python Code:
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

Sample Input/Output:

Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: 35 is the largest, 34 is the second largest.


Input: arr = [10, 10, 10]
Output: None
Explanation: No distinct second largest exists.


Input: arr = [5]
Output: None
Explanation: Array has fewer than 2 elements.




2. Rotate an Array by k Positions
Problem: Rotate an array to the right by k steps.
Detailed Approach:

Normalize k by taking k = k % n to handle cases where k > n.
Use the reversal algorithm to rotate in-place:
Reverse the entire array to get the elements in reverse order.
Reverse the first k elements to place them in their final positions.
Reverse the remaining n-k elements to correct their order.


This method is space-efficient as it modifies the array in-place and avoids temporary arrays.
Handle edge cases: empty array or k = 0 (no rotation needed).

Complexity:

Time: O(n) - three reversals, each O(n).
Space: O(1) - in-place operations.

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

Sample Input/Output:

Input: arr = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
Explanation: Rotate [1, 2, 3, 4, 5] right by 2 steps.


Input: arr = [1, 2, 3], k = 3
Output: [1, 2, 3]
Explanation: k = 3 % 3 = 0, no rotation.


Input: arr = [], k = 5
Output: []
Explanation: Empty array remains unchanged.




3. Find the Missing Number in an Array
Problem: Given an array of n-1 integers in the range [1, n], find the missing number.
Detailed Approach:

Compute the expected sum of numbers from 1 to n using the formula n * (n + 1) / 2.
Compute the actual sum of the array elements.
The missing number is the difference between the expected and actual sums.
Alternatively, use XOR to find the missing number, but summation is simpler and sufficient.
This approach is efficient with a single pass and constant space, handling all cases like missing first or last numbers.

Complexity:

Time: O(n) - single pass to compute sum.
Space: O(1) - constant space.

def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

Sample Input/Output:

Input: arr = [1, 2, 4, 6, 3, 7, 8], n = 8
Output: 5
Explanation: Numbers 1 to 8, 5 is missing.


Input: arr = [2, 3, 4], n = 4
Output: 1
Explanation: 1 is missing from [1, 2, 3, 4].


Input: arr = [1], n = 2
Output: 2
Explanation: 2 is missing.




4. Merge Two Sorted Arrays
Problem: Merge two sorted arrays into a single sorted array.
Detailed Approach:

Initialize two pointers, i and j, at the start of arr1 and arr2.
Create an empty result array.
Compare elements at i and j, appending the smaller one to the result and advancing the corresponding pointer.
After one array is exhausted, append the remaining elements from the other array.
This ensures the result is sorted without modifying the input arrays.
Handle edge cases: empty arrays or arrays of different lengths.

Complexity:

Time: O(n + m) - where n and m are array lengths.
Space: O(n + m) - result array.

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

Sample Input/Output:

Input: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
Explanation: Merge sorted arrays into a single sorted array.


Input: arr1 = [], arr2 = [1, 2]
Output: [1, 2]
Explanation: arr1 is empty, return arr2.


Input: arr1 = [1], arr2 = []
Output: [1]
Explanation: arr2 is empty, return arr1.




5. Find the Maximum Subarray Sum (Kadane’s Algorithm)
Problem: Find the maximum sum of a contiguous subarray.
Detailed Approach:

Use Kadane’s algorithm to track the maximum sum subarray ending at each position.
Maintain current_sum (sum of subarray ending at current index) and max_sum (global maximum).
For each element:
Update current_sum as max(current element, current_sum + current element).
Update max_sum if current_sum is greater.


Initialize both sums with the first element to handle negative arrays.
This approach handles all cases, including all-negative arrays, in a single pass.

Complexity:

Time: O(n) - single pass.
Space: O(1) - constant space.

def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

Sample Input/Output:

Input: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: Subarray [4, -1, 2, 1] has the maximum sum of 6.


Input: arr = [1]
Output: 1
Explanation: Single element is the maximum subarray.


Input: arr = [-1, -2, -3]
Output: -1
Explanation: Maximum sum is the least negative number.




6. Find Duplicates in an Array
Problem: Given an array of integers in the range [1, n], find all duplicates.
Detailed Approach:

Use the array itself as a hash table by marking indices.
For each number, make the element at index (abs(num) - 1) negative to mark its presence.
If an index is already negative, the number is a duplicate.
Use absolute values to handle negative numbers created during marking.
Restore the array if needed (not done here for simplicity).
This approach is space-efficient as it modifies the array in-place.

Complexity:

Time: O(n) - single pass.
Space: O(1) - in-place (excluding output).

def find_duplicates(arr):
    result = []
    for num in arr:
        index = abs(num) - 1
        if arr[index] > 0:
            arr[index] = -arr[index]
        else:
            result.append(abs(num))
    return result

Sample Input/Output:

Input: arr = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]
Explanation: 2 and 3 appear twice.


Input: arr = [1, 1, 2]
Output: [1]
Explanation: 1 is the only duplicate.


Input: arr = [1, 2, 3]
Output: []
Explanation: No duplicates.




7. Move Zeros to End
Problem: Move all zeros to the end of the array while maintaining the relative order of non-zero elements.
Detailed Approach:

Use a pointer non_zero_pos to track the position where the next non-zero element should go.
Iterate through the array, swapping non-zero elements to non_zero_pos and incrementing it.
After placing all non-zero elements, fill the remaining positions with zeros.
This ensures in-place modification and preserves the order of non-zero elements.
Handle edge cases: all zeros or no zeros.

Complexity:

Time: O(n) - single pass.
Space: O(1) - in-place.

def move_zeros(arr):
    non_zero_pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_pos], arr[i] = arr[i], arr[non_zero_pos]
            non_zero_pos += 1

Sample Input/Output:

Input: arr = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Explanation: Non-zero elements maintain order, zeros moved to end.


Input: arr = [0, 0, 0]
Output: [0, 0, 0]
Explanation: All zeros, no change needed.


Input: arr = [1, 2, 3]
Output: [1, 2, 3]
Explanation: No zeros, no change.




8. Find the First Non-Repeating Element
Problem: Find the first element in an array that appears only once.
Detailed Approach:

Create a hashmap to store the frequency of each element.
Iterate through the array to populate the hashmap with counts.
Iterate through the array again to find the first element with a frequency of 1.
Return None if no such element exists.
This approach preserves the order of elements by checking in the original array order.

Complexity:

Time: O(n) - two passes.
Space: O(n) - hashmap storage.

def first_non_repeating(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for num in arr:
        if freq[num] == 1:
            return num
    return None

Sample Input/Output:

Input: arr = [9, 4, 9, 6, 7, 4]
Output: 6
Explanation: 6 is the first element that appears once.


Input: arr = [1, 1, 2, 2]
Output: None
Explanation: No element appears once.


Input: arr = [1]
Output: 1
Explanation: Single element appears once.




9. Find Pair with Given Sum
Problem: Find a pair of elements in an array that sum to a given target.
Detailed Approach:

Use a hashset to store elements as you iterate through the array.
For each element, compute target - element and check if it exists in the hashset.
If found, return the pair; otherwise, add the current element to the hashset.
Return None if no pair is found.
This approach ensures O(n) time by avoiding nested loops.

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

Sample Input/Output:

Input: arr = [2, 7, 11, 15], target = 9
Output: (7, 2)
Explanation: 7 + 2 = 9.


Input: arr = [1, 2, 3], target = 10
Output: None
Explanation: No pair sums to 10.


Input: arr = [5, 5], target = 10
Output: (5, 5)
Explanation: 5 + 5 = 10.




10. Find the Longest Consecutive Sequence
Problem: Find the length of the longest consecutive sequence in an unsorted array.
Detailed Approach:

Convert the array to a hashset for O(1) lookups.
For each element, check if it’s the start of a sequence (no element num-1 exists).
If it is, count consecutive elements (num+1, num+2, ...) in the set.
Track the maximum sequence length found.
This approach avoids checking non-starting elements, ensuring each element is processed at most twice.

Complexity:

Time: O(n) - each element is checked at most twice.
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

Sample Input/Output:

Input: arr = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: Longest sequence is [1, 2, 3, 4].


Input: arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
Explanation: Sequence [0, 1, 2, 3, 4, 5, 6, 7, 8].


Input: arr = []
Output: 0
Explanation: Empty array has no sequence.




Stacks
11. Valid Parentheses
Problem: Check if a string containing parentheses is valid.
Detailed Approach:

Use a stack to track opening brackets.
For each character:
If it’s an opening bracket, push it onto the stack.
If it’s a closing bracket, check if the stack’s top matches; if not, return False.


After iteration, check if the stack is empty (all brackets matched).
Use a dictionary to map closing brackets to their corresponding opening brackets.
Handle edge cases: empty string, unmatched brackets.

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

Sample Input/Output:

Input: s = "()[]{}"
Output: True
Explanation: All brackets are properly matched.


Input: s = "(]"
Output: False
Explanation: Parentheses do not match.


Input: s = ""
Output: True
Explanation: Empty string is valid.




12. Next Greater Element
Problem: Find the next greater element for each element in an array.
Detailed Approach:

Use a monotonic stack to store indices of elements in increasing order.
Iterate through the array:
While the stack is not empty and the current element is greater than the element at the stack’s top index, pop the stack and assign the current element as the next greater element for the popped index.
Push the current index onto the stack.


After iteration, any remaining indices in the stack have no greater element (assign -1).
This ensures each element is pushed and popped at most once.

Complexity:

Time: O(n) - each element is pushed/popped once.
Space: O(n) - stack storage.

def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

Sample Input/Output:

Input: arr = [4, 5, 2, 25]
Output: [5, 25, 25, -1]
Explanation: Next greater for 4 is 5, for 5 is 25, for 2 is 25, for 25 is none.


Input: arr = [13, 7, 6, 12]
Output: [-1, 12, 12, -1]
Explanation: No greater for 13 and 12, 7 and 6 have 12.


Input: arr = [1]
Output: [-1]
Explanation: Single element has no greater element.




13. Implement Stack Using Arrays
Problem: Implement a stack using an array.
Detailed Approach:

Initialize an array of fixed size and a top pointer set to -1.
Push operation:
Increment top and add the element at arr[top].
Check for overflow (top >= size).


Pop operation:
Return arr[top] and decrement top.
Check for underflow (top < 0).


Handle edge cases: empty stack, full stack.
This implementation is simple but limited by fixed size.

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

Sample Input/Output:

Input: Operations = push(1), push(2), pop(), push(3), pop()
Output: 2, 3
Explanation: Pop returns 2 after pushing 1, 2; then 3 after pushing 3.


Input: Operations = push(1), pop()
Output: 1
Explanation: Push 1, pop returns 1.


Input: Operations = pop()
Output: Exception: Stack Underflow
Explanation: Cannot pop from empty stack.




14. Min Stack
Problem: Design a stack that supports getMin() in O(1) time.
Detailed Approach:

Use two stacks: one for values (stack), one for minimums (min_stack).
Push operation:
Push value to stack.
If value is less than or equal to min_stack’s top (or min_stack is empty), push value to min_stack.


Pop operation:
Pop from stack.
If the popped value equals min_stack’s top, pop from min_stack.


getMin: Return min_stack’s top.
Handle edge cases: empty stack for pop/getMin.
This ensures O(1) for all operations by maintaining minimums dynamically.

Complexity:

Time: O(1) for push, pop, getMin.
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

Sample Input/Output:

Input: Operations = push(3), push(5), getMin(), push(2), getMin(), pop(), getMin()
Output: 3, 2, 3
Explanation: Min is 3 after pushing 3, 5; 2 after pushing 2; 3 after popping 2.


Input: Operations = push(1), pop(), getMin()
Output: Exception: Stack Empty
Explanation: getMin fails on empty stack.


Input: Operations = push(1), push(1), getMin()
Output: 1
Explanation: Min is 1 with duplicates.




15. Evaluate Postfix Expression
Problem: Evaluate a postfix expression (e.g., "2 3 +").
Detailed Approach:

Use a stack to store operands.
Split the expression into tokens.
For each token:
If it’s a number, push it to the stack.
If it’s an operator, pop two operands (in correct order: b, a), compute a op b, and push the result.


The final result is the only element left in the stack.
Handle edge cases: invalid expressions, division by zero (not handled here for brevity).
Assume valid input with integers and basic operators (+, -, *, /).

Complexity:

Time: O(n) - single pass through tokens.
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

Sample Input/Output:

Input: expression = "2 3 +"
Output: 5
Explanation: 2 + 3 = 5.


Input: expression = "4 13 5 / +"
Output: 6
Explanation: 4 + (13 / 5) = 4 + 2 = 6 (integer division).


Input: expression = "5 1 2 + 4 * + 3 -"
Output: 14
Explanation: 5 + ((1 + 2) * 4) - 3 = 5 + 12 - 3 = 14.




Queues
16. Implement Queue Using Arrays
Problem: Implement a queue using an array.
Detailed Approach:

Initialize an array of fixed size, with front and rear pointers set to -1.
Enqueue:
If empty, set front to 0.
Increment rear and add element at arr[rear].
Check for overflow (rear >= size).


Dequeue:
Return arr[front] and increment front.
Check for underflow (front > rear or front = -1).


Handle edge cases: empty queue, full queue.
This is a basic implementation with linear space usage.

Complexity:

Time: O(1) for enqueue and dequeue.
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

Sample Input/Output:

Input: Operations = enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue()
Output: 1, 2
Explanation: Dequeue returns 1, then 2 after enqueuing 1, 2, 3.


Input: Operations = enqueue(1), dequeue()
Output: 1
Explanation: Enqueue 1, dequeue returns 1.


Input: Operations = dequeue()
Output: Exception: Queue Underflow
Explanation: Cannot dequeue from empty queue.




17. Implement Queue Using Two Stacks
Problem: Implement a queue using two stacks.
Detailed Approach:

Use two stacks: stack1 for enqueue, stack2 for dequeue.
Enqueue:
Push element to stack1.


Dequeue:
If stack2 is empty, pop all elements from stack1 to stack2 (reversing order).
Pop and return top of stack2.
If both stacks are empty, raise underflow exception.


This makes enqueue O(1) and dequeue O(n) in worst case, but amortized O(1) for a sequence of operations.
Handle edge cases: empty queue, multiple dequeues.

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

Sample Input/Output:

Input: Operations = enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue()
Output: 1, 2
Explanation: FIFO order: 1 dequeued first, then 2.


Input: Operations = enqueue(1), dequeue()
Output: 1
Explanation: Enqueue 1, dequeue returns 1.


Input: Operations = dequeue()
Output: Exception: Queue Underflow
Explanation: Empty queue.




18. Implement Circular Queue
Problem: Implement a circular queue using an array.
Detailed Approach:

Initialize an array of fixed size, with front, rear, and count (number of elements).
Enqueue:
If full (count == size), raise overflow.
If empty, set front to 0.
Increment rear using (rear + 1) % size, add element, increment count.


Dequeue:
If empty (count == 0), raise underflow.
Return element at front, increment front using (front + 1) % size, decrement count.
Reset front and rear to -1 if queue becomes empty.


Circular nature allows reusing space, avoiding the linear queue’s space waste.
Handle edge cases: full/empty queue, wrap-around indices.

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

Sample Input/Output:

Input: Operations = enqueue(1), enqueue(2), dequeue(), enqueue(3), enqueue(4)
Output: 1
Explanation: Dequeue returns 1, queue becomes [2, 3, 4].


Input: Operations = enqueue(1), dequeue(), enqueue(2)
Output: 1
Explanation: Dequeue 1, enqueue 2 reuses space.


Input: Operations = enqueue(1), enqueue(2), enqueue(3) (size=2)
Output: Exception: Queue Overflow
Explanation: Queue of size 2 cannot hold 3 elements.




19. Sliding Window Maximum
Problem: Find the maximum element in each sliding window of size k in an array.
Detailed Approach:

Use a deque to store indices of potential maximums in decreasing order.
For each index i:
Remove indices outside the current window (i - k).
Remove indices of smaller elements from the back (maintain decreasing order).
Add current index to the back.


After processing k-1 elements, the front of the deque is the maximum for each window.
This ensures O(n) time as each index is pushed and popped at most once.
Handle edge cases: k > n, empty array.

Complexity:

Time: O(n) - each element is pushed/popped once.
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

Sample Input/Output:

Input: arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
Explanation: Max in windows [1,3,-1], [3,-1,-3], ..., [3,6,7].


Input: arr = [1], k = 1
Output: [1]
Explanation: Single element window.


Input: arr = [9, 8, 7], k = 2
Output: [9, 8]
Explanation: Max in [9,8], [8,7].




20. Implement Priority Queue
Problem: Implement a priority queue using a heap.
Detailed Approach:

Use Python’s heapq module for a min-heap implementation.
Push: Add element to heap using heappush, maintaining heap property.
Pop: Remove and return smallest element using heappop.
Peek: Return the smallest element (heap[0]) without removing it.
Handle edge cases: empty queue for pop/peek.
For max-heap, negate values or use a custom comparator (min-heap used here for simplicity).
This provides efficient priority-based operations.

Complexity:

Time: O(log n) for push/pop, O(1) for peek.
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

Sample Input/Output:

Input: Operations = push(3), push(1), push(2), pop(), peek()
Output: 1, 2
Explanation: Pop returns smallest (1), peek returns next smallest (2).


Input: Operations = push(5), pop()
Output: 5
Explanation: Single element popped.


Input: Operations = pop()
Output: Exception: Queue Empty
Explanation: Cannot pop empty queue.




Hashmaps
21. Two Sum
Problem: Find indices of two numbers in an array that add up to a target.
Detailed Approach:

Use a hashmap to store value-to-index mappings.
For each element at index i:
Compute target - arr[i].
If it exists in the hashmap, return [hashmap[target - arr[i]], i].
Otherwise, add arr[i]: i to the hashmap.


Return empty list if no solution is found.
This ensures O(n) time by avoiding nested loops and handles unique solutions (as per problem constraints).

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

Sample Input/Output:

Input: arr = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: arr[0] + arr[1] = 2 + 7 = 9.


Input: arr = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: arr[1] + arr[2] = 2 + 4 = 6.


Input: arr = [3, 3], target = 6
Output: [0, 1]
Explanation: arr[0] + arr[1] = 3 + 3 = 6.




22. Group Anagrams
Problem: Group all anagrams together from a list of strings.
Detailed Approach:

Use a hashmap where the key is the sorted string (or character count) and the value is a list of anagrams.
For each string:
Sort its characters to create a key.
Add the original string to the list associated with that key.


Return the hashmap’s values as a list of grouped anagrams.
Sorting ensures that anagrams map to the same key.
Handle edge cases: empty list, single-character strings.

Complexity:

Time: O(n * k * log k) - n strings, k max string length, sorting k chars.
Space: O(n * k) - hashmap storage.

def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagrams.setdefault(sorted_s, []).append(s)
    return list(anagrams.values())

Sample Input/Output:

Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
Explanation: Grouped by anagrams.


Input: strs = [""]
Output: [[""]]
Explanation: Empty string is its own anagram.


Input: strs = ["a"]
Output: [["a"]]
Explanation: Single character is an anagram.




23. LRU Cache
Problem: Implement an LRU (Least Recently Used) cache with get and put operations.
Detailed Approach:

Use a hashmap for O(1) key-to-node mappings and a doubly linked list for O(1) order updates.
Doubly linked list nodes store key-value pairs, with head (most recent) and tail (least recent).
Get operation:
If key exists, move its node to head and return value.
Else, return -1.


Put operation:
If key exists, update value and move node to head.
Else, add new node to head; if capacity exceeded, remove tail node and its hashmap entry.


Use dummy head and tail nodes to simplify list operations.
Handle edge cases: capacity = 1, empty cache.

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

Sample Input/Output:

Input: Operations = LRUCache(2), put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1)
Output: 1, -1, -1
Explanation: Get 1 returns 1; after put(3,3), 2 is evicted; after put(4,4), 1 is evicted.


Input: Operations = LRUCache(1), put(1,1), put(2,2), get(1)
Output: -1
Explanation: Capacity 1, 1 evicted by 2.


Input: Operations = LRUCache(2), get(1)
Output: -1
Explanation: Key 1 not in cache.




24. Find All Anagrams in a String
Problem: Find all starting indices of anagrams of a pattern in a string.
Detailed Approach:

Use a sliding window of size equal to pattern length.
Create frequency maps (or arrays) for the pattern and the current window.
Initialize the window’s frequency map for the first len(p) characters.
Slide the window:
Remove the leftmost character’s frequency.
Add the new character’s frequency.
If frequencies match, record the window’s start index.


Use Counter for simplicity, handling character additions/removals efficiently.
Handle edge cases: pattern longer than string, empty inputs.

Complexity:

Time: O(n) - single pass through string.
Space: O(1) - fixed-size frequency maps (ASCII).

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

Sample Input/Output:

Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation: Anagrams "cba" at 0, "abc" at 6.


Input: s = "abab", p = "ab"
Output: [0, 1, 2]
Explanation: Anagrams "ab" at 0, "ba" at 1, "ab" at 2.


Input: s = "aaa", p = "aaaa"
Output: []
Explanation: Pattern too long.




25. Subarray Sum Equals K
Problem: Find the number of subarrays with a sum equal to k.
Detailed Approach:

Use a hashmap to store cumulative sums and their frequencies.
Initialize curr_sum = 0 and sum_freq = {0: 1} (for subarrays starting at index 0).
For each element:
Add to curr_sum.
If curr_sum - k exists in sum_freq, add its frequency to the count (valid subarrays).
Increment curr_sum’s frequency in sum_freq.


This handles negative numbers and zero-sum subarrays efficiently.
Handle edge cases: empty array, k = 0.

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

Sample Input/Output:

Input: arr = [1, 1, 1], k = 2
Output: 2
Explanation: Subarrays [1,1] at indices [0,1] and [1,1] at [1,2].


Input: arr = [1, 2, 3], k = 3
Output: 2
Explanation: Subarrays [1,2] and [3].


Input: arr = [1, -1, 0], k = 0
Output: 3
Explanation: Subarrays [1,-1], [1,-1,0], [0].




Sets
26. Intersection of Two Arrays
Problem: Find the intersection of two arrays (return unique elements).
Detailed Approach:

Convert the first array to a set for O(1) lookups and to remove duplicates.
Iterate through the second array, adding elements to a result set if they exist in the first set.
Convert the result set to a list for output.
This ensures unique elements and efficient lookups.
Handle edge cases: empty arrays, no intersection.

Complexity:

Time: O(n + m) - n and m are array lengths.
Space: O(n) - set storage.

def intersection(arr1, arr2):
    set1 = set(arr1)
    result = set()
    for num in arr2:
        if num in set1:
            result.add(num)
    return list(result)

Sample Input/Output:

Input: arr1 = [1, 2, 2, 1], arr2 = [2, 2]
Output: [2]
Explanation: Unique intersection is 2.


Input: arr1 = [4, 9, 5], arr2 = [9, 4, 9, 8, 4]
Output: [4, 9]
Explanation: Unique elements 4 and 9.


Input: arr1 = [1, 2], arr2 = [3, 4]
Output: []
Explanation: No intersection.




27. Contains Duplicate
Problem: Check if an array contains any duplicates.
Detailed Approach:

Convert the array to a set, which removes duplicates.
Compare the set’s length to the array’s length.
If they differ, duplicates exist (set length is smaller).
Alternatively, use a hashset to check for duplicates in one pass, but set conversion is more concise.
Handle edge cases: empty array, single element.

Complexity:

Time: O(n) - set conversion.
Space: O(n) - set storage.

def contains_duplicate(arr):
    return len(arr) != len(set(arr))

Sample Input/Output:

Input: arr = [1, 2, 3, 1]
Output: True
Explanation: 1 appears twice.


Input: arr = [1, 2, 3, 4]
Output: False
Explanation: No duplicates.


Input: arr = []
Output: False
Explanation: Empty array has no duplicates.




28. Single Number
Problem: Find the element that appears exactly once in an array where every other element appears twice.
Detailed Approach:

Use XOR operation: XOR of all elements cancels out paired numbers (a XOR a = 0), leaving the single number (a XOR 0 = a).
Iterate through the array, XORing each element with the result.
The final result is the single number.
This is optimal as it uses O(1) space and handles all cases efficiently.
Handle edge case: assume valid input (one single number).

Complexity:

Time: O(n) - single pass.
Space: O(1) - constant space.

def single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

Sample Input/Output:

Input: arr = [2, 2, 1]
Output: 1
Explanation: 1 appears once, 2 appears twice.


Input: arr = [4, 1, 2, 1, 2]
Output: 4
Explanation: 4 is the single number.


Input: arr = [1]
Output: 1
Explanation: Only one element.




29. Happy Number
Problem: Determine if a number is happy (sum of squares of digits eventually reaches 1).
Detailed Approach:

Use a set to track seen sums to detect cycles.
For the input number:
Compute the sum of squares of its digits.
If sum is 1, return True (happy number).
If sum is seen before, return False (cycle detected).
Otherwise, add sum to set and repeat.


This handles all cases, including cycles (e.g., 4 loops to 4).
Handle edge case: assume positive integer input.

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

Sample Input/Output:

Input: n = 19
Output: True
Explanation: 1² + 9² = 82, 8² + 2² = 68, 6² + 8² = 100, 1² + 0² + 0² = 1.


Input: n = 2
Output: False
Explanation: Enters cycle: 2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4.


Input: n = 1
Output: True
Explanation: 1 is happy by definition.




30. Longest Substring Without Repeating Characters
Problem: Find the length of the longest substring without repeating characters.
Detailed Approach:

Use a sliding window with a set to track unique characters.
Initialize left pointer and max_length.
For each right pointer:
If current character is in set, remove characters from left until the duplicate is removed.
Add current character to set.
Update max_length with current window size (right - left + 1).


This ensures O(n) time as each character is added and removed at most once.
Handle edge cases: empty string, single character.

Complexity:

Time: O(n) - each character processed once.
Space: O(min(m, n)) - set size, m is charset size.

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

Sample Input/Output:

Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring without repeats.


Input: s = "bbbbb"
Output: 1
Explanation: Single character "b" is longest.


Input: s = ""
Output: 0
Explanation: Empty string has length 0.




Lists
31. Merge Intervals
Problem: Merge overlapping intervals in a list of intervals.
Detailed Approach:

Sort intervals by start time to ensure overlapping intervals are adjacent.
Initialize result with the first interval.
For each subsequent interval:
If it overlaps with the last interval in result (curr.start <= last.end), merge by updating the end to max(last.end, curr.end).
Otherwise, add the interval to result.


Sorting ensures correct merging order; max end handles contained intervals.
Handle edge cases: empty list, single interval.

Complexity:

Time: O(n log n) - sorting dominates.
Space: O(1) - excluding output.

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

Sample Input/Output:

Input: intervals = [[1,3], [2,6], [8,10], [15,18]]
Output: [[1,6], [8,10], [15,18]]
Explanation: Merge [1,3] and [2,6] into [1,6].


Input: intervals = [[1,4], [4,5]]
Output: [[1,5]]
Explanation: Merge touching intervals.


Input: intervals = []
Output: []
Explanation: Empty input.




32. Remove Duplicates from Sorted List
Problem: Remove duplicates from a sorted list in-place.
Detailed Approach:

Since the list is sorted, duplicates are adjacent.
Use two pointers: write for the position of the next unique element, read for scanning.
Initialize write to 1 (first element is unique).
For each read position:
If arr[read] differs from arr[write-1], copy it to arr[write] and increment write.


Return write as the length of the unique elements.
This modifies the list in-place efficiently.
Handle edge cases: empty list, single element.

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

Sample Input/Output:

Input: nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]
Explanation: Remove duplicate 1, length is 2.


Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
Explanation: Unique elements are [0, 1, 2, 3, 4].


Input: nums = []
Output: 0
Explanation: Empty list.




33. Reverse a List
Problem: Reverse a list in-place.
Detailed Approach:

Use two pointers: left starting at 0, right starting at the end.
While left < right:
Swap elements at left and right.
Increment left, decrement right.


This reverses the list in-place without extra space.
Handle edge cases: empty list, single element (no change needed).

Complexity:

Time: O(n) - single pass.
Space: O(1) - in-place.

def reverse_list(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

Sample Input/Output:

Input: arr = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Explanation: List reversed in-place.


Input: arr = [1]
Output: [1]
Explanation: Single element unchanged.


Input: arr = []
Output: []
Explanation: Empty list unchanged.




34. Find Kth Largest Element
Problem: Find the kth largest element in an unsorted list.
Detailed Approach:

Use a min-heap of size k to track the k largest elements.
For each element:
Push to heap.
If heap size exceeds k, pop the smallest element.


After iteration, the heap’s root is the kth largest element.
Alternatively, use quickselect for average O(n) time, but heap is simpler and reliable.
Handle edge cases: k > n, k = 1 (largest), k = n (smallest).

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

Sample Input/Output:

Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
Explanation: 2nd largest is 5 (6 is 1st).


Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
Explanation: 4th largest is 4.


Input: nums = [1], k = 1
Output: 1
Explanation: Only element is 1st largest.




35. Partition List Around a Value
Problem: Partition a list around a value x such that all elements less than x come before those greater than or equal to x.
Detailed Approach:

Create two temporary lists: less for elements < x, greater for elements >= x.
Iterate through the array, appending each element to the appropriate list.
Concatenate less and greater to form the result.
This preserves relative order within partitions but requires extra space.
Alternatively, use in-place partitioning with two pointers for O(1) space (not shown here for simplicity).
Handle edge cases: empty list, all elements < x or >= x.

Complexity:

Time: O(n) - single pass.
Space: O(n) - temporary lists.

def partition_list(arr, x):
    less, greater = [], []
    for num in arr:
        if num < x:
            less.append(num)
        else:
            greater.append(num)
    return less + greater

Sample Input/Output:

Input: arr = [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]
Explanation: Elements < 3 come before >= 3.


Input: arr = [2, 1], x = 2
Output: [1, 2]
Explanation: 1 < 2, 2 >= 2.


Input: arr = [], x = 5
Output: []
Explanation: Empty list.




Linked Lists
36. Reverse a Linked List
Problem: Reverse a singly linked list.
Detailed Approach:

Use three pointers: prev, curr, and next.
Initialize prev as None, curr as head.
While curr is not None:
Save curr.next in next.
Reverse link: set curr.next to prev.
Move prev to curr, curr to next.


Return prev as the new head.
This reverses the list in-place efficiently.
Handle edge cases: empty list, single node.

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

Sample Input/Output:

Input: head = 1->2->3->4->5
Output: 5->4->3->2->1
Explanation: List reversed.


Input: head = 1
Output: 1
Explanation: Single node unchanged.


Input: head = None
Output: None
Explanation: Empty list.




37. Merge Two Sorted Linked Lists
Problem: Merge two sorted linked lists into one sorted linked list.
Detailed Approach:

Use a dummy node to simplify merging and handle edge cases.
Initialize curr to dummy node.
While both lists have nodes:
Compare values, link smaller node to curr.next, advance that list’s pointer.
Move curr to the linked node.


Append remaining nodes from either list (if any).
Return dummy.next as the merged list head.
This merges in-place without extra space for nodes.
Handle edge cases: empty lists, one empty list.

Complexity:

Time: O(n + m) - n, m are list lengths.
Space: O(1) - excluding output.

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

Sample Input/Output:

Input: l1 = 1->2->4, l2 = 1->3->4
Output: 1->1->2->3->4->4
Explanation: Merged in sorted order.


Input: l1 = None, l2 = 1->2
Output: 1->2
Explanation: Return non-empty list.


Input: l1 = None, l2 = None
Output: None
Explanation: Both empty.




38. Detect Cycle in a Linked List
Problem: Determine if a linked list has a cycle.
Detailed Approach:

Use Floyd’s Cycle-Finding Algorithm (tortoise and hare).
Initialize two pointers, slow and fast, at head.
Move slow one step, fast two steps per iteration.
If slow meets fast, a cycle exists.
If fast or fast.next becomes None, no cycle.
This is efficient with O(1) space, detecting cycles without extra storage.
Handle edge cases: empty list, no cycle.

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

Sample Input/Output:

Input: head = 3->2->0->-4, -4->2 (cycle)
Output: True
Explanation: Cycle at node 2.


Input: head = 1->2->3
Output: False
Explanation: No cycle.


Input: head = None
Output: False
Explanation: Empty list has no cycle.




39. Find the Middle of a Linked List
Problem: Find the middle node of a linked list.
Detailed Approach:

Use two pointers: slow moves one step, fast moves two steps.
When fast reaches the end (or fast.next is None), slow is at the middle.
For even-length lists, return the second middle node (e.g., for 1->2->3->4, return 3).
This requires a single pass and constant space.
Handle edge cases: empty list, single node.

Complexity:

Time: O(n) - single pass.
Space: O(1) - constant space.

def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

Sample Input/Output:

Input: head = 1->2->3->4->5
Output: 3->4->5
Explanation: Middle node is 3.


Input: head = 1->2->3->4
Output: 3->4
Explanation: Second middle node is 3.


Input: head = None
Output: None
Explanation: Empty list.




40. Remove Nth Node from End
Problem: Remove the nth node from the end of a linked list.
Detailed Approach:

Use two pointers: slow and fast, with a dummy node pointing to head.
Move fast n steps ahead.
Move both pointers until fast.next is None; slow will be at the node before the target.
Remove the target by setting slow.next = slow.next.next.
Return dummy.next.
Dummy node handles edge case of removing the head.
Handle edge cases: n = length, single node.

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

Sample Input/Output:

Input: head = 1->2->3->4->5, n = 2
Output: 1->2->3->5
Explanation: Remove 4 (2nd from end).


Input: head = 1, n = 1
Output: None
Explanation: Remove only node.


Input: head = 1->2, n = 2
Output: 2
Explanation: Remove head (1).




41. Add Two Numbers
Problem: Add two numbers represented as linked lists (digits in reverse order).
Detailed Approach:

Initialize a dummy node and curr pointer for the result list.
Use a carry variable for overflow.
While either list or carry exists:
Get values from lists (0 if None).
Compute sum = x + y + carry.
Create new node with sum % 10.
Update carry = sum // 10.
Advance pointers.


Return dummy.next.
This handles lists of different lengths and carry propagation.
Handle edge cases: empty lists, large numbers.

Complexity:

Time: O(max(n, m)) - n, m are list lengths.
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

Sample Input/Output:

Input: l1 = 2->4->3, l2 = 5->6->4
Output: 7->0->8
Explanation: 342 + 465 = 807.


Input: l1 = 0, l2 = 0
Output: 0
Explanation: 0 + 0 = 0.


Input: l1 = 9->9, l2 = 1
Output: 0->0->1
Explanation: 99 + 1 = 100.




42. Intersection of Two Linked Lists
Problem: Find the intersection point of two linked lists.
Detailed Approach:

Use two pointers: a for list A, b for list B.
Traverse both lists:
If a reaches end, switch to head of B.
If b reaches end, switch to head of A.
Move both one step per iteration.


If they meet, that’s the intersection; otherwise, no intersection (meet at None).
This works because a + c + b = b + c + a, where c is the common part.
Handle edge cases: no intersection, empty lists.

Complexity:

Time: O(n + m) - n, m are list lengths.
Space: O(1) - constant space.

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

Sample Input/Output:

Input: listA = 4->1->8->4->5, listB = 5->6->1->8->4->5, intersect at 8
Output: 8->4->5
Explanation: Lists intersect at node 8.


Input: listA = 1->2, listB = 3->4
Output: None
Explanation: No intersection.


Input: listA = None, listB = 1
Output: None
Explanation: Empty list A.




43. Palindrome Linked List
Problem: Check if a linked list is a palindrome.
Detailed Approach:

Find the middle node using slow and fast pointers (fast moves twice as fast).
Reverse the second half starting from slow.next.
Compare the first half (from head) with the reversed second half.
If all values match, it’s a palindrome; otherwise, not.
Optionally restore the list

