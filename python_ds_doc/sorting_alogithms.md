# Popular Sorting Algorithms - Complexity & Approaches

## 1. Bubble Sort
**Approach:** Comparison-based, repeatedly steps through the list, compares adjacent elements and swaps them if they're in wrong order.

**Time Complexity:**
- Best Case: O(n) - when array is already sorted
- Average Case: O(n²)
- Worst Case: O(n²) - when array is reverse sorted

**Space Complexity:** O(1) - in-place sorting

**Representation:**
```
Pass 1: [64, 34, 25, 12, 22, 11, 90]
        [34, 64, 25, 12, 22, 11, 90] (swap 64,34)
        [34, 25, 64, 12, 22, 11, 90] (swap 64,25)
        ... continues until largest element bubbles to end
```

## 2. Selection Sort
**Approach:** Finds the minimum element from unsorted portion and places it at the beginning.

**Time Complexity:**
- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)

**Space Complexity:** O(1) - in-place sorting

**Representation:**
```
Initial: [64, 25, 12, 22, 11, 90]
Step 1:  [11, 25, 12, 22, 64, 90] (11 is minimum, swap with first)
Step 2:  [11, 12, 25, 22, 64, 90] (12 is next minimum)
... continues
```

## 3. Insertion Sort
**Approach:** Builds sorted array one element at a time by inserting each element into its correct position.

**Time Complexity:**
- Best Case: O(n) - when array is already sorted
- Average Case: O(n²)
- Worst Case: O(n²) - when array is reverse sorted

**Space Complexity:** O(1) - in-place sorting

**Representation:**
```
Initial: [5, 2, 4, 6, 1, 3]
Step 1:  [2, 5, 4, 6, 1, 3] (insert 2 before 5)
Step 2:  [2, 4, 5, 6, 1, 3] (insert 4 between 2 and 5)
... continues
```

## 4. Merge Sort
**Approach:** Divide-and-conquer algorithm that divides array into halves, sorts them separately, then merges them.

**Time Complexity:**
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

**Space Complexity:** O(n) - requires additional space for merging

**Representation:**
```
                [38, 27, 43, 3, 9, 82, 10]
                      /              \
            [38, 27, 43, 3]      [9, 82, 10]
               /      \            /      \
         [38, 27]   [43, 3]   [9, 82]   [10]
          /    \     /    \    /    \      |
       [38]  [27] [43]  [3] [9]  [82]   [10]
         \    /     \    /    \    /      |
       [27, 38]   [3, 43]   [9, 82]   [10]
            \        /         \        /
         [3, 27, 38, 43]    [9, 10, 82]
                  \              /
            [3, 9, 10, 27, 38, 43, 82]
```

## 5. Quick Sort
**Approach:** Divide-and-conquer algorithm that selects a pivot element and partitions array around it.

**Time Complexity:**
- Best Case: O(n log n) - when pivot divides array evenly
- Average Case: O(n log n)
- Worst Case: O(n²) - when pivot is always smallest/largest

**Space Complexity:** O(log n) - for recursion stack

**Representation:**
```
Initial: [10, 7, 8, 9, 1, 5] (pivot = 5)
Partition: [1, 5, 8, 9, 10, 7] (elements ≤5 left, >5 right)
Recursively sort left [1] and right [8, 9, 10, 7]
Continue until fully sorted
```

## 6. Heap Sort
**Approach:** Uses binary heap data structure to repeatedly extract maximum/minimum element.

**Time Complexity:**
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

**Space Complexity:** O(1) - in-place sorting

**Representation:**
```
Build Max Heap: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
                      16
                   /      \
                 14        10
               /   \     /   \
              8     7   9     3
            /  \   /
           2   4  1

Extract max (16), place at end, heapify remaining
Continue until heap is empty
```

## 7. Counting Sort
**Approach:** Non-comparison based sorting that counts occurrences of each distinct element.

**Time Complexity:**
- Best Case: O(n + k) where k is range of input
- Average Case: O(n + k)
- Worst Case: O(n + k)

**Space Complexity:** O(k) - for counting array

**Representation:**
```
Input: [4, 2, 2, 8, 3, 3, 1]
Count: [0, 1, 2, 2, 1, 0, 0, 0, 1] (index represents value)
Output: [1, 2, 2, 3, 3, 4, 8]
```

## 8. Radix Sort
**Approach:** Non-comparison based sorting that processes digits from least to most significant.

**Time Complexity:**
- Best Case: O(d × (n + k)) where d is number of digits
- Average Case: O(d × (n + k))
- Worst Case: O(d × (n + k))

**Space Complexity:** O(n + k)

**Representation:**
```
Input: [170, 45, 75, 90, 2, 802, 24, 66]

Sort by ones place:    [170, 90, 2, 802, 24, 45, 75, 66]
Sort by tens place:    [2, 802, 24, 45, 66, 170, 75, 90]
Sort by hundreds place: [2, 24, 45, 66, 75, 90, 170, 802]
```

## 9. Bucket Sort
**Approach:** Distributes elements into buckets, sorts individual buckets, then concatenates them.

**Time Complexity:**
- Best Case: O(n + k) when elements are uniformly distributed
- Average Case: O(n + k)
- Worst Case: O(n²) when all elements fall into same bucket

**Space Complexity:** O(n + k)

**Representation:**
```
Input: [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

Bucket 0: [0.1234]
Bucket 1: []
Bucket 2: []
Bucket 3: [0.3434]
Bucket 4: []
Bucket 5: [0.565]
Bucket 6: [0.656, 0.665]
Bucket 7: []
Bucket 8: [0.897]
Bucket 9: []

Sort each bucket individually, then concatenate
```

## Summary Comparison

| Algorithm      | Best Case    | Average Case | Worst Case   | Space   | Stable | In-Place |
|----------------|--------------|--------------|--------------|---------|--------|----------|
| Bubble Sort    | O(n)         | O(n²)        | O(n²)        | O(1)    | Yes    | Yes      |
| Selection Sort | O(n²)        | O(n²)        | O(n²)        | O(1)    | No     | Yes      |
| Insertion Sort | O(n)         | O(n²)        | O(n²)        | O(1)    | Yes    | Yes      |
| Merge Sort     | O(n log n)   | O(n log n)   | O(n log n)   | O(n)    | Yes    | No       |
| Quick Sort     | O(n log n)   | O(n log n)   | O(n²)        | O(log n)| No     | Yes      |
| Heap Sort      | O(n log n)   | O(n log n)   | O(n log n)   | O(1)    | No     | Yes      |
| Counting Sort  | O(n + k)     | O(n + k)     | O(n + k)     | O(k)    | Yes    | No       |
| Radix Sort     | O(d(n + k))  | O(d(n + k))  | O(d(n + k))  | O(n + k)| Yes    | No       |
| Bucket Sort    | O(n + k)     | O(n + k)     | O(n²)        | O(n + k)| Yes    | No       |

## When to Use Which Algorithm

- **Small datasets (n < 50):** Insertion Sort
- **Nearly sorted data:** Insertion Sort or Bubble Sort
- **Guaranteed O(n log n):** Merge Sort or Heap Sort
- **Average case performance:** Quick Sort
- **Integer sorting with small range:** Counting Sort
- **Floating point numbers in uniform range:** Bucket Sort
- **Large integers:** Radix Sort
- **Memory constrained:** Heap Sort or Quick Sort (in-place variants)