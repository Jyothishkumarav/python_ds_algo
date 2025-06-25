# Data Structures Interview Preparation Guide

## 1. Arrays

### Overview
Arrays are contiguous memory locations storing elements of the same data type, accessed by index.

### Time & Space Complexity
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access    | O(1)           | O(1)            |
| Search    | O(n)           | O(1)            |
| Insertion | O(n)           | O(n)            |
| Deletion  | O(n)           | O(n)            |

### When to Use
- When you need constant-time access to elements by index
- When memory usage is critical (cache-friendly)
- When the size is relatively fixed or known in advance
- Mathematical computations, matrix operations

### Python Implementation
```python
# Python lists are dynamic arrays - use built-in list
arr = []

# Common operations:
arr.append(5)           # O(1) amortized - add to end
arr.insert(0, 1)        # O(n) - insert at index
arr.pop()               # O(1) - remove from end
arr.pop(0)              # O(n) - remove from index
arr[2]                  # O(1) - access by index
arr[1] = 10             # O(1) - set by index
len(arr)                # O(1) - get length
5 in arr                # O(n) - search

# For fixed-size arrays, use array module
import array
fixed_arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' for integers
```

---

## 2. Linked Lists

### Overview
A linear data structure where elements are stored in nodes, each containing data and a reference to the next node.

### Time & Space Complexity
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access    | O(n)           | O(1)            |
| Search    | O(n)           | O(1)            |
| Insertion | O(1)*          | O(1)            |
| Deletion  | O(1)*          | O(1)            |

*O(1) if you have reference to the node, O(n) if searching first

### When to Use
- When frequent insertions/deletions are needed
- When the size varies significantly
- When you don't need random access
- Implementing other data structures (stacks, queues)

### Python Implementation
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_head(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_tail(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def delete(self, val):
        if not self.head:
            return False
        
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            self.size -= 1
            return True
        return False
    
    def search(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False
    
    def display(self):
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
```

---

## 3. Stacks

### Overview
LIFO (Last In, First Out) data structure where elements are added and removed from the same end (top).

### Time & Space Complexity
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Push      | O(1)           | O(1)            |
| Pop       | O(1)           | O(1)            |
| Peek/Top  | O(1)           | O(1)            |
| Search    | O(n)           | O(1)            |

### When to Use
- Function call management (call stack)
- Expression evaluation and syntax parsing
- Undo operations
- Backtracking algorithms
- Browser history

### Python Implementation
```python
# Use built-in list as stack
stack = []

# Stack operations:
stack.append(5)         # Push - O(1)
stack.pop()             # Pop - O(1)
stack[-1]               # Peek/Top - O(1)
len(stack) == 0         # Check empty - O(1)
len(stack)              # Size - O(1)

# Alternative: Use collections.deque for better performance
from collections import deque
stack = deque()
stack.append(5)         # Push
stack.pop()             # Pop
stack[-1]               # Peek

# Example usage:
def is_balanced_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0
```

---

## 4. Queues

### Overview
FIFO (First In, First Out) data structure where elements are added at rear and removed from front.

### Time & Space Complexity
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Enqueue   | O(1)           | O(1)            |
| Dequeue   | O(1)           | O(1)            |
| Front     | O(1)           | O(1)            |
| Rear      | O(1)           | O(1)            |

### When to Use
- BFS traversal
- Process scheduling
- Handling requests in web servers
- Print queue management
- Level-order tree traversal

### Python Implementation
```python
from collections import deque

# Use collections.deque for efficient queue operations
queue = deque()

# Queue operations:
queue.append(5)         # Enqueue - O(1)
queue.popleft()         # Dequeue - O(1)
queue[0]                # Front - O(1)
queue[-1]               # Rear - O(1)
len(queue) == 0         # Check empty - O(1)
len(queue)              # Size - O(1)

# Alternative: Use queue.Queue for thread-safe operations
import queue
q = queue.Queue()
q.put(5)                # Enqueue
q.get()                 # Dequeue (blocks if empty)
q.empty()               # Check if empty
q.qsize()               # Size

# Example usage - BFS traversal:
def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])
    
    return result

# Priority Queue using heapq
import heapq
pq = []
heapq.heappush(pq, (priority, item))
priority, item = heapq.heappop(pq)
```

---

## 5. Hash Maps (Dictionaries)

### Overview
Data structure that maps keys to values using a hash function for fast access.

### Time & Space Complexity
| Operation | Average Time | Worst Time | Space Complexity |
|-----------|-------------|------------|------------------|
| Search    | O(1)        | O(n)       | O(n)            |
| Insert    | O(1)        | O(n)       | O(n)            |
| Delete    | O(1)        | O(n)       | O(n)            |

### When to Use
- When you need fast key-based lookups
- Counting frequencies
- Caching/memoization
- Database indexing
- Implementing other data structures

### Python Implementation
```python
# Use built-in dict - highly optimized hash table
hashmap = {}

# Basic operations:
hashmap['key'] = 'value'    # Insert/Update - O(1) average
value = hashmap['key']      # Access - O(1) average
del hashmap['key']          # Delete - O(1) average
'key' in hashmap            # Check existence - O(1) average
hashmap.get('key', default) # Safe access with default

# Useful methods:
hashmap.keys()              # Get all keys
hashmap.values()            # Get all values
hashmap.items()             # Get key-value pairs
hashmap.pop('key', default) # Remove and return value

# Counter for frequency counting
from collections import Counter
counter = Counter([1, 2, 2, 3, 3, 3])
# Result: Counter({3: 3, 2: 2, 1: 1})

# DefaultDict for default values
from collections import defaultdict
dd = defaultdict(list)      # Creates empty list for new keys
dd = defaultdict(int)       # Creates 0 for new keys

# Example usage - Two Sum problem:
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Example usage - Group Anagrams:
def group_anagrams(strs):
    anagram_map = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagram_map[key].append(s)
    return list(anagram_map.values())
```

---

## 6. Binary Trees

### Overview
Hierarchical data structure where each node has at most two children (left and right).

### Time & Space Complexity (Binary Search Tree)
| Operation | Average Time | Worst Time | Space Complexity |
|-----------|-------------|------------|------------------|
| Search    | O(log n)    | O(n)       | O(log n)        |
| Insert    | O(log n)    | O(n)       | O(log n)        |
| Delete    | O(log n)    | O(n)       | O(log n)        |

### When to Use
- Hierarchical data representation
- Fast searching in sorted data
- Expression parsing
- File system structures
- Decision trees

### Python Implementation
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        
        return node
    
    def search(self, val):
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        if not node or node.val == val:
            return node is not None
        
        if val < node.val:
            return self._search_recursive(node.left, val)
        return self._search_recursive(node.right, val)
    
    def delete(self, val):
        self.root = self._delete_recursive(self.root, val)
    
    def _delete_recursive(self, node, val):
        if not node:
            return node
        
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Node to delete found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node has both children
            min_node = self._find_min(node.right)
            node.val = min_node.val
            node.right = self._delete_recursive(node.right, min_node.val)
        
        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)
```

---

## 7. Heaps

### Overview
Complete binary tree where parent nodes have priority over children (min-heap or max-heap).

### Time & Space Complexity
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert    | O(log n)       | O(1)            |
| Extract   | O(log n)       | O(1)            |
| Peek      | O(1)           | O(1)            |
| Build     | O(n)           | O(n)            |

### When to Use
- Priority queues
- Heap sort algorithm
- Finding k largest/smallest elements
- Dijkstra's shortest path
- Task scheduling

### Python Implementation
```python
import heapq

# Python's heapq module implements min-heap
heap = []

# Basic operations:
heapq.heappush(heap, 5)     # Insert - O(log n)
min_val = heapq.heappop(heap)  # Extract min - O(log n)
min_val = heap[0]           # Peek min - O(1)
heapq.heapify(heap)         # Convert list to heap - O(n)

# For max-heap, negate values:
max_heap = []
heapq.heappush(max_heap, -5)  # Push -5 for max behavior
max_val = -heapq.heappop(max_heap)  # Get actual max value

# Advanced operations:
heapq.nlargest(k, heap)     # Get k largest elements
heapq.nsmallest(k, heap)    # Get k smallest elements
heapq.heappushpop(heap, item)  # Push then pop
heapq.heapreplace(heap, item)  # Pop then push

# Priority Queue with custom objects:
import heapq
from dataclasses import dataclass

@dataclass
class Task:
    priority: int
    name: str
    
    def __lt__(self, other):
        return self.priority < other.priority

pq = []
heapq.heappush(pq, Task(1, "High priority"))
heapq.heappush(pq, Task(5, "Low priority"))
next_task = heapq.heappop(pq)

# Example usage - K largest elements:
def find_k_largest(nums, k):
    return heapq.nlargest(k, nums)

# Example usage - Merge k sorted lists:
def merge_k_sorted_lists(lists):
    heap = []
    result = []
    
    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result
```

---

## Common Interview Problem Patterns

### 1. Two Pointers
**Use Case**: Array problems, finding pairs, palindromes
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### 2. Sliding Window
**Use Case**: Substring problems, arrays with contiguous elements
```python
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### 3. Fast & Slow Pointers
**Use Case**: Cycle detection, finding middle element
```python
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

## Problem-Solving Guide: When to Use Which Data Structure

### 🔍 Problem Analysis Framework

**Step 1: Identify the Problem Pattern**
- What operations are you performing most frequently?
- Do you need to maintain order?
- Are you looking for specific elements or patterns?
- What are the constraints (time/space)?

**Step 2: Match Pattern to Data Structure**

---

## Arrays/Lists Problems

### **Pattern Recognition:**
- "Find/search in sorted array"
- "Subarray/substring problems"
- "Two pointers/sliding window"
- "Index-based access needed"

### **Classic Problems:**

**1. Two Sum (Easy)**
```python
# Problem: Find two numbers that add up to target
# DS Choice: HashMap for O(1) lookup
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```
**Why HashMap?** Need fast lookup to find complement.

**2. Maximum Subarray (Medium)**
```python
# Problem: Find contiguous subarray with largest sum
# DS Choice: Array with single pass (Kadane's algorithm)
def max_subarray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```
**Why Array?** Sequential access, no additional DS needed.

**3. Sliding Window Maximum (Hard)**
```python
# Problem: Find maximum in each sliding window of size k
# DS Choice: Deque (maintains decreasing order)
from collections import deque
def max_sliding_window(nums, k):
    dq = deque()  # stores indices
    result = []
    
    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```
**Why Deque?** Need to add/remove from both ends efficiently.

---

## Linked List Problems

### **Pattern Recognition:**
- "Reverse/modify list structure"
- "Cycle detection"
- "Merge multiple lists"
- "Two pointers (fast/slow)"

### **Classic Problems:**

**4. Reverse Linked List (Easy)**
```python
# Problem: Reverse a linked list
# DS Choice: Linked List with three pointers
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev
```
**Why Linked List?** Problem inherently about list structure.

**5. Detect Cycle (Medium)**
```python
# Problem: Detect if linked list has cycle
# DS Choice: Two pointers (Floyd's algorithm)
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
**Why Two Pointers?** Space-efficient cycle detection.

**6. Merge K Sorted Lists (Hard)**
```python
# Problem: Merge k sorted linked lists
# DS Choice: Min-heap for efficient merging
import heapq
def merge_k_lists(lists):
    heap = []
    dummy = ListNode(0)
    current = dummy
    
    # Add first node from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
```
**Why Heap?** Efficiently find minimum among k elements.

---

## Stack Problems

### **Pattern Recognition:**
- "Matching/balancing (parentheses)"
- "Nearest greater/smaller element"
- "Expression evaluation"
- "Undo operations"
- "DFS traversal"

### **Classic Problems:**

**7. Valid Parentheses (Easy)**
```python
# Problem: Check if parentheses are balanced
# DS Choice: Stack for LIFO matching
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0
```
**Why Stack?** Need to match most recent opening bracket.

**8. Daily Temperatures (Medium)**
```python
# Problem: Find next warmer day for each temperature
# DS Choice: Monotonic stack
def daily_temperatures(temperatures):
    stack = []  # stores indices
    result = [0] * len(temperatures)
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    
    return result
```
**Why Monotonic Stack?** Find next greater element efficiently.

**9. Largest Rectangle in Histogram (Hard)**
```python
# Problem: Find largest rectangle area in histogram
# DS Choice: Stack to track increasing heights
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area
```
**Why Stack?** Track bars that can extend to current position.

---

## Queue Problems

### **Pattern Recognition:**
- "Level-order traversal"
- "BFS problems"
- "Process in order (FIFO)"
- "Sliding window with order"

### **Classic Problems:**

**10. Binary Tree Level Order Traversal (Medium)**
```python
# Problem: Traverse tree level by level
# DS Choice: Queue for BFS
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
```
**Why Queue?** Process nodes in order they were discovered.

**11. Rotting Oranges (Medium)**
```python
# Problem: Find time for all oranges to rot (multi-source BFS)
# DS Choice: Queue for simultaneous BFS from multiple sources
from collections import deque
def oranges_rotting(grid):
    queue = deque()
    fresh = 0
    
    # Find all rotten oranges and count fresh ones
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_time = 0
    
    while queue:
        x, y, time = queue.popleft()
        max_time = max(max_time, time)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                grid[nx][ny] = 2
                fresh -= 1
                queue.append((nx, ny, time + 1))
    
    return max_time if fresh == 0 else -1
```
**Why Queue?** Simultaneous spreading from multiple sources.

---

## Hash Map Problems

### **Pattern Recognition:**
- "Frequency counting"
- "Fast lookup/existence check"
- "Mapping relationships"
- "Avoiding nested loops"

### **Classic Problems:**

**12. Group Anagrams (Medium)**
```python
# Problem: Group strings that are anagrams
# DS Choice: HashMap with sorted string as key
from collections import defaultdict
def group_anagrams(strs):
    anagram_map = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        anagram_map[key].append(s)
    
    return list(anagram_map.values())
```
**Why HashMap?** Group by common characteristic (sorted letters).

**13. Subarray Sum Equals K (Medium)**
```python
# Problem: Count subarrays with sum equal to k
# DS Choice: HashMap to store prefix sums
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
```
**Why HashMap?** Efficiently find if complement exists.

**14. Longest Consecutive Sequence (Hard)**
```python
# Problem: Find longest consecutive sequence in unsorted array
# DS Choice: Set for O(1) lookup
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Only start counting from the beginning of sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            longest = max(longest, current_length)
    
    return longest
```
**Why Set?** Fast membership testing.

---

## Heap Problems

### **Pattern Recognition:**
- "Kth largest/smallest"
- "Top K elements"
- "Merge sorted arrays/lists"
- "Priority-based processing"

### **Classic Problems:**

**15. Kth Largest Element (Medium)**
```python
# Problem: Find kth largest element in array
# DS Choice: Min-heap of size k
import heapq
def find_kth_largest(nums, k):
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]
```
**Why Min-heap?** Maintain k largest elements, root is kth largest.

**16. Meeting Rooms II (Medium)**
```python
# Problem: Find minimum conference rooms needed
# DS Choice: Min-heap to track end times
import heapq
def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    heap = []  # Min-heap for end times
    
    for start, end in intervals:
        # If earliest meeting has ended, reuse room
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        
        heapq.heappush(heap, end)
    
    return len(heap)
```
**Why Min-heap?** Track which room becomes available first.

**17. Merge K Sorted Arrays (Hard)**
```python
# Problem: Merge k sorted arrays
# DS Choice: Min-heap for efficient merging
import heapq
def merge_k_sorted_arrays(arrays):
    heap = []
    result = []
    
    # Initialize heap with first element from each array
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    
    while heap:
        val, array_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same array
        if elem_idx + 1 < len(arrays[array_idx]):
            next_val = arrays[array_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, array_idx, elem_idx + 1))
    
    return result
```
**Why Min-heap?** Always get minimum among k elements.

---

## Tree Problems

### **Pattern Recognition:**
- "Hierarchical relationships"
- "Path problems"
- "Ancestor/descendant queries"
- "Recursive structure"

### **Classic Problems:**

**18. Validate Binary Search Tree (Medium)**
```python
# Problem: Check if tree is valid BST
# DS Choice: Recursion with bounds
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    
    if root.val <= min_val or root.val >= max_val:
        return False
    
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))
```
**Why Recursion?** Tree structure is naturally recursive.

**19. Lowest Common Ancestor (Medium)**
```python
# Problem: Find LCA of two nodes in BST
# DS Choice: Tree traversal with BST property
def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None
```
**Why BST Property?** Use ordering to guide search.

**20. Serialize and Deserialize Binary Tree (Hard)**
```python
# Problem: Convert tree to string and back
# DS Choice: Queue for level-order traversal
from collections import deque
class Codec:
    def serialize(self, root):
        if not root:
            return ""
        
        queue = deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        return ",".join(result)
    
    def deserialize(self, data):
        if not data:
            return None
        
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        
        while queue and i < len(values):
            node = queue.popleft()
            
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        
        return root
```
**Why Queue?** Level-order traversal for complete serialization.

---

## Decision Tree: Choosing the Right Data Structure

```
Problem Analysis:
├── Need fast random access by index?
│   └── YES → Array/List
├── Need LIFO (Last In, First Out)?
│   └── YES → Stack
├── Need FIFO (First In, First Out)?
│   └── YES → Queue
├── Need fast key-based lookup?
│   └── YES → HashMap/Set
├── Need to maintain sorted order with insertions?
│   └── YES → Heap or Balanced BST
├── Need to find min/max repeatedly?
│   └── YES → Heap
├── Working with hierarchical data?
│   └── YES → Tree
├── Need to track sequences/chains?
│   └── YES → Linked List
└── Need to combine multiple structures?
    └── YES → Use appropriate combination
```

---

## Interview Tips

### Problem-Solving Approach
1. **Understand the problem**: Ask clarifying questions
2. **Think of examples**: Work through test cases
3. **Consider edge cases**: Empty inputs, single elements, etc.
4. **Choose appropriate data structure**: Based on operations needed
5. **Start with brute force**: Then optimize
6. **Analyze complexity**: Time and space complexity
7. **Code cleanly**: Use meaningful variable names
8. **Test your solution**: Walk through with examples

### Data Structure Selection Guidelines
- **Need fast access by index?** → Array
- **Frequent insertions/deletions?** → Linked List
- **LIFO operations?** → Stack
- **FIFO operations?** → Queue  
- **Fast key-based lookup?** → Hash Map
- **Sorted data with fast search?** → Binary Search Tree
- **Priority-based operations?** → Heap

### Complexity Analysis Framework
Always analyze:
- **Best case**: Optimal input scenario
- **Average case**: Expected performance
- **Worst case**: Pessimistic scenario
- **Space complexity**: Additional memory used
- **In-place vs out-of-place**: Memory usage patterns