from collections import deque

def sliding_window_deque(arr, k):
    """
    Implements a sliding window using a deque.

    Args:
        arr: The input list or array.
        k: The size of the window.

    Returns:
        A list of results for each window (e.g., max, min, sum).
        This example will return a list of deques representing each window.
    """
    if not arr or k <= 0 or k > len(arr):
        return []  # Or raise an error, depending on desired behavior

    result = []
    window = deque()

    for i in range(len(arr)):
        # Add the current element to the window
        window.append(arr[i])

        # If the window has reached its desired size 'k'
        if len(window) == k:
            # Process the current window (e.g., find max, min, sum)
            # For this example, we'll just add a copy of the window to results
            result.append(list(window.copy())) # Storing a copy

            # Slide the window: remove the element from the left
            window.popleft()

    return result

# --- Example Usage ---
if __name__ == "__main__":
    data = [1, 3, -1, -3, 5, 3, 6, 7]
    window_size = 3

    windows = sliding_window_deque(data, window_size)
    print(f"Input array: {data}")
    print(f"Window size: {window_size}")
    print("Sliding windows:")
    for w in windows:
        print(w)

    print("\n--- Example: Finding max in each window ---")

    def sliding_window_max(arr, k):
        if not arr or k <= 0 or k > len(arr):
            return []

        result = []
        # The deque will store indices of elements in the current window.
        # It will be maintained such that elements are in decreasing order.
        # The head of the deque (dq[0]) will always be the index of the largest element.
        dq = deque()

        for i in range(len(arr)):
            # Remove elements from the left of the deque that are out of the current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove elements from the right of the deque that are smaller than the current element
            # This maintains the decreasing order property
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()

            dq.append(i)

            # Once the window is full (i.e., we have processed at least k elements)
            # the maximum element for the current window is at the front of the deque
            if i >= k - 1:
                result.append(arr[dq[0]])
        return result

    max_values = sliding_window_max(data, window_size)
    print(f"Input array: {data}")
    print(f"Window size: {window_size}")
    print("Maximums in each sliding window:")
    print(max_values)